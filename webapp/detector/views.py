import os
import torch
import traceback
from pathlib import Path
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from torchvision import transforms, models
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    """
    Mobile API Authentication Endpoint.
    Accepts JSON raw fields 'username' (email) and 'password'.
    Returns success status if credentials match a database user.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {"status": "error", "error": "Missing email or password fields."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Django matches against registered User models securely
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            return Response({
                "status": "success",
                "message": f"Welcome back, {user.username}!",
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"status": "error", "error": "This user account has been deactivated."},
                status=status.HTTP_403_FORBIDDEN
            )
    else:
        return Response(
            {"status": "error", "error": "Invalid email or password credentials."},
            status=status.HTTP_401_UNAUTHORIZED
        )




# Import unified text parameters
from .treatments import DISEASE_TREATMENTS

# ========================================================
# 1. ARCHITECTURES DEFINITION
# ========================================================
class SimplePlantCNN(torch.nn.Module):
    def __init__(self, num_classes=38):
        super(SimplePlantCNN, self).__init__()
        self.features = torch.nn.Sequential(
            torch.nn.Conv2d(3, 16, kernel_size=3, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
            torch.nn.Conv2d(16, 32, kernel_size=3, padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2, 2),
        )
        self.classifier = torch.nn.Sequential(
            torch.nn.Flatten(),
            torch.nn.Linear(32 * 32 * 32, 128),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(128, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

# ========================================================
# 2. RUNTIME PIPELINE LAYER INITIALIZATION
# ========================================================
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "plant_cnn_epoch_5.pth"

CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 
    'Tomato___healthy'
]

VALID_ORGANIC_IDS = set(range(936, 950)) | {984, 985, 986, 987, 988}

disease_model = SimplePlantCNN(num_classes=38)
if MODEL_PATH.exists():
    disease_model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
    disease_model.eval()
    print("✅ Custom Pathology CNN verified.")
else:
    print("⚠️ Custom weights file not found.")

gatekeeper_model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
gatekeeper_model.eval()

transform_disease = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

transform_gatekeeper = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# ========================================================
# 3. INTERFACE ENDPOINTS
# ========================================================
def index(request):
    return render(request, 'detector/index.html')

def predict_disease(request):
    # Keep web template views running normally for local browser uploads
    return render(request, 'detector/index.html')

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def api_predict_disease(request):
    if 'image' not in request.FILES:
        return Response({"status": "error", "error": "Missing 'image' field."}, status=status.HTTP_400_BAD_REQUEST)

    uploaded_file = request.FILES['image']
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    
    if file_extension not in ['.jpg', '.jpeg', '.png', '.bmp', '.webp']:
        return Response({"status": "error", "error": "Unsupported picture extension format."}, status=status.HTTP_400_BAD_REQUEST)

    fs = FileSystemStorage()
    filename = fs.save(uploaded_file.name, uploaded_file)
    file_path = fs.path(filename)

    try:
        img = Image.open(file_path).convert('RGB')

        # STAGE 1: Flexible Gatekeeper Evaluation
        gatekeeper_tensor = transform_gatekeeper(img).unsqueeze(0)
        with torch.no_grad():
            gatekeeper_output = gatekeeper_model(gatekeeper_tensor)
            _, top_5_indices = torch.topk(gatekeeper_output, 5, dim=1)

        predicted_ids = top_5_indices[0].tolist()
        has_foliage = any(pid in VALID_ORGANIC_IDS for pid in predicted_ids)

        if not has_foliage:
            probabilities = torch.nn.functional.softmax(gatekeeper_output, dim=1)
            if torch.max(probabilities).item() > 0.40:
                return Response({"status": "error", "error": "Security check failed: Image does not appear to contain a plant leaf."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        # STAGE 2: Pathology Inference
        disease_tensor = transform_disease(img).unsqueeze(0)
        with torch.no_grad():
            disease_output = disease_model(disease_tensor)
            probabilities = torch.nn.functional.softmax(disease_output, dim=1)
            confidence, predicted_idx = torch.max(probabilities, 1)

        confidence_score = confidence.item() * 100
        predicted_class = CLASS_NAMES[predicted_idx.item()]
        display_name = predicted_class.replace("___", " - ").replace("_", " ")

        # Match healthy classes securely or map to treatments base fallback keys
        treatment_data = DISEASE_TREATMENTS.get(predicted_class, {
            'organic': 'Foliage appears healthy. Maintain current balanced organic companion planting schedules.',
            'chemical': 'No chemical spray applications are required for this healthy crop specimen.',
            'prevention': 'Continue standard bi-weekly crop scouting procedures across the field perimeter.'
        })

        if confidence_score >= 40.0:
            # Structuring the nested layout keys to precisely match App.js components mapping structure!
            return Response({
                "status": "success",
                "diagnosis": {
                    "raw_class": predicted_class,
                    "display_name": display_name,
                    "confidence": f"{confidence_score:.2f}%"
                },
                "treatment_protocol": {
                    "organic_remedy": treatment_data['organic'],
                    "chemical_control": treatment_data['chemical'],
                    "preventative_action": treatment_data['prevention']
                }
            }, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "error": "Ambiguous input features. Please re-capture close up under clear daylight conditions."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        print("\n❌ BACKEND RUNTIME FAILURE:")
        traceback.print_exc()
        return Response({"status": "error", "error": f"Internal matrix crash: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
