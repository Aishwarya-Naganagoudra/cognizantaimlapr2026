#create power analysis using medicine_effect 
import numpy as np
import pandas as pd
from distapp.configurations.config import Config
#power is assumed to be 0.8 and alpha is assumed to be 0.05
#def power_analysis(medicine_effect, alpha=0.05, power=0.8):


def calculate_medicine_effect(medicine_effect, control_effect):
    # Calculate the effect size (Cohen's d)
    effect_size = (medicine_effect - control_effect) / np.sqrt((medicine_effect + control_effect) / 2)
    return effect_size


if __name__ == "__main__":
    config = Config()
    df=pd.read_csv(config.effectiveness_path)
    medicine_effect_count = df['medicine_name']=='Metformin'.count()
    medicine_effect_mean= medicine_effect_count/len(df)
    control_effect_count = df['medicine_name']=='Glimepiride'.count()
    control_effect_mean= control_effect_count/len(df)
    effect_size = calculate_medicine_effect(medicine_effect_mean, control_effect_mean) 

    print(f"Medicine Effect Mean: {medicine_effect_mean}")
    print(f"Control Effect Mean: {control_effect_mean}")
    print(f"Effect Size (Cohen's d): {effect_size}") 



    