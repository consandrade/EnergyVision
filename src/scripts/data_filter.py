import pandas as pd

# Load the CSV file
df = pd.read_csv('/home/ctand/EnergyVision/data/raw/energy_consumption.csv')

# Create a new DataFrame with only the "Hour Ending" and "COAST" columns
coastal_df = df[['Hour Ending', 'COAST']].copy()

# Ensure 'Hour Ending' is treated as a string
coastal_df['Hour Ending'] = coastal_df['Hour Ending'].astype(str)

# Remove " DST" from timestamps if present
coastal_df['Hour Ending'] = coastal_df['Hour Ending'].str.replace(' DST', '', regex=False)

# Identify rows with '24:00' and adjust them before conversion
mask = coastal_df['Hour Ending'].str.endswith(' 24:00')

# Convert '24:00' to '00:00' and shift date forward by one day
coastal_df.loc[mask, 'Hour Ending'] = (
    coastal_df.loc[mask, 'Hour Ending'].str.replace(' 24:00', ' 00:00', regex=False)
)

# Convert to datetime format
coastal_df['Hour Ending'] = pd.to_datetime(coastal_df['Hour Ending'], format='%m/%d/%Y %H:%M', errors='coerce')

# Check if there were any issues with conversion (NaT means Not a Time)
if coastal_df['Hour Ending'].isna().any():
    print("There were issues with some timestamp conversions!")
    print(coastal_df[coastal_df['Hour Ending'].isna()])

# Handle '24:00' adjusted rows by adding 1 day
coastal_df.loc[mask, 'Hour Ending'] = coastal_df.loc[mask, 'Hour Ending'] + pd.Timedelta(days=1)

# Subtract 1 hour to get the correct "Hour Ending" time
coastal_df['date'] = coastal_df['Hour Ending'] - pd.Timedelta(hours=1)

# Format 'Date' as 'YYYY-MM-DD HH:MM:SS'
coastal_df['date'] = coastal_df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Remove commas and convert 'COAST' column to float
coastal_df['COAST'] = coastal_df['COAST'].str.replace(',', '', regex=False).astype(float)

# Drop the old 'Hour Ending' column
coastal_df = coastal_df.drop(columns=['Hour Ending'])

# Save to a new CSV file
coastal_df.to_csv('/home/ctand/EnergyVision/data/processed/COASTCONSUMPTION.csv', index=False)

# Display the new DataFrame
print(coastal_df.head())



