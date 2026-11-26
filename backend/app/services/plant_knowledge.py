"""
Plant Biology, Pathology & Treatment Knowledge Base for BioScan AI.
Provides expert botanical metadata, pathogen etiology, and actionable treatment solutions.
Includes extended crop profiles for Carrot, Strawberry, Banana, Cucumber, Rose, Guava,
Cabbage, Onion, Rice, Wheat, Mango, Citrus, Pepper, Apple, Corn, Grape, Potato, and Tomato.
"""

from typing import Dict, Any, List

PLANT_SPECIES_INFO = {
    "Apple": {
        "leaf_name": "Apple Leaf",
        "scientific_name": "Malus domestica",
        "family": "Rosaceae",
        "biology_notes": "Deciduous fruit tree. Foliar diseases directly degrade photosynthetic canopy, causing premature leaf drop and reducing apple yield."
    },
    "Corn": {
        "leaf_name": "Corn (Maize) Leaf",
        "scientific_name": "Zea mays",
        "family": "Poaceae",
        "biology_notes": "Vital monocot cereal crop. Foliar rusts and blights compromise photosynthetic leaf area, reducing grain-fill capacity and ear size."
    },
    "Grape": {
        "leaf_name": "Grape Leaf",
        "scientific_name": "Vitis vinifera",
        "family": "Vitaceae",
        "biology_notes": "Perennial climbing woody vine. Foliar fungal infections lead to widespread defoliation, sunburn on fruit, and reduced brix/sugar accumulation."
    },
    "Mango": {
        "leaf_name": "Mango Leaf",
        "scientific_name": "Mangifera indica",
        "family": "Anacardiaceae",
        "biology_notes": "Tropical evergreen fruit tree. Thick glossy lanceolate leaves with robust waxy cuticles that support dense flowering panicles and high fruit yields."
    },
    "Potato": {
        "leaf_name": "Potato Leaf",
        "scientific_name": "Solanum tuberosum",
        "family": "Solanaceae",
        "biology_notes": "Starchy tuber crop. Foliar blights attack leaves and stems, destroying foliage and transferring spores into developing underground tubers."
    },
    "Tomato": {
        "leaf_name": "Tomato Leaf",
        "scientific_name": "Solanum lycopersicum",
        "family": "Solanaceae",
        "biology_notes": "Warm-season fruiting vegetable. High susceptibility to foliar fungal and bacterial pathogens that cause rapid leaf defoliation and fruit spotting."
    },
    "Citrus": {
        "leaf_name": "Citrus / Lemon Leaf",
        "scientific_name": "Citrus limon / sinensis",
        "family": "Rutaceae",
        "biology_notes": "Subtropical evergreen citrus tree. Leaves feature winged petioles and rich essential oil glands; susceptible to bacterial canker and greasy spot."
    },
    "Pepper": {
        "leaf_name": "Bell Pepper Leaf",
        "scientific_name": "Capsicum annuum",
        "family": "Solanaceae",
        "biology_notes": "Warm-season solanaceous vegetable. Smooth elliptical leaves vulnerable to bacterial spot and viral mottling."
    },
    "Carrot": {
        "leaf_name": "Carrot Leaf",
        "scientific_name": "Daucus carota subsp. sativus",
        "family": "Apiaceae (Umbelliferae)",
        "biology_notes": "Biennial root crop with delicate, 2-3 pinnately dissected feathery lace-like foliage. The feathery photosynthetic canopy drives sucrose storage into the taproot."
    },
    "Strawberry": {
        "leaf_name": "Strawberry Leaf",
        "scientific_name": "Fragaria × ananassa",
        "family": "Rosaceae",
        "biology_notes": "Perennial stoloniferous fruit crop. Leaves are trifoliate with coarsely serrated margins; vulnerable to fungal scorch and angular leaf spot."
    },
    "Banana": {
        "leaf_name": "Banana Leaf",
        "scientific_name": "Musa acuminata",
        "family": "Musaceae",
        "biology_notes": "Large tropical monocot herb. Giant oblong paddle leaves with massive surface area vulnerable to airborne Mycosphaerella black sigatoka spores."
    },
    "Cucumber": {
        "leaf_name": "Cucumber Leaf",
        "scientific_name": "Cucumis sativus",
        "family": "Cucurbitaceae",
        "biology_notes": "Vining cucurbit crop with broad triangular palmate-lobed leaves covered in rough trichomes; highly susceptible to powdery and downy mildews."
    },
    "Rose": {
        "leaf_name": "Rose Leaf",
        "scientific_name": "Rosa hybrida",
        "family": "Rosaceae",
        "biology_notes": "Woody perennial flowering shrub. Odd-pinnate compound leaves with serrated margins prone to Diplocarpon rosae fungal black spot."
    },
    "Guava": {
        "leaf_name": "Guava Leaf",
        "scientific_name": "Psidium guajava",
        "family": "Myrtaceae",
        "biology_notes": "Tropical fruit tree with opposite, oblong-elliptic leathery leaves with prominent parallel veins and aromatic essential oils."
    },
    "Cabbage": {
        "leaf_name": "Cabbage Leaf",
        "scientific_name": "Brassica oleracea",
        "family": "Brassicaceae",
        "biology_notes": "Cruciferous vegetable with broad rounded waxy glaucous leaves prone to Xanthomonas campestris bacterial black rot."
    },
    "Onion": {
        "leaf_name": "Onion Leaf",
        "scientific_name": "Allium cepa",
        "family": "Amaryllidaceae",
        "biology_notes": "Bulbous crop with tubular hollow cylindrical foliage (fistular leaves) vulnerable to Alternaria porri purple blotch."
    },
    "Rice": {
        "leaf_name": "Rice (Paddy) Leaf",
        "scientific_name": "Oryza sativa",
        "family": "Poaceae",
        "biology_notes": "Cereal grain grass with flat linear blade and parallel veins; critical food security crop vulnerable to Bipolaris oryzae fungal brown spot."
    },
    "Wheat": {
        "leaf_name": "Wheat Leaf",
        "scientific_name": "Triticum aestivum",
        "family": "Poaceae",
        "biology_notes": "Major temperate cereal crop. Long linear photosynthetic flag leaves highly vulnerable to Puccinia triticina airborne leaf rust spores."
    },
    "Neem": {
        "leaf_name": "Neem Leaf",
        "scientific_name": "Azadirachta indica",
        "family": "Meliaceae",
        "biology_notes": "Valued medicinal tree native to the Indian subcontinent. Pinnate compound leaves with curved serrated leaflets containing azadirachtin."
    },
    "Tulsi": {
        "leaf_name": "Tulsi (Holy Basil) Leaf",
        "scientific_name": "Ocimum tenuiflorum",
        "family": "Lamiaceae",
        "biology_notes": "Aromatic sacred medicinal herb. Opposite ovate green or purple-tinted leaves rich in eugenol and essential volatile terpenes."
    },
    "Papaya": {
        "leaf_name": "Papaya Leaf",
        "scientific_name": "Carica papaya",
        "family": "Caricaceae",
        "biology_notes": "Tropical herbaceous fruit crop. Large palmately 7-9 lobed leaves with long hollow petioles vulnerable to Papaya ringspot potyvirus."
    },
    "Cotton": {
        "leaf_name": "Cotton Leaf",
        "scientific_name": "Gossypium hirsutum",
        "family": "Malvaceae",
        "biology_notes": "Major fiber cash crop. Broad 3-5 lobed palmate leaves susceptible to Xanthomonas malvacearum bacterial angular leaf spot."
    },
    "Sugarcane": {
        "leaf_name": "Sugarcane Leaf",
        "scientific_name": "Saccharum officinarum",
        "family": "Poaceae",
        "biology_notes": "Tall tropical perennial grass. Long linear strap blades with sharp serrulate margins and white midrib vulnerable to Colletotrichum falcatum red rot."
    },
    "Tea": {
        "leaf_name": "Tea Leaf",
        "scientific_name": "Camellia sinensis",
        "family": "Theaceae",
        "biology_notes": "Perennial evergreen plantation shrub. Glossy elliptic to lanceolate serrated leaves prone to Exobasidium vexans blister blight."
    },
    "Coffee": {
        "leaf_name": "Coffee Leaf",
        "scientific_name": "Coffea arabica",
        "family": "Rubiaceae",
        "biology_notes": "Understory tropical shrub. Dark glossy green opposite oval blades with wavy margins highly vulnerable to Hemileia vastatrix leaf rust."
    },
    "Brinjal": {
        "leaf_name": "Brinjal (Eggplant) Leaf",
        "scientific_name": "Solanum melongena",
        "family": "Solanaceae",
        "biology_notes": "Warm-season solanaceous vegetable with broad, coarsely lobed fuzzy pubescent leaves vulnerable to Ralstonia solanacearum bacterial wilt."
    },
    "Pomegranate": {
        "leaf_name": "Pomegranate Leaf",
        "scientific_name": "Punica granatum",
        "family": "Lythraceae",
        "biology_notes": "Deciduous fruit shrub. Narrow glossy oblong-lanceolate leaves with entire margins vulnerable to Xanthomonas axonopodis bacterial blight."
    },
    "Mint": {
        "leaf_name": "Mint (Pudina) Leaf",
        "scientific_name": "Mentha spicata",
        "family": "Lamiaceae",
        "biology_notes": "Fast-spreading aromatic perennial herb. Opposite serrated lanceolate leaves producing characteristic menthol essential oils."
    },
    "Hibiscus": {
        "leaf_name": "Hibiscus Leaf",
        "scientific_name": "Hibiscus rosa-sinensis",
        "family": "Malvaceae",
        "biology_notes": "Ornamental tropical flowering shrub with ovate to lanceolate glossy green leaves with serrated to dentate upper margins."
    },
    "Moringa": {
        "leaf_name": "Moringa (Drumstick) Leaf",
        "scientific_name": "Moringa oleifera",
        "family": "Moringaceae",
        "biology_notes": "Drought-resistant nutrient-dense fast-growing tree. Tripinnate compound leaves bearing hundreds of delicate small obovate leaflets."
    },
    "Ginger": {
        "leaf_name": "Ginger Leaf",
        "scientific_name": "Zingiber officinale",
        "family": "Zingiberaceae",
        "biology_notes": "Tropical herbaceous perennial with narrow linear-lanceolate sheathing leaves with distinct aromatic underground rhizomes."
    },
    "Soybean": {
        "leaf_name": "Soybean Leaf",
        "scientific_name": "Glycine max",
        "family": "Fabaceae",
        "biology_notes": "Major oilseed and protein legume crop. Trifoliate compound leaves with ovate leaflets susceptible to Phakopsora pachyrhizi Asian rust."
    },
    "Watermelon": {
        "leaf_name": "Watermelon Leaf",
        "scientific_name": "Citrullus lanatus",
        "family": "Cucurbitaceae",
        "biology_notes": "Vining cucurbit fruit crop with deeply pinnatifid, sinuate-lobed sand-textured leaves vulnerable to Colletotrichum orbiculare anthracnose."
    },
    "Banyan": {
        "leaf_name": "Banyan Leaf",
        "scientific_name": "Ficus benghalensis",
        "family": "Moraceae",
        "biology_notes": "Vast national canopy tree of India. Leathery glossy ovate-elliptic leaves with prominent pale lateral veins and milky latex."
    },
    "Ashoka": {
        "leaf_name": "Ashoka Leaf",
        "scientific_name": "Polyalthia longifolia",
        "family": "Annonaceae",
        "biology_notes": "Evergreen ornamental mast tree. Long pendulous lanceolate glossy dark green leaves with wavy sinusoidal margins."
    },
    "Eucalyptus": {
        "leaf_name": "Eucalyptus Leaf",
        "scientific_name": "Eucalyptus globulus",
        "family": "Myrtaceae",
        "biology_notes": "Fast-growing aromatic hardwood tree. Sickle-shaped (falcate) pendulous leathery blue-green leaves rich in cineole essential oil."
    },
    "Bamboo": {
        "leaf_name": "Bamboo Leaf",
        "scientific_name": "Bambusa vulgaris",
        "family": "Poaceae",
        "biology_notes": "Arborescent giant woody grass. Linear-lanceolate blades with parallel venation and silica-reinforced rough margins."
    },
    "Coconut": {
        "leaf_name": "Coconut Palm Frond Leaflet",
        "scientific_name": "Cocos nucifera",
        "family": "Arecaceae",
        "biology_notes": "Tropical perennial palm tree. Huge pinnate fronds composed of dozens of linear-lanceolate rigid leathery leaflets."
    },
    "Money_Plant": {
        "leaf_name": "Money Plant (Golden Pothos) Leaf",
        "scientific_name": "Epipremnum aureum",
        "family": "Araceae",
        "biology_notes": "Ubiquitous tropical evergreen indoor vining climber. Distinctive glossy cordate (heart-shaped) waxy leaves with acute tips and smooth entire margins, often displaying golden variegation."
    },
    "Curry_Leaf": {
        "leaf_name": "Curry Leaf (Kadi Patta)",
        "scientific_name": "Murraya koenigii",
        "family": "Rutaceae",
        "biology_notes": "Aromatic subtropical culinary small tree. Pinnate compound leaves with 11-25 asymmetric ovate leaflets producing distinct culinary essential oils."
    }
}

