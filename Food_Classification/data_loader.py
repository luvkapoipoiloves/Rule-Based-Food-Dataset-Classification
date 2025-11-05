import pandas as pd
import numpy as np
from typing import Dict, Any

class FoodDataloader:
    # Loads and Processes the Food Dataset from Open Food Facts

    def __init__(self, file_path: str = None):
        self.file_path = file_path
        self.data = None

    def load_sample_data(self) ->  pd.DataFrame:
        # This Creates a sample dataset that simulates Open Food facts' Data
        # In real life application, this would load from an actual dataset

        np.random.seed (42) # For Consistent results

        sample_size = 500
        data = {
            'product_name': [f'Product_{i}' for i in range (sample_size)],
            'energy kcal': np.random.uniform(50, 600, sample_size),
            'carbonhydrates_g': np.random.uniform(0, 100, sample_size),
            'sugars_g': np.random.uniform(0, 50, sample_size),
            'fat_g': np.random.uniform(0, 40, sample_size),
            'saturated_fat_g': np.random.uniform(0, 20, sample_size),
            'proteins_g': np.random.uniform(0, 30, sample_size),
            'fiber_g': np.random.uniform(0, 15, sample_size),
            'sodium_g': np.random.uniform(0, 2000, sample_size),
            'processed': np.random.uniform([True, False], sample_size, p=[0.6, 0.4])
        }

        self.data = pd.DataFrame(data)
        return self.data
    
    def preprocess_data (self, df: pd.DataFrame) -> pd.DataFrame:
        # This cleans and preprocesses the food dataset

        critical_columns = ['energy_kcal', 'sugars_g', 'proteins_g', 'fat_g', 'fiber_g']
        df.clean = df.dropna(subset=critical_columns)

        #This fills the missing columns with 0
        df_clean = df_clean.fillna(0)

        return df_clean