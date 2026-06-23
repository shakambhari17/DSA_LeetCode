import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter where referee_id is not 2 OR referee_id is NaN (null)
    filtered_df = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isna())]
    
    # Return only the 'name' column as a DataFrame
    return filtered_df[['name']]