CLASS_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    # ------------------ CARROT ------------------
    "Carrot___Alternaria_leaf_blight": {
        "plant": "Carrot",
        "leaf_name": "Carrot Leaf",
        "condition": "Alternaria Leaf Blight",
        "pathogen_type": "Fungal",
        "causal_agent": "Alternaria dauci (Fungus)",
        "is_healthy": False,
        "symptoms": "Dark brown-to-black necrotic spots with bright yellow chlorotic halos on feathery leaflet margins; tips curl, turn brown, and appear scorched.",
        "pathology": "Airborne and seed-borne fungal pathogen. Spores germinate in free moisture and penetrate feathery leaf tissue, causing rapid necrosis and crown rot.",
        "treatment_organic": "Apply copper hydroxide or Bacillus subtilis biofungicide at first sign of leaf spot. Avoid overhead sprinkler irrigation and use drip lines.",
        "treatment_chemical": "Apply protectant fungicides such as Chlorothalonil or Azoxystrobin every 7-10 days when foliage is dense and weather is warm and humid.",
        "prevention_guide": [
            "Use certified disease-free, hot-water treated carrot seed stock.",
            "Thin carrot seedlings to at least 2-3 inches apart to promote rapid drying of feathery foliage.",
            "Rotate carrot fields with non-umbellifer crops (e.g. corn, beans, brassicas) on a 3-year cycle."
        ],
        "immediate_actions": [
            "Cease overhead irrigation immediately; water strictly at soil level.",
            "Apply protective fungicide coverage to prevent blight from destroying the crown.",
            "Remove and safely burn or discard severely blighted leaf debris."
        ]
    },
    "Carrot___Powdery_mildew": {
        "plant": "Carrot",
        "leaf_name": "Carrot Leaf",
        "condition": "Powdery Mildew",
        "pathogen_type": "Fungal",
        "causal_agent": "Erysiphe heraclei (Fungus)",
        "is_healthy": False,
        "symptoms": "White to grayish powdery fungal patches developing across feathery leaflets and petioles, causing premature foliar yellowing and leaf collapse.",
        "pathology": "Fungal ectoparasite that forms superficial white mycelium on leaf cuticle and extracts nutrients through haustoria, suppressing root enlargement.",
        "treatment_organic": "Spray potassium bicarbonate (3-5 g/L) or cold-pressed neem oil emulsion (0.5%) every 7 days. Sulfur dust can be applied during dry weather.",
        "treatment_chemical": "Apply systemic triazole or strobilurin fungicides (e.g., Myclobutanil, Tebuconazole) at first sign of powdery fungal growth.",
        "prevention_guide": [
            "Plant carrots in full sunlight with adequate row spacing for ventilation.",
            "Avoid excessive nitrogen fertilizer which stimulates overly dense, disease-prone foliage.",
            "Eliminate wild carrot (Queen Anne's lace) growing adjacent to production beds."
        ],
        "immediate_actions": [
            "Apply potassium bicarbonate or biofungicide spray thoroughly over feathery foliage.",
            "Prune heavily infected lower leaves to increase under-canopy airflow."
        ]
    },
    "Carrot___healthy": {
        "plant": "Carrot",
        "leaf_name": "Carrot Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Vibrant, feathery, bright green bipinnate fronds with crisp lace segments and complete absence of necrotic browning or powdery films.",
        "pathology": "Active photosynthetic mesophyll tissue in finely dissected leaflets driving efficient sucrose synthesis and taproot expansion.",
        "treatment_organic": "Maintain consistent soil moisture, mulch lightly with straw to suppress weeds, and apply balanced compost tea monthly.",
        "treatment_chemical": "No fungicide required. Maintain adequate potassium and phosphorus levels in soil for optimal carrot root development.",
        "prevention_guide": [
            "Weed regularly around carrot crowns to prevent competition for light and nutrients.",
            "Water deeply 1-2 times weekly rather than frequent shallow sprinkling.",
            "Scout feathery foliage weekly for early signs of leafhoppers or aphids."
        ],
        "immediate_actions": [
            "Continue standard watering and root-crop maintenance.",
            "Ensure carrot shoulders are covered with soil to avoid greening from direct sunlight."
        ]
    },

    # ------------------ APPLE ------------------
    "Apple___Apple_scab": {
        "plant": "Apple",
        "leaf_name": "Apple Leaf",
        "condition": "Apple Scab",
        "pathogen_type": "Fungal",
        "causal_agent": "Venturia inaequalis (Ascomycete Fungus)",
        "is_healthy": False,
        "symptoms": "Velvety, olive-green to dull dark-brown circular lesions with feathery borders on upper leaf surfaces; leaf puckering and premature defoliation.",
        "pathology": "Overwinters as pseudothecia in dead fallen apple leaves. Spring rain releases ascospores that infect tender young apple foliage.",
        "treatment_organic": "Apply wettable sulfur or liquid lime-sulfur during green tip through bloom. Shred and compost fallen autumn leaves thoroughly.",
        "treatment_chemical": "Apply protective fungicides such as Captan, Mancozeb, or systemic DMI fungicides (Difenoconazole, Myclobutanil).",
        "prevention_guide": [
            "Plant scab-resistant apple cultivars such as Liberty, Enterprise, Freedom, or GoldRush.",
            "Prune tree canopies annually in late winter to maximize sunlight penetration and rapid leaf drying.",
            "Rake and destroy fallen leaves in autumn or apply 5% agricultural urea spray to accelerate leaf breakdown."
        ],
        "immediate_actions": [
            "Spray protective fungicide before predicted rain events during spring vegetative growth.",
            "Prune dense interior water sprouts to improve airflow across canopy.",
            "Keep the ground beneath the tree canopy clean of decaying leaf litter."
        ]
    },
    "Apple___Black_rot": {
        "plant": "Apple",
        "leaf_name": "Apple Leaf",
        "condition": "Black Rot (Frogeye Leaf Spot)",
        "pathogen_type": "Fungal",
        "causal_agent": "Diplodia seriata / Botryosphaeria obtusa (Fungus)",
        "is_healthy": False,
        "symptoms": "Small purple specks enlarging into circular lesions with tan/grey centers and purple-brown margins resembling a 'frogeye'.",
        "pathology": "Fungal inoculum overwinters in dead wood, branch cankers, and mummified fruits left hanging on the tree from previous seasons.",
        "treatment_organic": "Prune out all dead wood, fire blight cankers, and mummified apples hanging from trees. Spray bio-fungicide (Bacillus subtilis) or copper octanoate.",
        "treatment_chemical": "Apply Captan or Thiophanate-methyl sprays beginning at silver tip and repeat every 10-14 days through early summer fruit development.",
        "prevention_guide": [
            "Remove all mummified apples and infected twigs from previous seasons immediately.",
            "Sterilize pruning shears with 70% isopropyl alcohol between every cut.",
            "Maintain tree vigor with balanced organic fertilizer; stressed or wounded trees are most vulnerable."
        ],
        "immediate_actions": [
            "Inspect branches for dark sunken cankers and prune 6-8 inches below affected tissue.",
            "Collect and burn or discard mummified fruit hanging on the tree."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "plant": "Apple",
        "leaf_name": "Apple Leaf",
        "condition": "Cedar Apple Rust",
        "pathogen_type": "Fungal (Heteroecious)",
        "causal_agent": "Gymnosporangium juniperi-virginianae (Rust Fungus)",
        "is_healthy": False,
        "symptoms": "Vibrant yellow-orange circular spots on leaf upper surfaces with dark center pimples; tubular spore cups develop on leaf undersides.",
        "pathology": "Obligate heteroecious rust requiring two alternating hosts: Eastern red cedar (Juniperus virginiana) and apple trees to complete its life cycle.",
        "treatment_organic": "Apply sulfur or copper sprays when orange gelatinous spore horns appear on nearby cedar/juniper trees in early spring.",
        "treatment_chemical": "Spray Myclobutanil (Immunox) or Propiconazole starting when blossom buds show pink and repeat every 7-10 days until petal drop.",
        "prevention_guide": [
            "Eliminate wild eastern red cedar and juniper plants within 1,000 feet of the orchard.",
            "Choose rust-immune apple varieties such as Prima, Priscilla, Liberty, or Redfree."
        ],
        "immediate_actions": [
            "Apply systemic triazole fungicide (e.g. Myclobutanil) to arrest rust lesion expansion.",
            "Inspect adjacent boundaries for juniper galls and remove them."
        ]
    },
    "Apple___healthy": {
        "plant": "Apple",
        "leaf_name": "Apple Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Smooth, vibrant green lamina, crisp finely serrated margins, intact veins, and complete absence of necrotic lesions or scabs.",
        "pathology": "Optimal photosynthetic parenchymal tissue with balanced chlorophyll a/b content and intact protective epidermal cuticle.",
        "treatment_organic": "Maintain regular organic mulch around tree drip line, apply compost tea monthly, and perform bi-weekly scouting.",
        "treatment_chemical": "No fungicide required. Maintain standard micronutrient balance (Zinc, Boron foliar spray if deficient).",
        "prevention_guide": [
            "Ensure deep, infrequent watering at tree base rather than overhead sprinkler watering.",
            "Apply dormant horticultural oil spray in late winter to suppress overwintering insect pests.",
            "Maintain an annual pruning schedule to keep the canopy open to light and airflow."
        ],
        "immediate_actions": [
            "Continue standard watering and seasonal care.",
            "Inspect foliage regularly for early signs of foliar pests or leaf-chewing insects."
        ]
    },

    # ------------------ CORN ------------------
    "Corn___Common_rust": {
        "plant": "Corn (Maize)",
        "leaf_name": "Corn (Maize) Leaf",
        "condition": "Common Rust",
        "pathogen_type": "Fungal",
        "causal_agent": "Puccinia sorghi (Airborne Rust Fungus)",
        "is_healthy": False,
        "symptoms": "Golden-brown to cinnamon-brown powdery pustules (uredinia) scattered on both upper and lower leaf surfaces, erupting through leaf epidermis.",
        "pathology": "Airborne urediniospores travel long distances in air currents. High humidity (>95%) and moderate temperatures (16-25°C) favor rapid sporulation.",
        "treatment_organic": "Dust with wettable sulfur at earliest onset. Spray neem oil or Bacillus amyloliquefaciens biofungicide early morning to protect unaffected upper leaves.",
        "treatment_chemical": "Apply strobilurin or triazole fungicides (such as Azoxystrobin + Propiconazole, or Pyraclostrobin) if pustules appear prior to tasseling.",
        "prevention_guide": [
            "Select certified rust-resistant corn hybrid varieties equipped with dominant Rp resistance genes.",
            "Plant early in the season to mature past peak airborne rust spore migrations.",
            "Rotate corn fields with non-host crops (soybeans, legumes) to disrupt fungal spore cycles."
        ],
        "immediate_actions": [
            "Assess rust severity: if pustules cover >5% of leaves before silking, apply targeted fungicide.",
            "Avoid overhead irrigation during evening hours to reduce leaf wetness duration."
        ]
    },
    "Corn___Northern_Leaf_Blight": {
        "plant": "Corn (Maize)",
        "leaf_name": "Corn (Maize) Leaf",
        "condition": "Northern Corn Leaf Blight",
        "pathogen_type": "Fungal",
        "causal_agent": "Exserohilum turcicum / Setosphaeria turcica (Fungus)",
        "is_healthy": False,
        "symptoms": "Long, elliptical, cigar-shaped grayish-green to tan necrotic lesions (1-6 inches long) running parallel to leaf margins.",
        "pathology": "Inoculum overwinters in corn residue. Spores splash onto lower foliage in moderate temperatures (18-27°C) accompanied by extended dew periods.",
        "treatment_organic": "Spray copper octanoate or Trichoderma harzianum bio-protectants on lower leaves. Incorporate fallen crop residue deeply into soil.",
        "treatment_chemical": "Apply fungicides containing Pyraclostrobin, Azoxystrobin, or Difenoconazole at VT-R1 growth stages if weather is persistently humid.",
        "prevention_guide": [
            "Utilize corn hybrids featuring Ht multi-gene resistance packages.",
            "Practice minimum 1-year crop rotation out of corn to deplete overwintering fungal residue."
        ],
        "immediate_actions": [
            "Scout canopy weekly: check third leaf below ear leaf for cigar-shaped lesions.",
            "Apply targeted fungicide if lesions threaten ear leaf during tasseling."
        ]
    },
    "Corn___healthy": {
        "plant": "Corn (Maize)",
        "leaf_name": "Corn (Maize) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Long, linear, bright green strap-like monocot blades with distinct parallel venation, intact margins, and zero pustules or blights.",
        "pathology": "Fully active C4 photosynthetic photosynthetic apparatus with optimal carbon fixation and vigorous leaf area index (LAI).",
        "treatment_organic": "Ensure side-dressing of organic nitrogen (blood meal, feather meal, composted manure) at V4-V6 vegetative stages.",
        "treatment_chemical": "No fungicide required. Maintain standard N-P-K nutrient fertility and soil moisture.",
        "prevention_guide": [
            "Plant in warm soil (>10°C) with proper plant density (28,000-34,000 plants/acre).",
            "Maintain clean field borders free of volunteer corn and wild grass weed hosts."
        ],
        "immediate_actions": [
            "Continue standard crop scouting and seasonal fertility management."
        ]
    },

    # ------------------ GRAPE ------------------
    "Grape___Black_rot": {
        "plant": "Grape",
        "leaf_name": "Grape Leaf",
        "condition": "Black Rot",
        "pathogen_type": "Fungal",
        "causal_agent": "Guignardia bidwellii / Phyllosticta ampelicida (Fungus)",
        "is_healthy": False,
        "symptoms": "Small circular reddish-brown spots with dark borders on foliage; tiny black pycnidia (pimples) form in rings within lesions.",
        "pathology": "Fungus overwinters in mummified grape berries and infected cane lesions. Ascospores infect young tissue in warm rain.",
        "treatment_organic": "Apply copper-soap or sulfur sprays early season. Diligently prune away and burn mummified grape clusters and infected canes.",
        "treatment_chemical": "Apply Mancozeb, Captan, or systemic DMI fungicides (e.g. Myclobutanil, Tebuconazole) from early shoot development through fruit set.",
        "prevention_guide": [
            "Prune vines in dormant season to open the canopy for maximum air circulation and sun exposure.",
            "Clean vineyard floor of all mummified grapes and fallen leaf litter before spring bud break."
        ],
        "immediate_actions": [
            "Remove visible mummified berry clusters and diseased foliage immediately.",
            "Apply protective fungicide coverage before the next forecasted rain event."
        ]
    },
    "Grape___healthy": {
        "plant": "Grape",
        "leaf_name": "Grape Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Broad, vibrant green, 3-5 lobed palmate blades with intact serrations, prominent radiating veins, and zero fungal lesions.",
        "pathology": "High chlorophyll density supporting vigorous vine growth, cluster development, and sugar synthesis.",
        "treatment_organic": "Maintain clean organic vine mulch, apply compost tea, and practice shoot positioning and canopy thinning.",
        "treatment_chemical": "No fungicide required. Maintain balanced micronutrients (Magnesium and Iron foliar spray if chlorosis appears).",
        "prevention_guide": [
            "Practice vertical shoot positioning (VSP) to keep grapevine canopy well-aerated.",
            "Water at the vine base using drip irrigation to maintain completely dry foliage."
        ],
        "immediate_actions": [
            "Continue standard trellis management, shoot tucking, and leaf pulling around fruit zones."
        ]
    },

    # ------------------ MANGO ------------------
    "Mango___Anthracnose": {
        "plant": "Mango",
        "leaf_name": "Mango Leaf",
        "condition": "Anthracnose",
        "pathogen_type": "Fungal",
        "causal_agent": "Colletotrichum gloeosporioides (Fungus)",
        "is_healthy": False,
        "symptoms": "Small angular dark-brown to black spots enlarging into irregular necrotic lesions, often causing leaf distortion and blossom blight.",
        "pathology": "Fungus survives in dead twigs and infected foliage. High relative humidity (>95%) and warm temperatures (24-30°C) drive rapid conidial sporulation.",
        "treatment_organic": "Spray copper oxychloride (3g/L) or neem oil (5ml/L) during flush emergence and flowering. Prune dead twigs.",
        "treatment_chemical": "Apply Azoxystrobin, Difenoconazole, or Carbendazim sprays starting at panicle emergence and repeat at 14-day intervals.",
        "prevention_guide": [
            "Prune tree canopy annually post-harvest to remove crossing branches and improve interior light and airflow.",
            "Harvest fruit carefully to avoid sap burn and peel abrasions which provide pathogen entry points."
        ],
        "immediate_actions": [
            "Prune blighted twigs and infected leaf clusters 4 inches below necrotic margins.",
            "Apply copper-based protectant spray before monsoonal or heavy rainfall periods."
        ]
    },
    "Mango___Bacterial_canker": {
        "plant": "Mango",
        "leaf_name": "Mango Leaf",
        "condition": "Bacterial Black Spot / Canker",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas citri pv. mangiferaeindicae (Bacterium)",
        "is_healthy": False,
        "symptoms": "Angular, water-soaked, raised black lesions surrounded by distinct yellow chlorotic halos on leaves and petioles; leaves crack and drop.",
        "pathology": "Bacterium enters through natural stomata and mechanical wounds. Wind-driven rains facilitate rapid tree-to-tree spread.",
        "treatment_organic": "Spray copper hydroxide combined with agricultural streptocycline (100 ppm) or bio-bactericide (Bacillus subtilis).",
        "treatment_chemical": "Apply Copper oxychloride (0.3%) plus Kasugamycin or Streptomycin sulphate at bud break and early vegetative flush.",
        "prevention_guide": [
            "Plant windbreaks around orchards to minimize foliar abrasions caused by wind-driven sand and branch rubbing.",
            "Use disease-free grafted saplings from certified certified phytosanitary nurseries."
        ],
        "immediate_actions": [
            "Prune infected branches during dry weather; sterilize tools with 70% ethanol.",
            "Apply copper-bactericide spray to protect uninfected tender new leaf flushes."
        ]
    },
    "Mango___healthy": {
        "plant": "Mango",
        "leaf_name": "Mango Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Thick, leathery, dark-green glossy lanceolate leaf with smooth entire margin, prominent pale midrib, and zero necrotic spots.",
        "pathology": "Robust waxy foliar cuticle preventing pathogen penetration and transpirational water stress, supporting heavy floral panicles.",
        "treatment_organic": "Apply organic neem cake around tree basin, mulch drip line with dry organic leaves, and irrigate regularly during fruit growth.",
        "treatment_chemical": "No chemical treatment required. Apply micronutrient foliar spray (Zinc, Boron, Copper) prior to flowering flush.",
        "prevention_guide": [
            "Maintain clean tree basins free of decaying leaves and weeds.",
            "Prune center water sprouts annually to maintain an open umbrella canopy structure."
        ],
        "immediate_actions": [
            "Continue standard orchard irrigation and seasonal fertilizer schedule."
        ]
    },

    # ------------------ POTATO ------------------
    "Potato___Early_blight": {
        "plant": "Potato",
        "leaf_name": "Potato Leaf",
        "condition": "Early Blight",
        "pathogen_type": "Fungal",
        "causal_agent": "Alternaria solani (Fungus)",
        "is_healthy": False,
        "symptoms": "Dark brown circular-to-angular spots with distinct concentric rings creating a 'target board' pattern on older lower leaves.",
        "pathology": "Pathogen overwinters in crop debris. Spores disperse via wind, rain, and mechanical contact during warm, humid conditions (24-29°C).",
        "treatment_organic": "Spray copper octanoate or Bacillus amyloliquefaciens bio-fungicide. Strip severely infected lower foliage to halt upward spread.",
        "treatment_chemical": "Apply protectant fungicides (Mancozeb, Chlorothalonil) or translaminar systemic fungicides (Azoxystrobin, Boscalid).",
        "prevention_guide": [
            "Rotate potato fields with non-solanaceous crops (corn, cereals, legumes) for at least 3 years.",
            "Maintain optimal plant nutrition; plants stressed by low nitrogen are significantly more vulnerable."
        ],
        "immediate_actions": [
            "Prune and safely discard heavily spotted lower leaves.",
            "Water strictly at base using drip irrigation; avoid overhead sprinklers."
        ]
    },
    "Potato___Late_blight": {
        "plant": "Potato",
        "leaf_name": "Potato Leaf",
        "condition": "Late Blight",
        "pathogen_type": "Oomycete",
        "causal_agent": "Phytophthora infestans (Oomycete / Water Mold)",
        "is_healthy": False,
        "symptoms": "Large, irregular water-soaked dark brown-to-black lesions with pale green borders; white fuzzy mold on leaf undersides in high humidity.",
        "pathology": "Historically devastating oomycete that caused the Irish Potato Famine. Spreads exponentially in cool (12-20°C), wet, foggy conditions.",
        "treatment_organic": "Apply fixed copper fungicides (copper hydroxide) proactively before rain. Rogue out and destroy entire infected plants immediately.",
        "treatment_chemical": "Apply systemic oomycide fungicides (e.g. Mefenoxam, Metalaxyl, Cymoxanil, Mandipropamid) at earliest regional disease warning.",
        "prevention_guide": [
            "Plant only certified disease-free seed tubers.",
            "Hill soil deeply around potato rows to prevent motile zoospores from washing down into developing tubers."
        ],
        "immediate_actions": [
            "Inspect field immediately: remove and seal infected plants in plastic bags for disposal.",
            "Apply curative systemic fungicide across all adjacent potato rows."
        ]
    },
    "Potato___healthy": {
        "plant": "Potato",
        "leaf_name": "Potato Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Vibrant compound foliage, smooth dark-green epidermis, intact trichomes, no water soaking, target rings, or necrotic flecks.",
        "pathology": "Active vegetative canopy supporting healthy tuber initiation, stolon development, and continuous starch accumulation.",
        "treatment_organic": "Maintain regular hill maintenance, certified organic seed sourcing, compost tea application, and balanced soil moisture.",
        "treatment_chemical": "No fungicide required. Apply balanced 10-10-10 or 5-10-10 fertilizer to support tuber bulking.",
        "prevention_guide": [
            "Maintain consistent soil moisture through drip irrigation.",
            "Hill potatoes every 2-3 weeks to protect tubers from sunlight and pests."
        ],
        "immediate_actions": [
            "Continue standard hilling and scout foliage twice weekly for early signs of blight."
        ]
    },

    # ------------------ TOMATO ------------------
    "Tomato___Bacterial_spot": {
        "plant": "Tomato",
        "leaf_name": "Tomato Leaf",
        "condition": "Bacterial Spot",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas perforans / euvesicatoria (Bacterium)",
        "is_healthy": False,
        "symptoms": "Small, dark brown-to-black angular spots (1-3 mm) with yellow halos; lesions coalesce causing leaf yellowing, browning, and defoliation.",
        "pathology": "Seed-borne and debris-borne bacterium. Spreads via splashing rain and sprinkler irrigation in warm, wet weather (24-30°C).",
        "treatment_organic": "Apply fixed copper bactericides combined with bio-control agents (Bacillus subtilis, Serenade ASO). Rogue out diseased seedlings.",
        "treatment_chemical": "Apply copper bactericides tank-mixed with Mancozeb (improves copper bioavailability against copper-tolerant Xanthomonas strains).",
        "prevention_guide": [
            "Use hot-water treated or certified disease-free tomato seeds and transplants.",
            "Avoid handling, pruning, or tying tomato plants when foliage is wet from rain or dew."
        ],
        "immediate_actions": [
            "Remove and destroy severely spotted lower leaves to prevent splash dispersion.",
            "Switch from overhead sprinkler to drip irrigation immediately."
        ]
    },
    "Tomato___Early_blight": {
        "plant": "Tomato",
        "leaf_name": "Tomato Leaf",
        "condition": "Early Blight",
        "pathogen_type": "Fungal",
        "causal_agent": "Alternaria solani (Fungus)",
        "is_healthy": False,
        "symptoms": "Concentric target-like circular dark-brown lesions with distinct yellow chlorotic halos, beginning on lower leaves and moving up.",
        "pathology": "Soil-borne and crop residue-borne fungal pathogen. Rain splash transfers spores to lower leaves in warm, humid weather.",
        "treatment_organic": "Prune all lower leaves up to 12 inches above the soil line. Spray copper octanoate, sulfur, or Bacillus subtilis biofungicide.",
        "treatment_chemical": "Apply protectant fungicides (Chlorothalonil, Mancozeb) or translaminar fungicides (Azoxystrobin, Difenoconazole) every 7-10 days.",
        "prevention_guide": [
            "Stake or cage tomato plants and apply 2-3 inches of straw mulch beneath plants to prevent soil splash.",
            "Practice 3-year crop rotation away from solanaceous plants (potato, pepper, eggplant)."
        ],
        "immediate_actions": [
            "Prune off all affected lower leaves up to 12 inches above mulch.",
            "Apply protective fungicide coverage to prevent disease ascent onto fruiting clusters."
        ]
    },
    "Tomato___healthy": {
        "plant": "Tomato",
        "leaf_name": "Tomato Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Intact compound pinnate foliage, vibrant green color, characteristic trichome fragrance, and complete absence of necrotic lesions.",
        "pathology": "Optimal photosynthetic capacity driving vigorous flower cluster set, pollination, and continuous lycopene-rich fruit production.",
        "treatment_organic": "Maintain regular drip irrigation, apply worm casting tea monthly, and maintain organic straw mulch over root zones.",
        "treatment_chemical": "No fungicide required. Supplement with Calcium-Magnesium (Cal-Mag) to prevent blossom-end rot in developing fruit.",
        "prevention_guide": [
            "Prune suckers and stake plants to ensure maximum vertical airflow.",
            "Water deeply in the morning at the soil base to maintain dry leaves."
        ],
        "immediate_actions": [
            "Continue standard trellising, sucker management, and fruit-cluster maintenance."
        ]
    },

    # ------------------ CITRUS ------------------
    "Citrus___Citrus_canker": {
        "plant": "Citrus",
        "leaf_name": "Citrus / Lemon Leaf",
        "condition": "Citrus Canker",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas citri subsp. citri (Bacterium)",
        "is_healthy": False,
        "symptoms": "Raised, corky, blister-like brown pustules on both leaf surfaces surrounded by characteristic bright oily yellow chlorotic halos.",
        "pathology": "Bacteria enter stomata and leaf wounds made by wind or citrus leafminers. Wind-driven rains cause rapid orchard spread.",
        "treatment_organic": "Spray copper hydroxide or copper octanoate at 21-day intervals during new vegetative flushes. Control citrus leafminer pests.",
        "treatment_chemical": "Apply preventive copper-based bactericides combined with systemic acquired resistance (SAR) inducers.",
        "prevention_guide": [
            "Plant windbreak trees around citrus orchards to reduce wind speeds below 18 mph.",
            "Disinfect pruning shears, vehicles, and harvest crates with quaternary ammonium compounds."
        ],
        "immediate_actions": [
            "Prune diseased shoots during dry weather and safely dispose of clippings.",
            "Apply copper bactericide before upcoming rainy periods."
        ]
    },
    "Citrus___healthy": {
        "plant": "Citrus",
        "leaf_name": "Citrus / Lemon Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Glossy, deep-green oval leaves with winged petioles, aromatic oil glands, and complete absence of corky lesions or greasy spots.",
        "pathology": "Optimal photosynthetic and transpirational health supporting vigorous vegetative flushing and high-quality citrus fruit set.",
        "treatment_organic": "Apply organic citrus fertilizer with balanced iron and zinc, mulch with organic wood chips, and irrigate regularly.",
        "treatment_chemical": "No chemical treatment required. Apply chelated iron or zinc foliar spray if minor interveinal chlorosis occurs.",
        "prevention_guide": [
            "Irrigate regularly under tree drip line; avoid wetting the tree trunk to prevent collar rot (Phytophthora).",
            "Monitor tree canopy for scale insects, aphids, or leafminers."
        ],
        "immediate_actions": [
            "Continue standard citrus feeding and seasonal watering."
        ]
    },

    # ------------------ PEPPER ------------------
    "Pepper___Bacterial_spot": {
        "plant": "Pepper",
        "leaf_name": "Bell Pepper Leaf",
        "condition": "Bacterial Spot",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas campestris pv. vesicatoria (Bacterium)",
        "is_healthy": False,
        "symptoms": "Small, water-soaked, circular to irregular dark brown spots that become sunken with light brown centers; leaves turn yellow and drop.",
        "pathology": "Bacterium overwinters on crop residue and contaminated seed. Warm, humid, rainy weather drives rapid dissemination.",
        "treatment_organic": "Spray fixed copper bactericide combined with Bacillus subtilis biofungicide. Strip severely affected lower leaves.",
        "treatment_chemical": "Apply copper hydroxide tank-mixed with Mancozeb at 7-10 day intervals during warm, wet periods.",
        "prevention_guide": [
            "Plant certified disease-free seeds and resistant pepper varieties (e.g. varieties with Bs resistance genes).",
            "Rotate out of solanaceous crops for a minimum of 2-3 years."
        ],
        "immediate_actions": [
            "Stop overhead sprinkler irrigation immediately.",
            "Apply copper-bactericide spray to protect newly emerging foliage."
        ]
    },
    "Pepper___healthy": {
        "plant": "Pepper",
        "leaf_name": "Bell Pepper Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Smooth, vibrant green, elliptical leaves with intact margins, prominent central midrib, and zero necrotic spotting or curling.",
        "pathology": "Healthy photosynthetic tissue providing abundant assimilate for continuous blossom formation and pepper pod enlargement.",
        "treatment_organic": "Apply compost tea, maintain even drip irrigation, and apply organic straw mulch around plant base.",
        "treatment_chemical": "No fungicide required. Supplement with balanced calcium and potassium fertilizer for thick pod walls.",
        "prevention_guide": [
            "Provide consistent watering to prevent blossom end rot.",
            "Cage or stake plants to prevent heavy fruit loads from snapping branches."
        ],
        "immediate_actions": [
            "Continue standard garden maintenance and pest scouting."
        ]
    },

    # ------------------ STRAWBERRY ------------------
    "Strawberry___Leaf_scorch": {
        "plant": "Strawberry",
        "leaf_name": "Strawberry Leaf",
        "condition": "Leaf Scorch",
        "pathogen_type": "Fungal",
        "causal_agent": "Diplocarpon earlianum (Fungus)",
        "is_healthy": False,
        "symptoms": "Numerous small, irregular, purple to dark reddish-brown blotches on upper leaf surfaces; spots coalesce causing entire leaf to dry and scorch.",
        "pathology": "Overwinters in infected strawberry foliage. Conidia splash in spring rain to infect new leaves during warm, wet weather.",
        "treatment_organic": "Apply copper octanoate or sulfur sprays early in the season. Remove and discard heavily scorched leaves during autumn renovation.",
        "treatment_chemical": "Apply Captan or Pyraclostrobin + Boscalid fungicides starting at early spring leaf emergence.",
        "prevention_guide": [
            "Plant in well-drained raised beds with straw mulch to prevent soil splashing.",
            "Renovate strawberry beds after harvest by mowing and raking old diseased foliage."
        ],
        "immediate_actions": [
            "Remove and discard severely scorched leaves.",
            "Apply protective fungicide coverage before incoming rain."
        ]
    },
    "Strawberry___healthy": {
        "plant": "Strawberry",
        "leaf_name": "Strawberry Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Vibrant, trifoliate leaves with deep-green color, distinct serrated margins, intact veins, and zero purple spotting or edge curling.",
        "pathology": "Active photosynthetic leaf area providing energy for vigorous stolon runner production, flowering, and sweet berry maturation.",
        "treatment_organic": "Maintain clean pine needle or straw mulch beneath plants, water via drip irrigation, and apply organic fish emulsion.",
        "treatment_chemical": "No fungicide required. Maintain balanced potassium for sweet berry sugar production.",
        "prevention_guide": [
            "Keep berries and foliage off direct soil contact with clean straw mulch.",
            "Replace strawberry plants every 3-4 years to maintain maximum disease resistance and vigor."
        ],
        "immediate_actions": [
            "Continue standard berry care and runner management."
        ]
    },

    # ------------------ BANANA ------------------
    "Banana___Black_sigatoka": {
        "plant": "Banana",
        "leaf_name": "Banana Leaf",
        "condition": "Black Sigatoka (Black Leaf Streak)",
        "pathogen_type": "Fungal",
        "causal_agent": "Pseudocercospora fijiensis / Mycosphaerella fijiensis (Fungus)",
        "is_healthy": False,
        "symptoms": "Narrow, reddish-brown streaks running parallel to leaf veins, enlarging into dark brown to black necrotic blotches with yellow halos and sunken gray centers.",
        "pathology": "Airborne ascospores germinate in free water droplets on leaf undersides, penetrating stomata and causing massive foliar collapse.",
        "treatment_organic": "Perform strict deleafing (surgical removal of infected leaf strips). Spray mineral oil combined with copper oxychloride or biofungicides.",
        "treatment_chemical": "Apply systemic fungicides (e.g. Difenoconazole, Epoxiconazole, Azoxystrobin) rotated with protectants (Mancozeb).",
        "prevention_guide": [
            "Maintain optimal plant density and plantation drainage to reduce standing water and canopy humidity.",
            "Plant resistant hybrid banana cultivars (e.g. FHIA hybrids)."
        ],
        "immediate_actions": [
            "Surgically cut out and destroy necrotic leaf sectors immediately.",
            "Apply protective fungicide-oil emulsion to remaining healthy leaves."
        ]
    },
    "Banana___healthy": {
        "plant": "Banana",
        "leaf_name": "Banana Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Massive, emerald-green, paddle-shaped leaf blades with smooth intact lamina, robust central midrib, and zero necrotic streaking.",
        "pathology": "High leaf area index (LAI) facilitating rapid photosynthetic assimilate generation necessary for heavy banana bunch development.",
        "treatment_organic": "Apply organic compost, maintain thick organic mulch around pseudostem base, and ensure heavy potassium feeding.",
        "treatment_chemical": "No chemical treatment required. Apply balanced N-P-K (high Potassium) fertilizer to support bunch filling.",
        "prevention_guide": [
            "Remove dead lower leaves regularly to maintain good airflow around pseudostems.",
            "Maintain 3-4 healthy functional leaves per banana plant minimum prior to harvest."
        ],
        "immediate_actions": [
            "Continue standard plantation desuckering and bunch-propping maintenance."
        ]
    },

    # ------------------ CUCUMBER ------------------
    "Cucumber___Powdery_mildew": {
        "plant": "Cucumber",
        "leaf_name": "Cucumber Leaf",
        "condition": "Powdery Mildew",
        "pathogen_type": "Fungal",
        "causal_agent": "Podosphaera xanthii / Golovinomyces cichoracearum (Fungus)",
        "is_healthy": False,
        "symptoms": "White, talcum-powder-like fungal spots on upper and lower leaf surfaces, enlarging to cover entire leaf blade; leaves turn yellow, brown, and senesce.",
        "pathology": "Airborne conidia infect foliage in warm, dry weather accompanied by high relative humidity at night. Haustoria rob plant nutrients.",
        "treatment_organic": "Spray potassium bicarbonate (4 g/L), milk spray (40% milk, 60% water), or neem oil (0.5%) at first appearance of white spots.",
        "treatment_chemical": "Apply systemic fungicides such as Myclobutanil, Trifloxystrobin, or Quinoxyfen at early vegetative stages.",
        "prevention_guide": [
            "Plant powdery mildew-resistant cucumber varieties (e.g. Marketmore 76, Diva, Spacemaster).",
            "Trellis cucumber vines vertically to maximize sunlight and airflow around foliage."
        ],
        "immediate_actions": [
            "Apply potassium bicarbonate or neem spray immediately across both leaf surfaces.",
            "Prune yellowing, heavily infected lower leaves."
        ]
    },
    "Cucumber___healthy": {
        "plant": "Cucumber",
        "leaf_name": "Cucumber Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Broad, vibrant green, triangular-ovate palmate-lobed leaves with rough surface trichomes, intact margins, and zero white powdery patches.",
        "pathology": "Optimal photosynthetic activity driving rapid vine elongation, continuous flowering, and uniform cucumber fruit expansion.",
        "treatment_organic": "Maintain steady drip irrigation, mulch with straw, and apply liquid seaweed extract to support continuous fruit production.",
        "treatment_chemical": "No fungicide required. Maintain consistent nitrogen and potassium fertility.",
        "prevention_guide": [
            "Water early in the morning at the soil level; keep foliage dry.",
            "Trellis vines to prevent leaves from touching wet soil."
        ],
        "immediate_actions": [
            "Continue vertical vine training and regular fruit harvesting."
        ]
    },

    # ------------------ ROSE ------------------
    "Rose___Black_spot": {
        "plant": "Rose",
        "leaf_name": "Rose Leaf",
        "condition": "Black Spot",
        "pathogen_type": "Fungal",
        "causal_agent": "Diplocarpon rosae (Fungus)",
        "is_healthy": False,
        "symptoms": "Circular black spots with feathery, fringed margins on upper leaf surfaces; surrounding leaf tissue turns bright yellow and drops prematurely.",
        "pathology": "Spore germination requires at least 7 hours of continuous leaf wetness. Rain splash transfers conidia upwards into the rose bush canopy.",
        "treatment_organic": "Apply baking soda spray (1 tbsp baking soda + 1 tsp horticultural oil per gallon of water) or copper fungicide weekly.",
        "treatment_chemical": "Apply systemic fungicides containing Tebuconazole, Propiconazole, or Chlorothalonil every 10-14 days during wet periods.",
        "prevention_guide": [
            "Prune rose bushes in late winter to create an open vase-shaped center for maximum airflow.",
            "Water roses strictly at base with soaker hose or drip line; avoid wetting foliage."
        ],
        "immediate_actions": [
            "Pick off and dispose of all spotted leaves immediately; do not compost.",
            "Apply protective fungicide spray across remaining canopy."
        ]
    },
    "Rose___healthy": {
        "plant": "Rose",
        "leaf_name": "Rose Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Glossy, deep-green, odd-pinnate leaflets with sharp serrated margins, intact petiole stipules, and complete absence of black spots or powdery mildew.",
        "pathology": "Healthy foliar tissue with high anthocyanin and chlorophyll balance supporting vigorous cane growth and continuous blooming flushes.",
        "treatment_organic": "Apply organic compost around rose base, mulch with bark chips, and apply alfalfa meal for natural growth stimulation.",
        "treatment_chemical": "No chemical treatment required. Apply balanced rose fertilizer (such as 4-3-2 organic or 10-10-10).",
        "prevention_guide": [
            "Plant roses in locations receiving at least 6 hours of direct morning sunlight.",
            "Clean up all fallen autumn foliage before winter dormancy."
        ],
        "immediate_actions": [
            "Continue standard deadheading and cane maintenance."
        ]
    },

    # ------------------ GUAVA ------------------
    "Guava___Wilt": {
        "plant": "Guava",
        "leaf_name": "Guava Leaf",
        "condition": "Guava Wilt",
        "pathogen_type": "Fungal (Vascular)",
        "causal_agent": "Fusarium oxysporum f. sp. psidii (Soil-Borne Fungus)",
        "is_healthy": False,
        "symptoms": "Yellowing and upward curling of leaves, followed by rapid foliar browning, drying, and premature shedding; vascular browning in stems.",
        "pathology": "Soil-borne pathogen penetrates root system and colonizes xylem vessels, completely blocking water and nutrient transport to the canopy.",
        "treatment_organic": "Drench root zone with Trichoderma viride or Trichoderma harzianum bio-agent mixed with neem cake. Rogue out severely wilted trees.",
        "treatment_chemical": "Soil drenching with Carbendazim (0.2%) or Thiophanate-methyl (0.15%) around tree basin at earliest onset of yellowing.",
        "prevention_guide": [
            "Plant guava varieties grafted onto wilt-resistant rootstocks (e.g. Psidium cattleianum).",
            "Avoid damaging tree roots during intercultural weeding and soil plowing."
        ],
        "immediate_actions": [
            "Isolate affected tree basins to prevent fungal spread through irrigation runoff.",
            "Apply bio-control Trichoderma drench across root zone."
        ]
    },
    "Guava___healthy": {
        "plant": "Guava",
        "leaf_name": "Guava Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Thick, leathery, dark-green oblong-elliptic leaves with prominent parallel ribs, aromatic surface, and zero wilt or leaf spotting.",
        "pathology": "Uninhibited xylem and phloem transport supporting lush vegetative shoots, heavy flowering, and sweet aromatic fruit set.",
        "treatment_organic": "Maintain organic leaf mulch, apply composted manure around drip line, and irrigate regularly during fruit enlargement.",
        "treatment_chemical": "No chemical treatment required. Apply micronutrient foliar spray (Zinc, Boron) twice annually.",
        "prevention_guide": [
            "Ensure well-drained orchard soil with no stagnant water accumulation around tree trunks.",
            "Prune dead and crossing branches annually after fruit harvest."
        ],
        "immediate_actions": [
            "Continue standard orchard irrigation and seasonal care."
        ]
    },

    # ------------------ CABBAGE ------------------
    "Cabbage___Black_rot": {
        "plant": "Cabbage",
        "leaf_name": "Cabbage Leaf",
        "condition": "Black Rot",
        "pathogen_type": "Bacterial",
        "causal_agent": "Xanthomonas campestris pv. campestris (Bacterium)",
        "is_healthy": False,
        "symptoms": "V-shaped yellow chlorotic lesions along leaf margins pointing inwards, with black/dark-brown blackened veins visible within the lesion.",
        "pathology": "Bacterium enters leaf hydathodes at leaf margins during warm, wet weather (25-30°C) and spreads systemically through vascular xylem.",
        "treatment_organic": "Apply copper hydroxide or bio-bactericide (Bacillus subtilis). Remove infected outer wrapper leaves immediately.",
        "treatment_chemical": "Spray copper bactericides (Copper hydroxide, Copper oxychloride) on young brassica transplants.",
        "prevention_guide": [
            "Use certified black-rot-free, hot-water treated brassica seed.",
            "Rotate brassica crops with non-crucifers on a 3-4 year rotation schedule."
        ],
        "immediate_actions": [
            "Remove and destroy plants showing V-shaped marginal lesions.",
            "Avoid working in cabbage fields while foliage is wet."
        ]
    },
    "Cabbage___healthy": {
        "plant": "Cabbage",
        "leaf_name": "Cabbage Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Broad, smooth, waxy blue-green glaucous leaves with undulating edges, intact veins, and complete absence of V-shaped lesions.",
        "pathology": "Heavy epicuticular wax layer protecting succulent leaf tissue and driving dense cabbage head formation.",
        "treatment_organic": "Apply organic fish emulsion or blood meal, mulch with straw, and use row covers to protect against cabbage moth larvae.",
        "treatment_chemical": "No chemical treatment required. Maintain balanced nitrogen for tight head formation.",
        "prevention_guide": [
            "Maintain consistent soil moisture to prevent head splitting.",
            "Scout weekly for cabbage loopers and aphids under leaves."
        ],
        "immediate_actions": [
            "Continue regular watering and head-firmness monitoring."
        ]
    },

    # ------------------ ONION ------------------
    "Onion___Purple_blotch": {
        "plant": "Onion",
        "leaf_name": "Onion Leaf",
        "condition": "Purple Blotch",
        "pathogen_type": "Fungal",
        "causal_agent": "Alternaria porri (Fungus)",
        "is_healthy": False,
        "symptoms": "Small, water-soaked lesions that enlarge into elliptical purplish-brown blotches with dark concentric rings and yellow borders; leaves snap over.",
        "pathology": "Spore germination occurs during warm (21-30°C), wet conditions with extended dew periods (>10 hours). Spores enter through stomata and thrips wounds.",
        "treatment_organic": "Apply copper hydroxide or neem oil spray. Control onion thrips pests whose feeding wounds enable fungal entry.",
        "treatment_chemical": "Apply fungicides such as Difenoconazole, Azoxystrobin, or Mancozeb at first sign of purple foliar lesions.",
        "prevention_guide": [
            "Rotate out of allium crops (onion, garlic, leek) for at least 3 years.",
            "Ensure wide plant spacing and excellent field drainage."
        ],
        "immediate_actions": [
            "Apply protective fungicide before heavy dew or rain periods.",
            "Ensure spray solution includes a spreader-sticker surfactant to adhere to waxy cylindrical leaves."
        ]
    },
    "Onion___healthy": {
        "plant": "Onion",
        "leaf_name": "Onion Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Upright, tubular, hollow, waxy glaucous-green cylindrical foliage with intact tips and zero purple blotches or dieback.",
        "pathology": "Vigorous photosynthetic activity in tubular leaves driving sugar translocation downwards to expand underground onion bulb scales.",
        "treatment_organic": "Apply organic fish fertilizer, keep beds weed-free, and maintain steady moisture until bulb maturation.",
        "treatment_chemical": "No fungicide required. Stop nitrogen application once bulbing initiates to prevent thick neck development.",
        "prevention_guide": [
            "Avoid overhead irrigation; water via drip lines.",
            "Stop watering 2-3 weeks before harvest when tops begin falling over."
        ],
        "immediate_actions": [
            "Continue standard weed control and bulb expansion monitoring."
        ]
    },

    # ------------------ RICE ------------------
    "Rice___Brown_spot": {
        "plant": "Rice (Paddy)",
        "leaf_name": "Rice (Paddy) Leaf",
        "condition": "Brown Spot",
        "pathogen_type": "Fungal",
        "causal_agent": "Bipolaris oryzae / Cochliobolus miyabeanus (Fungus)",
        "is_healthy": False,
        "symptoms": "Small, circular to oval dark-brown spots with gray or whitish centers and reddish-brown margins scattered across linear leaf blades.",
        "pathology": "Airborne and seed-borne fungus. Historically severe under poor soil fertility (silicon, potassium, or nitrogen deficiency) and water stress.",
        "treatment_organic": "Apply pseudomonas fluorescens bio-seed treatment and foliar spray. Incorporate silicon and potassium into paddy soil.",
        "treatment_chemical": "Apply Azoxystrobin, Propiconazole, or Tricyclazole sprays at early tillering and panicle initiation stages.",
        "prevention_guide": [
            "Use certified disease-free, fungicide-treated rice seeds.",
            "Maintain proper water depth in paddy fields and avoid drought stress during vegetative growth."
        ],
        "immediate_actions": [
            "Ensure paddy fields maintain continuous standing water depth.",
            "Apply top-dressing of potassium fertilizer and targeted fungicide."
        ]
    },
    "Rice___healthy": {
        "plant": "Rice (Paddy)",
        "leaf_name": "Rice (Paddy) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Erect, vibrant green, linear blades with intact parallel veins, sharp tips, and zero brown spotting or leaf blast lesions.",
        "pathology": "High chlorophyll content supporting maximum tillering, panicle emergence, and high grain-filling percentage.",
        "treatment_organic": "Apply neem-coated urea, Azolla biofertilizer, and maintain optimal water level management.",
        "treatment_chemical": "No fungicide required. Maintain balanced nitrogen-phosphorus-potassium-zinc nutrition in paddy.",
        "prevention_guide": [
            "Practice alternate wetting and drying (AWD) water management where appropriate.",
            "Maintain weed-free levees to eliminate wild grass pathogen hosts."
        ],
        "immediate_actions": [
            "Continue standard paddy water management and tillering monitoring."
        ]
    },

    # ------------------ WHEAT ------------------
    "Wheat___Leaf_rust": {
        "plant": "Wheat",
        "leaf_name": "Wheat Leaf",
        "condition": "Leaf Rust (Brown Rust)",
        "pathogen_type": "Fungal",
        "causal_agent": "Puccinia triticina (Airborne Rust Fungus)",
        "is_healthy": False,
        "symptoms": "Small, circular to oval, reddish-orange powdery pustules (uredinia) scattered randomly across upper leaf surfaces and flag leaves.",
        "pathology": "Airborne urediniospores travel thousands of miles on wind currents. Spores infect in free moisture at 15-22°C, reducing flag leaf photosynthesis.",
        "treatment_organic": "Apply wettable sulfur dust or Trichoderma harzianum bio-protectants at earliest detection.",
        "treatment_chemical": "Apply systemic triazole or strobilurin fungicides (e.g. Tebuconazole, Propiconazole, Pyraclostrobin) before rust reaches flag leaf.",
        "prevention_guide": [
            "Plant wheat cultivars with diverse Lr genetic rust resistance combinations.",
            "Eradicate alternate hosts (Thalictrum spp.) near wheat acreage."
        ],
        "immediate_actions": [
            "Scout the critical flag leaf: if pustules appear prior to heading, apply systemic triazole fungicide immediately.",
            "Monitor regional rust spore advisories."
        ]
    },
    "Wheat___healthy": {
        "plant": "Wheat",
        "leaf_name": "Wheat Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Long, linear, bright green erect flag leaves with parallel venation, intact margins, and zero rust pustules or powdery mildew.",
        "pathology": "Optimal flag leaf area ensuring maximum photosynthetic assimilates translocated directly into developing grain heads.",
        "treatment_organic": "Apply composted organic amendments, ensure adequate soil zinc, and scout canopy weekly.",
        "treatment_chemical": "No fungicide required. Apply top-dressed nitrogen at tillering to support dense head development.",
        "prevention_guide": [
            "Seed wheat at recommended planting depth and seeding rate in well-drained soil.",
            "Rotate wheat with non-cereal crops (soybeans, canola, legumes)."
        ],
        "immediate_actions": [
            "Continue standard crop scouting through grain-filling."
        ]
    },
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
    },

    # ------------------ MONEY PLANT ------------------
    "Money_Plant___healthy": {
        "plant": "Money_Plant",
        "leaf_name": "Money Plant (Golden Pothos) Leaf",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Glossy cordate (heart-shaped) blade with vibrant emerald green surface and golden-yellow marbling; intact smooth margins and waxy cuticle.",
        "pathology": "High chlorophyll density and active aerial root respiration; resilient indoor air-purifying foliage.",
        "treatment_organic": "Allow top 1-2 inches of potting mix to dry before watering. Wipe leaf surfaces with a damp cloth or dilute neem wash to remove household dust.",
        "treatment_chemical": "No chemical fungicides required. Apply balanced water-soluble liquid houseplant fertilizer (10-10-10) at half strength monthly during active spring/summer growth.",
        "prevention_guide": [
            "Keep in bright, indirect filtered sunlight; avoid harsh scorching direct noon rays.",
            "Ensure pot has drainage holes to prevent soggy soil and root rot.",
            "If growing in water jars, change the water every 7-10 days."
        ],
        "immediate_actions": [
            "Maintain moderate room humidity and clean glossy leaf blades."
        ]
    },
    "Money_Plant___Bacterial_leaf_spot": {
        "plant": "Money_Plant",
        "leaf_name": "Money Plant (Golden Pothos) Leaf",
        "condition": "Bacterial Leaf Spot",
        "pathogen_type": "Bacterial",
        "causal_agent": "Pseudomonas cichorii / Xanthomonas campestris (Bacteria)",
        "is_healthy": False,
        "symptoms": "Water-soaked dark brown-to-black necrotic spots with distinct translucent yellow halos expanding across heart-shaped lamina; affected leaves turn yellow and drop.",
        "pathology": "Bacterial pathogens enter via stomata or mechanical leaf tears during prolonged foliar wetness, degrading cell pectin and causing localized vascular collapse.",
        "treatment_organic": "Immediately snip off severely spotted leaves with sterilized scissors. Avoid misting or wetting foliage. Drench root zone with dilute cinnamon tea or bio-fungicide.",
        "treatment_chemical": "Apply copper hydroxide or streptomycin sulfate bactericidal spray at first onset of spreading spots.",
        "prevention_guide": [
            "Never leave standing water on pothos leaves indoors; ensure good ceiling fan or room ventilation.",
            "Isolate infected plants from other indoor houseplants until recovery."
        ],
        "immediate_actions": [
            "Cease foliar misting immediately and discard infected leaves in trash."
        ]
    },

    # ------------------ CURRY LEAF ------------------
    "Curry_Leaf___healthy": {
        "plant": "Curry_Leaf",
        "leaf_name": "Curry Leaf (Kadi Patta)",
        "condition": "Healthy Leaf",
        "pathogen_type": "None",
        "causal_agent": "None (Healthy cellular tissue)",
        "is_healthy": True,
        "symptoms": "Aromatic, dark green asymmetric ovate leaflets on pinnate rachis; rich culinary scent with zero psyllid curling or scale insects.",
        "pathology": "Active secondary terpene metabolite synthesis and healthy vascular transport.",
        "treatment_organic": "Apply sour buttermilk spray (diluted 1:5 in water) monthly; top-dress root zone with vermicompost and cow dung manure.",
        "treatment_chemical": "No chemicals recommended for culinary herbs harvested for kitchen cooking.",
        "prevention_guide": [
            "Place in full sunlight (minimum 5-6 hours daily).",
            "Prune branches regularly to stimulate bushy tender leaf production."
        ],
        "immediate_actions": [
            "Maintain moderate soil moisture and full sunlight."
        ]
    }
}

