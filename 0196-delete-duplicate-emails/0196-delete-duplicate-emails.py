import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # 1. Sort by id in ascending order to ensure the smallest id comes first
    person.sort_values(by='id', ascending=True, inplace=True)
    
    # 2. Drop duplicates based on the 'email' column, keeping the first occurrence
    # 'inplace=True' modifies the original DataFrame as required by the problem
    person.drop_duplicates(subset='email', keep='first', inplace=True)