import pandas as pd
import numpy as np  
from typing import Dict, Any, List
from config import NUTRITIONAL_THRESHOLDS, SCORING_RULES, CLASSIFICATION_THRESHOLD

class ThresholdRuleBasedSystem:
    # This is the Threshold Rule-based System for the classifying the food dataset

    def __init__(self):
        self.thresholds = NUTRITIONAL_THRESHOLDS
        self.rules_applied = []

    def classify_food(self, nutritional_facts: Dict[str, Any]) -> str:
        # This classifies the food  using the threshold-based rules 
        # It returns terms such as 'healthy', 'moderate' and 'unhealthy'

        self.rules_applied = []

    # Extract nutritional values

        calories = nutritional_facts.get('energy_kcal', 0)
        sugar = nutritional_facts.get('sugars_g', 0)
        fat = nutritional_facts.get('fat_g', 0)
        fiber = nutritional_facts.get('fiber_g', 0)
        processed = nutritional_facts.get('processed', False)

        # Rule 1: Processed Foods with high sugar or high fat are UNHEALTHY
        if processed and (sugar > self.thresholds['sugar_high'] or fat > self.thresholds['fat_high']): 
            self.rules_applied.append("Processed with high fat/sugar")

            return 'Unhealthy'
        
        # Rule 2: Low Calories, Sugar, High fiber but not processed are considered HEALTHY
        if (calories < self.thresholds['calories_low'] and
        sugar < self.thresholds['sugar_moderate'] and 
        fiber > self.thresholds['fiber_high'] and 
        not processed):
            
            self.rules_applied.append ("Low Calories, sugar, High Fiber, Not Processed")
            return 'Healthy'
        
        # Rule 3: Additional healthy Criteria
        if (fiber > self.thresholds['fiber_very_high'] and 
            sugar < self.thresholds['sugar_moderate'] and
            fat < self.thresholds['fat_high']):

            self.rules_applied( "High fiber, low sugar, moderate fat")
            return 'Healthy'

        # Rule 4: High Calories with a low nutritional value is considered UNHEALTHY 
        if (calories > self.thresholds ['calories_high'] and 
            fiber < self.thresholds['fiber_high'] and 
            sugar > self.thresholds['sugar_high']): 
            
            self.rules_applied.append("High Calories, Sugar, Low Fiber")
            return 'Unhealthy'
        
        # Normal Classification
        self.rules_applied.append("Normal moderate Classification")

        return 'Moderate'
    
    def batch_classify(self, data: pd.DataFrame) -> List[str]:
        # This classifies multiple food items 
        classification = []
        for _, row in data.iterrows():
            classification = self.classify_food(row.to.dict())
            classification.append(classification)
        return classification
    
    class WeightedRulebasedSystem:
        # This is the weighted scoring system for classifying the foods

        def __init__(self):
            self.scoring_rules = SCORING_RULES
            self.class_thresholds = CLASSIFICATION_THRESHOLD

        def calculate_score(self, nutritional_facts: Dict[str, Any]) -> float:
            # This calculates the score based on the nutritional facts given
            
            score = 0

            # This extracts the nutritional values
            fiber = nutritional_facts.get('fiber_g', 0)
            protein = nutritional_facts.get('proteins_g', 0)
            calories = nutritional_facts.get('energy_kcal', 0)
            sugar = nutritional_facts.get('sugar_g', 0)
            fat = nutritional_facts.get('fat_g', 0)
            saturated_fat = nutritional_facts.get('saturated_fat_g', 0)
            processed = nutritional_facts.get('processed', False)

            # Positive scores will show as 'Health-promoting nutrients'
            if fiber >= self.scoring_rules['fiber_high']['threshold']:
                score += self.scoring_rules['fiber_high']['score']

            if protein >= self.scoring_rules['protein_high']['threshold']:
                score += self.scoring_rules['protein_high']['score']

            # Extra health factors
            if fiber > 3: #This will show that it has moderate fiber
                score += 1
            if protein > 5: #This will show that it has moderate protein
                score += 1

            # Negative scores will show as 'Unhealthy-risk nutrients'
            if calories > self.scoring_rules['calories_high']['threshold']:
                score += self.scoring_rules['calories_high']['score']

            if sugar >= self.scoring_rules['sugar_high']['threshold']:
                score += self.scoring_rules['sugar_high']['score']

            # Extra Negative factors
            if fat > 20: # This means the food has high fat
                score -= 1
            if saturated_fat > 5: # This means the food has high saturated fat
                score -= 1
            if processed: # This means that the food is high processed
                score -= 1

            return score
        
        def classify_food(self, nutritional_facts: Dict[str, Any]) -> str:
            # This classifies food based on their score nutritionally
            score = self.calculate_score(nutritional_facts)

            if score >= self.class_thresholds['Healthy']:
                return 'Healthy' 
            elif score >= self.class_thresholds['moderate_min']:
                return 'Moderate'
            else: 
                return 'Unhealthy'
            
        def batch_classify(self, data: pd.DataFrame) -> List[str]:
            # This classifies multiple food items
            classification = []
            for _, row in data.iterrows():
                classification = self.classify_food(row.to_dict())
                classification.append(classification)
            return classification








