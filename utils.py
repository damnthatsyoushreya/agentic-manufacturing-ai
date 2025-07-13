import pandas as pd

def compute_metrics(df):
    # Clean column names
    df.columns = df.columns.str.strip()  # 🔥 removes extra spaces

    # Rename columns for consistency
    df = df.rename(columns={
        'Timestamp': 'Date',
        'Production Output (Units)': 'Units_Produced',
        'Energy Consumption (kWh)': 'Energy_Used',
        'Defect Rate (%) ': 'Defect_Rate'  # <-- make sure this matches your CSV exactly
    })

    # Convert data types
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    # Convert defect rate (%) to actual count
    df['Defect_Count'] = (df['Defect_Rate'] / 100) * df['Units_Produced']

    # Estimate cost
    df['Cost'] = df['Energy_Used'] * 0.15  # Rs. 0.15 per kWh

    # Calculate energy efficiency
    df['Energy_Efficiency'] = df['Units_Produced'] / df['Energy_Used']

    # Group by Month
    summary = df.groupby('Month').agg({
        'Units_Produced': 'sum',
        'Defect_Count': 'sum',
        'Energy_Used': 'sum',
        'Cost': 'sum',
        'Defect_Rate': 'mean',
        'Energy_Efficiency': 'mean'
    }).reset_index()

    return summary