def parse_class_name(class_name: str) -> Dict[str, Any]:
    """Parse a dataset class name into structured plant, condition, pathogen, and treatment info."""
    if "___" in class_name:
        plant, condition = class_name.split("___", 1)
    else:
        plant = "Unknown"
        condition = class_name

    condition_clean = condition.replace("_", " ").strip()
    is_healthy = condition.lower() == "healthy" or "healthy" in condition.lower()
    if is_healthy:
        condition_clean = "Healthy Leaf"
    
    details = CLASS_KNOWLEDGE_BASE.get(class_name, {
        "plant": plant,
        "leaf_name": f"{plant} Leaf",
        "condition": condition_clean,
        "pathogen_type": "None" if is_healthy else "Biological Pathogen",
        "causal_agent": "None (Healthy cellular tissue)" if is_healthy else "Phytopathogenic organism",
        "is_healthy": is_healthy,
        "symptoms": "Normal vegetative leaf tissue with intact chlorophyll." if is_healthy else f"Visual signs characteristic of {condition_clean}.",
        "pathology": "Cellular structure intact with active photosynthesis." if is_healthy else "Pathological cellular response in plant foliage.",
        "treatment_organic": "Maintain regular watering, organic mulch, and standard scouting." if is_healthy else "Remove infected leaves and apply copper-based organic spray.",
        "treatment_chemical": "No chemical treatment required." if is_healthy else "Apply broad-spectrum protectant fungicide or bactericide according to label instructions.",
        "prevention_guide": [
            "Maintain proper plant spacing for airflow.",
            "Water at the soil level to keep foliage dry.",
            "Rotate crops annually."
        ],
        "immediate_actions": [
            "Inspect overall plant health.",
            "Ensure adequate sunlight and drainage."
        ]
    })
    
    species_info = PLANT_SPECIES_INFO.get(plant, {})
    leaf_name = details.get("leaf_name") or species_info.get("leaf_name") or f"{plant} Leaf"
    
    return {
        "class_name": class_name,
        "plant_name": plant,
        "leaf_name": leaf_name,
        "condition_name": condition_clean,
        "is_healthy": is_healthy,
        "scientific_name": species_info.get("scientific_name", "N/A"),
        "plant_family": species_info.get("family", "N/A"),
        "pathogen_type": details.get("pathogen_type", "Unknown"),
        "causal_agent": details.get("causal_agent", "Unknown"),
        "symptoms": details.get("symptoms", ""),
        "pathology": details.get("pathology", ""),
        "treatment_organic": details.get("treatment_organic", ""),
        "treatment_chemical": details.get("treatment_chemical", ""),
        "prevention_guide": details.get("prevention_guide", []),
        "immediate_actions": details.get("immediate_actions", []),
        "management_research": details.get("treatment_organic", "")
    }
