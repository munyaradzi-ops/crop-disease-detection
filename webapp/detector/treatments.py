# Comprehensive knowledge base mapping for all 38 PlantVillage classes
DISEASE_TREATMENTS = {
    # APPLES
    'Apple___Apple_scab': {
        'organic': 'Apply sulfur-based or copper-based fungicides early in the spring season.',
        'chemical': 'Use protective fungicides containing Captan or Myclobutanil.',
        'prevention': 'Rake and destroy fallen leaves in autumn to prevent spores from overwintering.'
    },
    'Apple___Black_rot': {
        'organic': 'Prune away dead wood, mummified fruit, and infected branches during winter.',
        'chemical': 'Apply targeted fungicides containing Captan or Mancozeb from green tip stage onward.',
        'prevention': 'Keep the orchard clean and pick all rotten fruit off the trees immediately.'
    },
    'Apple___Cedar_apple_rust': {
        'organic': 'Remove nearby wild juniper or cedar trees if possible, or pick off rust galls manually.',
        'chemical': 'Apply systemic fungicides containing Myclobutanil or Triadimefon.',
        'prevention': 'Plant rust-resistant apple cultivars like Liberty, Freedom, or Enterprise.'
    },
    'Apple___healthy': {
        'organic': 'Apply standard organic compost and organic mulch around the root zone.',
        'chemical': 'No chemical interventions required for healthy foliage.',
        'prevention': 'Maintain regular watering schedules and monitor for early signs of pests.'
    },

    # BLUEBERRY
    'Blueberry___healthy': {
        'organic': 'Maintain acidic soil pH (4.5-4.8) using organic elemental sulfur or peat moss.',
        'chemical': 'No chemical interventions required.',
        'prevention': 'Prune older canes annually to maintain optimal sunlight penetration and airflow.'
    },

    # CHERRY
    'Cherry_(including_sour)___Powdery_mildew': {
        'organic': 'Spray organic neem oil, potassium bicarbonate, or horticultural oil options.',
        'chemical': 'Apply targeted fungicides containing Myclobutanil or Fenbuconazole.',
        'prevention': 'Prune the inner canopy heavily to reduce humidity and increase air circulation.'
    },
    'Cherry_(including_sour)___healthy': {
        'organic': 'Apply organic matter to the base baseline ring annually.',
        'chemical': 'No chemical controls required.',
        'prevention': 'Protect fruit from birds using netting and monitor for early aphid clusters.'
    },

    # CORN
    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': {
        'organic': 'Incorporate strict crop rotation profiles with non-host crops like soybeans.',
        'chemical': 'Apply foliar fungicides such as strobilurins or triazoles if spots appear early.',
        'prevention': 'Use resistant crop hybrids and practice tillage to bury infected stalk residue.'
    },
    'Corn_(maize)___Common_rust_': {
        'organic': 'Usually minor; apply compost teas to boost plant vigor.',
        'chemical': 'Foliar fungicides containing Pyraclostrobin can be used for severe commercial outbreaks.',
        'prevention': 'Select corn varieties possessing specific rust resistance genes (Rp genes).'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'organic': 'Implement a 2-year crop rotation out of maize to break the pathogen lifecycle.',
        'chemical': 'Apply group 3 or group 11 professional fungicides during the silking stage.',
        'prevention': 'Manage field drainage channels and reduce plant density to decrease leaf wetness.'
    },
    'Corn_(maize)___healthy': {
        'organic': 'Ensure adequate nitrogen levels using organic blood meal or legume covers.',
        'chemical': 'No chemical applications needed.',
        'prevention': 'Practice proper spacing and keep fields clear of dynamic grass weeds.'
    },

    # GRAPE
    'Grape___Black_rot': {
        'organic': 'Manually remove and burn infected berries, leaves, and tendrils.',
        'chemical': 'Apply preventative copper-mancozeb mixes or Mancozeb systematically from bud break.',
        'prevention': 'Keep vines trained off the ground and maintain clean floor weed management.'
    },
    'Grape___Esca_(Black_Measles)': {
        'organic': 'No direct organic cure. Protect large pruning wounds using organic paste shields.',
        'chemical': 'Apply wound-protectant fungicides directly to vines during winter pruning steps.',
        'prevention': 'Sanitize pruning tools between individual vines using 70% isopropyl alcohol.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'organic': 'Apply fixed copper sprays post-harvest to lower overwintering spore loads.',
        'chemical': 'Apply multi-site protectant chemical fungicides like Captan early in wet seasons.',
        'prevention': 'Rake up and burn all fallen leaves and vine debris at the end of autumn.'
    },
    'Grape___healthy': {
        'organic': 'Apply well-rotted manure compost and mulch to suppress ground weeds.',
        'chemical': 'No chemical intervention required.',
        'prevention': 'Practice regular canopy thinning to maximize leaf exposure to wind and sun.'
    },

    # ORANGE
    'Orange___Haunglongbing_(Citrus_greening)': {
        'organic': 'No cure exists. Apply nutritional sprays to support tree vigor temporarily.',
        'chemical': 'Control the Asian citrus psyllid vector using systemic imidacloprid insecticides.',
        'prevention': 'Immediately remove and burn infected trees to protect surrounding orchards.'
    },

    # PEACH
    'Peach___Bacterial_spot': {
        'organic': 'Apply organic copper sprays combined with dormant oil during late dormancy.',
        'chemical': 'Use oxytetracycline or protective copper-mancozeb applications during the season.',
        'prevention': 'Avoid overhead irrigation systems; prioritize planting bacterial-spot resistant cultivars.'
    },
    'Peach___healthy': {
        'organic': 'Maintain a wide mulched ring around the base to keep weeds clear.',
        'chemical': 'No chemical controls required.',
        'prevention': 'Thin developing fruit early in the season to prevent branch breakage and stress.'
    },

    # PEPPER
    'Pepper,_bell___Bacterial_spot': {
        'organic': 'Apply copper-based liquid bactericide sprays every 7 to 10 days.',
        'chemical': 'Mix copper fungicides with Mancozeb to increase control efficacy against resistant strains.',
        'prevention': 'Purchase certified disease-free seeds and avoid working among wet foliage.'
    },
    'Pepper,_bell___healthy': {
        'organic': 'Feed regularly with fish emulsion or seaweed extract solutions.',
        'chemical': 'No chemical applications required.',
        'prevention': 'Use stakes or cages to support pepper plants and prevent fruit ground contact.'
    },

    # POTATO
    'Potato___Early_blight': {
        'organic': 'Apply copper hydroxide liquid sprays immediately when lower leaf spots emerge.',
        'chemical': 'Treat fields with Chlorothalonil or Mancozeb protectant chemical sprays.',
        'prevention': 'Water at the base of the plant using drip tape to keep foliage completely dry.'
    },
    'Potato___Late_blight': {
        'organic': 'Highly destructive; no organic cure once active. Destroy the crop immediately.',
        'chemical': 'Apply preventative specialized anti-blight fungicides containing Mefenoxam.',
        'prevention': 'Plant certified disease-free seed tubers and eliminate all volunteer potato plants.'
    },
    'Potato___healthy': {
        'organic': 'Hill soil around the base of the stems regularly to protect growing tubers.',
        'chemical': 'No chemical treatments required.',
        'prevention': 'Practice a 3-year crop rotation framework excluding tomato and eggplants.'
    },

    # RASPBERRY
    'Raspberry___healthy': {
        'organic': 'Provide a thick layer of organic woodchip mulch to retain root moisture.',
        'chemical': 'No chemical interventions required.',
        'prevention': 'Cut old spent floricanes down to the ground level immediately after summer harvest.'
    },

    # SOYBEAN
    'Soybean___healthy': {
        'organic': 'Incorporate organic green manure covers between seasonal plantings.',
        'chemical': 'No chemical treatments required.',
        'prevention': 'Ensure proper seed planting depth and maintain optimal row drainage configurations.'
    },

    # SQUASH
    'Squash___Powdery_mildew': {
        'organic': 'Spray leaves with dilute milk-water mixes (40:60) or potassium bicarbonate solutions.',
        'chemical': 'Apply systemic triazole or strobilurin fungicides at the first sign of white dust coating.',
        'prevention': 'Space plants generously to enable maximum airflow through dense vine layers.'
    },

    # STRAWBERRY
    'Strawberry___Leaf_scorch': {
        'organic': 'Remove and destroy older infected leaves manually to slow down baseline spread.',
        'chemical': 'Apply protective copper or Captan fungicide arrays during early spring flushes.',
        'prevention': 'Renovate strawberry beds after harvest and avoid excessive spring nitrogen fertilizer.'
    },
    'Strawberry___healthy': {
        'organic': 'Mulch beds cleanly with clean straw to keep berries off bare dirt surfaces.',
        'chemical': 'No chemical treatments required.',
        'prevention': 'Keep runner plants thinned out to avoid overcrowding and root resource competition.'
    },

    # TOMATOES
    'Tomato___Bacterial_spot': {
        'organic': 'Apply organic copper sprays weekly as a preventative protection shield layer.',
        'chemical': 'Apply copper fungicides combined with Mancozeb to counter copper-resistant bacteria.',
        'prevention': 'Prune lower branches to prevent rain-driven soil splash from reaching leaves.'
    },
    'Tomato___Early_blight': {
        'organic': 'Remove infected lower leaves immediately and spray organic copper formulas.',
 'chemical': 'Spray with Chlorothalonil or Daconil fungicides every 10 days during humid spells.','prevention': 'Mulch heavily around the plant base to establish a barrier against soil spores.'},'Tomato___Late_blight': {'organic': 'Highly destructive. Pull up, bag, and discard infected plants instantly to stop spore clouds.','chemical': 'Apply aggressive protectant treatments containing Mefenoxam or Chlorothalonil.','prevention': 'Avoid overhead watering systems completely and ensure wide plant canopy spacing.'},'Tomato___Leaf_Mold': {'organic': 'Spray with potassium bicarbonate solutions to alter leaf surface pH chemistry.','chemical': 'Apply specialized broad-spectrum fungicides if greenhouse humidity breaks threshold targets.','prevention': 'Grow tomatoes in highly ventilated structures and keep relative humidity below 85%.'},'Tomato___Septoria_leaf_spot': {'organic': 'Remove infected foliage at the base and spray bio-fungicides containing Bacillus subtilis.','chemical': 'Apply protective multi-site fungicides containing Chlorothalonil or Mancozeb.','prevention': 'Practice a strict 3-year crop rotation and sanitize all tomato cages with bleach.'},'Tomato___Spider_mites_Two-spotted_spider_mite': {'organic': 'Release predatory mites or spray leaves thoroughly with organic neem oil solutions.','chemical': 'Apply targeted agricultural miticides/acaricides containing Abamectin.','prevention': 'Keep plants well-hydrated; spider mite colonies expand rapidly in dry, dusty zones.'},'Tomato___Target_Spot': {'organic': 'Prune lower suckers to boost ventilation and apply copper octanoate sprays.','chemical': 'Apply professional-grade azoxystrobin or pyraclostrobin chemical applications.','prevention': 'Eradicate all solanaceous weeds near the patch field perimeter boundaries.'},'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {'organic': 'Cover young nursery seedlings using fine mesh cloth to block whitefly insects.','chemical': 'Viruses cannot be cured chemically. Target the whitefly vector using Imidacloprid.','prevention': 'Install yellow sticky traps early across the canopy to trap whitefly vectors.'},'Tomato___Tomato_mosaic_virus': {'organic': 'No active organic cure exists. Uproot and burn the entire plant crop instantly.','chemical': 'Viruses have no chemical treatments. Sterilize all tools using non-fat dry milk solutions.','prevention': 'Wash hands thoroughly with soap before handling crops, especially if you use tobacco.'},'Tomato___healthy': {'organic': 'Apply balanced organic worm castings or compost tea inputs regularly.','chemical': 'No chemical applications required.','prevention': 'Prune lower leaves up to 30cm off the ground to establish excellent base ventilation.'}}