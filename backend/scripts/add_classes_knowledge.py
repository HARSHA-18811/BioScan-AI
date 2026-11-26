import sys
from pathlib import Path

NEW_ENTRIES = '''
    # ------------------ NEEM ------------------
    "Neem___healthy": {
        "plant": "Neem",
        "leaf_name": "Neem Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Vibrant emerald green curved serrated leaflets, intact cuticle rich in bitter azadirachtin, free from fungal spots or insect galling.",
        "pathology": "Healthy photosynthetic parenchyma tissue exhibiting natural biological resistance to common insects and foliar pathogens.",
        "treatment_organic": "Ensure deep, infrequent watering. Neem thrives in well-drained soils and requires minimal organic fertilizing once established.",
        "treatment_chemical": "No chemical treatment required. Neem naturally synthesizes potent insecticidal triterpenoids.",
        "prevention_guide": [
            "Plant in full sun with excellent drainage; avoid standing water around the root zone.",
            "Prune lower or crowded branches annually to promote canopy airflow."
        ],
        "immediate_actions": [
            "Maintain baseline soil moisture."
        ]
    },
    "Neem___Leaf_spot": {
        "plant": "Neem",
        "leaf_name": "Neem Leaf",
        "condition": "Leaf Spot",
        "pathogen_type": "Fungal",
        "causal_agent": "Pseudocercospora subsessilis (Fungus)",
        "is_healthy": False,
        "symptoms": "Circular to angular dark brown-gray spots with yellow chlorotic rings on serrated leaflets, causing premature foliar defoliation.",
        "pathology": "Fungal spores infect leaf stomata during prolonged wet rainy seasons, colonizing the mesophyll and disrupting photosynthesis.",
        "treatment_organic": "Apply 1% Bordeaux mixture or copper hydroxide spray. Collect and burn fallen defoliated leaves to eliminate overwintering inoculum.",
        "treatment_chemical": "Apply Carbendazim or Mancozeb foliar spray at 2 g/liter at the onset of monsoon spot symptoms.",
        "prevention_guide": [
            "Thin inner canopy shoots to accelerate foliar drying after heavy rains.",
            "Avoid overhead irrigation."
        ],
        "immediate_actions": [
            "Rake and destroy infected fallen leaflets beneath the tree canopy."
        ]
    },

    # ------------------ TULSI ------------------
    "Tulsi___healthy": {
        "plant": "Tulsi",
        "leaf_name": "Tulsi (Holy Basil) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Aromatic ovate green leaves with intact glandular trichomes producing eugenol fragrance; no spotting, powdery film, or leaf curl.",
        "pathology": "Active cellular metabolism with optimal essential oil synthesis in leaf epidermal glands.",
        "treatment_organic": "Provide 4-6 hours of morning sunlight. Water at base when topsoil feels dry. Top-dress with vermicompost monthly.",
        "treatment_chemical": "No chemical fungicides recommended for medicinal Tulsi foliage.",
        "prevention_guide": [
            "Pinch growing tips periodically to encourage bushy vegetative branching.",
            "Do not overwater; ensure container or bed has drainage holes."
        ],
        "immediate_actions": [
            "Maintain moderate soil moisture and full morning sunlight."
        ]
    },
    "Tulsi___Powdery_mildew": {
        "plant": "Tulsi",
        "leaf_name": "Tulsi (Holy Basil) Leaf",
        "condition": "Powdery Mildew",
        "pathogen_type": "Fungal",
        "causal_agent": "Oidium basilicum (Fungus)",
        "is_healthy": False,
        "symptoms": "White powdery talcum-like superficial fungal growth across upper leaf lamina, accompanied by chlorosis and leaf distortion.",
        "pathology": "Obligate biotrophic fungus penetrates epidermal cells with haustoria, draining leaf carbohydrates and reducing essential oil yield.",
        "treatment_organic": "Spray milk-water solution (1:9 ratio) or potassium bicarbonate (3 g/liter) in morning sunlight. Remove severely affected leaves.",
        "treatment_chemical": "Apply wettable sulfur spray (safe waiting period must be observed before consuming leaves).",
        "prevention_guide": [
            "Avoid dense crowded planting; allow ample airflow around Tulsi plants.",
            "Water strictly at root level without wetting foliage."
        ],
        "immediate_actions": [
            "Isolate affected Tulsi pot and gently wipe leaves with dilute neem oil emulsion."
        ]
    },

    # ------------------ PAPAYA ------------------
    "Papaya___healthy": {
        "plant": "Papaya",
        "leaf_name": "Papaya Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Expansive, deeply palmately 7-lobed dark green blade with prominent cream-colored radiating veins; intact petioles with no mosaic.",
        "pathology": "Vigorous photosynthetic activity supporting rapid tropical vegetative stem growth and fruit set.",
        "treatment_organic": "Apply well-rotted cow manure around canopy drip line every 2 months. Water consistently without allowing waterlogging.",
        "treatment_chemical": "No chemical treatment required. Maintain balanced nitrogen-phosphorus-potassium (NPK) nutrition.",
        "prevention_guide": [
            "Plant on raised mounds to prevent crown and collar rot.",
            "Scout regularly for aphid and whitefly vectors."
        ],
        "immediate_actions": [
            "Maintain steady drip irrigation."
        ]
    },
    "Papaya___Leaf_curl": {
        "plant": "Papaya",
        "leaf_name": "Papaya Leaf",
        "condition": "Leaf Curl",
        "pathogen_type": "Viral",
        "causal_agent": "Papaya Leaf Curl Virus (PaLCuV, Begomovirus)",
        "is_healthy": False,
        "symptoms": "Severe downward rolling and puckering of young leaves; thickened veins, enations, stunted distorted foliage, and brittle leathery lamina.",
        "pathology": "Whitefly-transmitted Begomovirus (Bemisia tabaci) causes cellular hyperplasia in vascular bundles, severely disrupting phloem translocation.",
        "treatment_organic": "Eradicate whitefly vectors using yellow sticky traps and 2% cold-pressed neem oil spray (3 ml/liter) mixed with bio-soap.",
        "treatment_chemical": "Apply systemic vector insecticides like Imidacloprid (0.3 ml/L) or Acetamiprid to suppress vector populations (virus itself cannot be cured chemically).",
        "prevention_guide": [
            "Install insect-proof nylon netting over young nursery seedlings.",
            "Rogue and immediately burn severely infected plants to prevent field-wide vector spread."
        ],
        "immediate_actions": [
            "Spray vector control immediately to prevent transmission to neighboring healthy papaya plants."
        ]
    },

    # ------------------ COTTON ------------------
    "Cotton___healthy": {
        "plant": "Cotton",
        "leaf_name": "Cotton Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Broad 3-to-5 lobed palmate leaves with healthy dark green hue and smooth laminar surface; free of angular water-soaking.",
        "pathology": "Uninhibited foliar transpiration and photosynthetic assimilation supporting squaring and boll development.",
        "treatment_organic": "Apply vermicompost and foliar seaweed extract to promote robust vegetative branching.",
        "treatment_chemical": "No chemical intervention needed. Ensure balanced potash fertilization.",
        "prevention_guide": [
            "Follow recommended inter-row spacing (90 cm x 60 cm) for optimal aeration.",
            "Maintain weed-free field boundaries."
        ],
        "immediate_actions": [
            "Continue weekly pest scouting."
        ]
    },
    "Cotton___Bacterial_blight": {
        "plant": "Cotton",
        "leaf_name": "Cotton Leaf",
        "condition": "Bacterial Blight (Angular Leaf Spot)",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas citri pv. malvacearum (Bacteria)",
        "is_healthy": False,
        "symptoms": "Angular, water-soaked translucent lesions bounded by leaf veinlets; lesions turn reddish-brown to dark black, progressing along primary veins.",
        "pathology": "Bacterial pathogen penetrates open stomata during warm rainy weather, causing enzymatic dissolution of cell walls and black arm symptoms.",
        "treatment_organic": "Spray copper oxychloride (3 g/L) combined with plant-derived bio-enhancers.",
        "treatment_chemical": "Apply Streptocycline (100 ppm) combined with Copper Oxychloride (0.3%) at 10-14 day intervals.",
        "prevention_guide": [
            "Use acid-delinted and certified disease-free cotton seeds.",
            "Rotate cotton crops with maize or sorghum."
        ],
        "immediate_actions": [
            "Apply copper-streptocycline bactericidal spray at first appearance of angular spots."
        ]
    },

    # ------------------ SUGARCANE ------------------
    "Sugarcane___healthy": {
        "plant": "Sugarcane",
        "leaf_name": "Sugarcane Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Long strap-like linear leaves with sharp serrulate margins and prominent pale central midrib; zero red discoloration.",
        "pathology": "Efficient C4 carbon fixation pathway supporting high sucrose accumulation in internodal stalks.",
        "treatment_organic": "Mulch furrows with sugarcane trash to conserve soil moisture and nourish earthworm activity.",
        "treatment_chemical": "No fungicide required. Apply recommended urea/potash split doses.",
        "prevention_guide": [
            "Select healthy 3-budded setts from pest-free seed nurseries.",
            "Ensure furrow drainage during rainy seasons."
        ],
        "immediate_actions": [
            "Maintain timely field weeding and earthing up."
        ]
    },
    "Sugarcane___Red_rot": {
        "plant": "Sugarcane",
        "leaf_name": "Sugarcane Leaf",
        "condition": "Red Rot",
        "pathogen_type": "Fungal",
        "causal_agent": "Colletotrichum falcatum (Fungus)",
        "is_healthy": False,
        "symptoms": "Third or fourth leaf from crown shows yellowing and withering; midrib exhibits dark blood-red lesions with crosswise white patches.",
        "pathology": "Devastating vascular fungus penetrates stalk vascular bundles, converting sucrose into glucose and producing alcohol odor.",
        "treatment_organic": "Drench soil with Trichoderma harzianum or Trichoderma viride biofungicide formulation.",
        "treatment_chemical": "Dip planting setts in Carbendazim (0.1%) solution before planting; foliar systemic fungicides have limited efficacy once systemic.",
        "prevention_guide": [
            "Plant red-rot resistant sugarcane varieties (e.g. Co 0238, Co 86032).",
            "Uproot and burn diseased clumps immediately; do not take ratoon from infected fields."
        ],
        "immediate_actions": [
            "Rogue infected clumps from roots and burn to prevent irrigation-water transmission."
        ]
    },

    # ------------------ TEA ------------------
    "Tea___healthy": {
        "plant": "Tea",
        "leaf_name": "Tea Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Glossy vibrant green young two-leaves-and-a-bud flush; firm texture with distinct serrated margins and zero blistering.",
        "pathology": "Abundant catechin and polyphenolic synthesis supporting premium tea liquor quality.",
        "treatment_organic": "Apply vermicompost and compost tea to tea bush roots; maintain shade trees (Albizia) for filtered light.",
        "treatment_chemical": "No chemical treatment required.",
        "prevention_guide": [
            "Maintain regular 7-10 day plucking rounds to harvest tender flush.",
            "Prune bushes periodically for light penetration."
        ],
        "immediate_actions": [
            "Follow standard estate plucking schedule."
        ]
    },

    # ------------------ COFFEE ------------------
    "Coffee___healthy": {
        "plant": "Coffee",
        "leaf_name": "Coffee Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Dark waxy green opposite elliptic leaves with prominent wavy undulating margins and glossy cuticle.",
        "pathology": "Healthy palisade parenchyma active in caffeine and chlorogenic acid biosignaling.",
        "treatment_organic": "Mulch coffee basin with leaf litter; apply bio-fertilizer consortia around drip line.",
        "treatment_chemical": "No chemical fungicide required.",
        "prevention_guide": [
            "Regulate shade tree canopy to provide 40-50% dappled sunlight.",
            "Prune dead and crisscross branches before blossom showers."
        ],
        "immediate_actions": [
            "Monitor lower leaf surfaces for incipient rust pustules."
        ]
    },
    "Coffee___Leaf_rust": {
        "plant": "Coffee",
        "leaf_name": "Coffee Leaf",
        "condition": "Leaf Rust",
        "pathogen_type": "Fungal",
        "causal_agent": "Hemileia vastatrix (Fungus)",
        "is_healthy": False,
        "symptoms": "Bright yellow-orange powdery pustules on underside of leaves; corresponding chlorotic spots on upper surface, leading to severe leaf drop.",
        "pathology": "Airborne and rain-splashed urediniospores infect lower stomata, depleting chlorophyll and causing massive defoliation and branch dieback.",
        "treatment_organic": "Apply 0.5% neutral Bordeaux mixture before monsoon and post-monsoon showers.",
        "treatment_chemical": "Apply systemic triazole fungicide like Triadimefon (0.05%) or Hexaconazole at early infection stage.",
        "prevention_guide": [
            "Plant rust-resistant coffee cultivars (e.g. S.795, Cauvery/Catimor).",
            "Maintain optimal shade management to reduce leaf-wetness duration."
        ],
        "immediate_actions": [
            "Spray Bordeaux mixture on undersides of leaves immediately."
        ]
    },

    # ------------------ BRINJAL ------------------
    "Brinjal___healthy": {
        "plant": "Brinjal",
        "leaf_name": "Brinjal (Eggplant) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Expansive broad lobed velvety leaves with fine stellate hairs; healthy green color with zero wilting or yellowing.",
        "pathology": "Robust turgor pressure maintained through vascular xylem supporting heavy flower and fruit set.",
        "treatment_organic": "Apply neem cake at 250 kg/hectare during land prep; foliar spray with fermented butter-milk.",
        "treatment_chemical": "No chemical intervention needed.",
        "prevention_guide": [
            "Avoid planting after other solanaceous crops (potato, tomato, pepper).",
            "Maintain uniform bed moisture."
        ],
        "immediate_actions": [
            "Scout for early leafhopper and shoot borer presence."
        ]
    },

    # ------------------ POMEGRANATE ------------------
    "Pomegranate___healthy": {
        "plant": "Pomegranate",
        "leaf_name": "Pomegranate Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Small, glossy oblong leaves with entire smooth margins and bright green luster; free of nodal blackening.",
        "pathology": "Intact leaf epidermis with active transpiration and sugar accumulation for fruit enlargement.",
        "treatment_organic": "Foliar spray with cow-dung urine slurry extract or organic humic acids.",
        "treatment_chemical": "No chemical spray needed.",
        "prevention_guide": [
            "Prune inside water shoots to maintain open bowl-shaped center.",
            "Disinfect pruning shears with 70% ethanol between trees."
        ],
        "immediate_actions": [
            "Ensure drip emitters are working uniformly."
        ]
    },

    # ------------------ MINT ------------------
    "Mint___healthy": {
        "plant": "Mint",
        "leaf_name": "Mint (Pudina) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Crisp ovate to lanceolate serrated bright green leaves rich in aromatic menthol; zero brown pustules.",
        "pathology": "Active glandular trichomes producing high concentration of monoterpenes.",
        "treatment_organic": "Water frequently to keep soil moist; harvest stems regularly to promote dense tender growth.",
        "treatment_chemical": "No chemicals recommended for culinary herbs.",
        "prevention_guide": [
            "Plant in container or confined bed to prevent invasive root spread.",
            "Water at soil line to keep leaves dry."
        ],
        "immediate_actions": [
            "Pinch tops regularly."
        ]
    },

    # ------------------ HIBISCUS ------------------
    "Hibiscus___healthy": {
        "plant": "Hibiscus",
        "leaf_name": "Hibiscus Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Glossy dark green ovate leaves with serrated margins, free of mealybug sooty mold or chlorotic spotting.",
        "pathology": "Active palisade tissue driving abundant flower bud differentiation.",
        "treatment_organic": "Spray dilute neem oil spray monthly to deter mealybugs and aphids.",
        "treatment_chemical": "No chemical spray required.",
        "prevention_guide": [
            "Place in full sunlight (at least 6 hours daily).",
            "Prune older leggy canes in spring."
        ],
        "immediate_actions": [
            "Check leaf axils for sap-sucking pests."
        ]
    },

    # ------------------ MORINGA ------------------
    "Moringa___healthy": {
        "plant": "Moringa",
        "leaf_name": "Moringa (Drumstick) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Delicate tripinnate compound foliage with hundreds of small obovate green leaflets; rich in vitamins and protein.",
        "pathology": "High nitrogen fixation efficiency and drought-tolerant cellular water conservation.",
        "treatment_organic": "Add organic compost around base once a year; pinch central leader to encourage harvestable bushy branching.",
        "treatment_chemical": "No chemical application needed.",
        "prevention_guide": [
            "Never allow water to stand at root collar; moringa is sensitive to root rot.",
            "Harvest compound leaves regularly."
        ],
        "immediate_actions": [
            "Ensure well-drained sandy loam soil."
        ]
    },

    # ------------------ WATERMELON ------------------
    "Watermelon___healthy": {
        "plant": "Watermelon",
        "leaf_name": "Watermelon Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Deeply sinuate-lobed sand-textured leaves with healthy green hue and vigorous branching runners.",
        "pathology": "Extensive photosynthetic leaf area supplying high fructose and water volume to swelling melons.",
        "treatment_organic": "Mulch soil with black plastic or straw; use drip irrigation to prevent foliar contact with wet soil.",
        "treatment_chemical": "No fungicide required.",
        "prevention_guide": [
            "Rotate with non-cucurbit crops for at least 3 years.",
            "Scout for cucumber beetles and aphids."
        ],
        "immediate_actions": [
            "Maintain drip irrigation under mulch."
        ]
    },

    # ------------------ BANYAN ------------------
    "Banyan___healthy": {
        "plant": "Banyan",
        "leaf_name": "Banyan Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Thick, leathery, glossy oval leaves with prominent lateral pale veins and milky white latex inside petiole.",
        "pathology": "Durable multi-layered epidermis designed for high irradiance and decades of canopy longevity.",
        "treatment_organic": "Virtually indestructible once established; requires zero fertilizer in native soils.",
        "treatment_chemical": "No chemical treatment required.",
        "prevention_guide": [
            "Provide vast space for prop roots to establish.",
            "Protect from severe frosts when young."
        ],
        "immediate_actions": [
            "Normal tree growth."
        ]
    },

    # ------------------ ASHOKA ------------------
    "Ashoka___healthy": {
        "plant": "Ashoka",
        "leaf_name": "Ashoka Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Long, narrow, weeping lanceolate dark green leaves with wavy undulating edges, hanging gracefully along upright branches.",
        "pathology": "Dense column of evergreen foliage acting as natural urban acoustic barrier and windbreak.",
        "treatment_organic": "Apply organic leaf mold around tree base annually.",
        "treatment_chemical": "No chemical intervention needed.",
        "prevention_guide": [
            "Plant at 4-5 feet intervals for screening hedges.",
            "Prune side branches only if shaping is needed."
        ],
        "immediate_actions": [
            "Maintain baseline watering."
        ]
    },

    # ------------------ BAMBOO ------------------
    "Bamboo___healthy": {
        "plant": "Bamboo",
        "leaf_name": "Bamboo Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Slender linear-lanceolate green blades with parallel venation and silica-hardened serrulate margins.",
        "pathology": "Extremely fast carbon sequestration and silica deposition in leaf epidermal phytoliths.",
        "treatment_organic": "Mulch bamboo grove with fallen bamboo leaves to recycle natural silica and organic matter.",
        "treatment_chemical": "No chemical fungicides required.",
        "prevention_guide": [
            "Thin out older culms (stems) every 3-4 years.",
            "Install root barrier if planting running bamboo varieties."
        ],
        "immediate_actions": [
            "Ensure regular irrigation during shoot emergence."
        ]
    },

    # ------------------ COCONUT ------------------
    "Coconut___healthy": {
        "plant": "Coconut",
        "leaf_name": "Coconut Palm Frond Leaflet",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Rigid, deep green linear-lanceolate leaflets with a stiff central keel, free of yellow bronzing or leaf spots.",
        "pathology": "Heavy cuticular wax layers enabling tolerance to high salinity, maritime winds, and intense UV radiation.",
        "treatment_organic": "Apply 50 kg farmyard manure and 1 kg neem cake per palm annually in a 1.8m ring basin.",
        "treatment_chemical": "Apply muriate of potash and borax according to soil fertility test recommendations.",
        "prevention_guide": [
            "Maintain root basin mulching with coconut husks to conserve moisture.",
            "Install pheromone traps for rhinoceros beetle control."
        ],
        "immediate_actions": [
            "Ensure regular summer basin irrigation."
        ]
    }
'''

target_path = Path("backend/app/services/plant_knowledge.py")
content = target_path.read_text(encoding="utf-8")

target = "    }\n}\n\ndef parse_class_name"
replacement = "    }," + NEW_ENTRIES + "}\n\ndef parse_class_name"

if target in content:
    content = content.replace(target, replacement, 1)
    target_path.write_text(content, encoding="utf-8")
    print("Successfully added new plants to CLASS_KNOWLEDGE_BASE!")
else:
    print("Error: Target pattern not found!")
