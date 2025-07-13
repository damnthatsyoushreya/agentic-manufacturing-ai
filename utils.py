import pandas as pd

def compute_metrics(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    df['Defect_Rate'] = df['Defect_Count'] / df['Units_Produced']
    df['Energy_Efficiency'] = df['Units_Produced'] / df['Energy_Used']

    summary = df.groupby('Month').agg({
        'Units_Produced': 'sum',
        'Defect_Count': 'sum',
        'Energy_Used': 'sum',
        'Cost': 'sum',
        'Defect_Rate': 'mean',
        'Energy_Efficiency': 'mean'
    }).reset_index()

    return summary
