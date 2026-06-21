import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # 1. Left join Employee with Bonus on 'empId'
    merged_df = pd.merge(employee, bonus, on='empId', how='left')
    
    # 2. Filter rows where bonus is < 1000 OR is NaN (missing)
    filtered_df = merged_df[(merged_df['bonus'] < 1000) | (merged_df['bonus'].isna())]
    
    # 3. Return only the required columns
    return filtered_df[['name', 'bonus']]