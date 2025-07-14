import pandas as pd

def compute_metrics(df):
    # Clean up any extra spaces or hidden characters
    df.columns = df.columns.str.strip()

    # Rename for consistency
    df = df.rename(columns={
        'Timestamp': 'Date',
        'Production Output (Units)': 'Units_Produced',
        'Energy Consumption (kWh)': 'Energy_Used',
        'Defect Rate (%)': 'Defect_Rate'
    })

    # Convert date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    # Calculate defect count from defect rate
    df['Defect_Count'] = (df['Defect_Rate'] / 100) * df['Units_Produced']

    # Estimate cost
    df['Cost'] = df['Energy_Used'] * 0.15

    # Calculate efficiency
    df['Energy_Efficiency'] = df['Units_Produced'] / df['Energy_Used']

    # Group by month
    summary = df.groupby('Month').agg({
        'Units_Produced': 'sum',
        'Defect_Count': 'sum',
        'Energy_Used': 'sum',
        'Cost': 'sum',
        'Defect_Rate': 'mean',
        'Energy_Efficiency': 'mean'
    }).reset_index()

    return summary
