import os
import time
from pathlib import Path
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def main():
    print("🔄 Running training as a native python process to eliminate RAM crashes...")
    
    # 1. Setup workspace boundaries
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    DATA_DIR = PROJECT_ROOT / "data"
    MODELS_DIR = PROJECT_ROOT / "models"
    MODELS_DIR.mkdir(exist_ok=True)
    
    BATCH_SIZE = 16   
    IMG_SIZE = (128, 128)  
    EPOCHS = 5

    data_transforms = transforms.Compose([
        transforms.Resize(IMG_SIZE),
        transforms.ToTensor(),
    ])

    print("Streaming data directly from split folders...")
    train_dataset = datasets.ImageFolder(root=str(DATA_DIR / "train"), transform=data_transforms)
    val_dataset   = datasets.ImageFolder(root=str(DATA_DIR / "val"), transform=data_transforms)

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
    val_loader   = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

    num_classes = len(train_dataset.classes)
    print(f"✅ Active DataLoaders verified for {num_classes} plant categories.")

    # 2. Define Custom Stable CNN Architecture
    class SimplePlantCNN(nn.Module):
        def __init__(self, num_classes):
            super(SimplePlantCNN, self).__init__()
            self.features = nn.Sequential(
                nn.Conv2d(3, 16, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.MaxPool2d(2, 2),
                nn.Conv2d(16, 32, kernel_size=3, padding=1),
                nn.ReLU(),
                nn.MaxPool2d(2, 2),
            )
            self.classifier = nn.Sequential(
                nn.Flatten(),
                nn.Linear(32 * 32 * 32, 128),
                nn.ReLU(),
                nn.Dropout(0.3),
                nn.Linear(128, num_classes)
            )

        def forward(self, x):
            x = self.features(x)
            x = self.classifier(x)
            return x

    model = SimplePlantCNN(num_classes=num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 3. Production Training Loop
    print(f"\n🚀 Launching training loop for {EPOCHS} epochs...")
    for epoch in range(EPOCHS):
        start_time = time.time()
        
        # --- TRAINING PHASE ---
        model.train()
        train_loss, train_correct, total_train_samples = 0.0, 0, 0
        
        for step, (imgs, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item() * imgs.size(0)
            _, preds = torch.max(outputs, 1)
            train_correct += torch.sum(preds == labels).item()
            total_train_samples += imgs.size(0)
            
            if step % 300 == 0 and step > 0:
                current_acc = (train_correct / total_train_samples) * 100
                print(f"   Epoch {epoch+1:02d} | Step {step:04d} | Batch Loss: {loss.item():.4f} | Training Acc: {current_acc:.2f}%")
                
        epoch_train_loss = train_loss / total_train_samples
        epoch_train_acc = (train_correct / total_train_samples) * 100
        
        # --- VALIDATION PHASE ---
        model.eval()
        val_loss, val_correct, total_val_samples = 0.0, 0, 0
        
        with torch.no_grad():
            for imgs, labels in val_loader:
                outputs = model(imgs)
                loss = criterion(outputs, labels)
                val_loss += loss.item() * imgs.size(0)
                _, preds = torch.max(outputs, 1)
                val_correct += torch.sum(preds == labels).item()
                total_val_samples += imgs.size(0)
                
        epoch_val_loss = val_loss / total_val_samples
        epoch_val_acc = (val_correct / total_val_samples) * 100
        elapsed_time = time.time() - start_time
        
        print(f"\n========================================================")
        print(f"🏆 EPOCH {epoch+1}/{EPOCHS} COMPLETE ({elapsed_time:.1f}s)")
        print(f"📈 Train Loss: {epoch_train_loss:.4f} | Train Acc: {epoch_train_acc:.2f}%")
        print(f"📊 Val Loss:   {epoch_val_loss:.4f} | Val Acc:   {epoch_val_acc:.2f}%")
        print(f"========================================================\n")
        
        torch.save(model.state_dict(), MODELS_DIR / f"plant_cnn_epoch_{epoch+1}.pth")

    print("🎉 Done! Model weights saved inside the 'models/' directory.")

if __name__ == "__main__":
    main()
