# Configuration file for the Research Paper ( Evaluating Rule-Based AI Approaches for Food Healthiness Classification)

# Nutritional Thresholds based on the World Health Organization (WHO) guidelines and their nutri-scores
NUTRITIONAL_THRESHOLDS = {
    'sugar_high' : 20, # grams per 100g
    'fat_high' : 15,  # grams per 100g
    'calories_low' : 250, #grams per 100g
    'calories_high' : 400, #grams per 100g
    'sugar_moderate' : 10, #grams per 100g
    'fiber_high' : 3, #grams per 100g
    'fiber_very_high' : 5, #grams per 100g
    'protein_high' : 10 #grams per 100g
}

# Weighted Scoring System Variables
SCORING_RULES = {
    'fiber_high' : {'threshold': 5, 'score': 3},
    'protein_high': {'threshold': 10, 'score': 2},
    'calories_high': {'threshold': 400, 'score': -1},
    'sugar_high': {'threshold': 15, 'score': -2}
}

# Classification Thresholds for the Weighted Scoring System
CLASSIFICATION_THRESHOLD = {
    'healthy': 3,
    'moderate_min': 0.5,
    'moderate_max': 2.9,
    'unhealthy': 0.5
}
