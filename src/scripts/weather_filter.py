import pandas as pd

# Load weather data
weather_df = pd.read_csv('/home/ctand/EnergyVision/data/raw/weather.csv')

weather_df['date'] = pd.to_datetime(weather_df['date'], utc=True)

weather_df['date'] = weather_df['date'].dt.tz_convert('America/Chicago')

weather_df['date'] = weather_df['date'].dt.tz_localize(None)

weather_df['hour'] = weather_df['date'].dt.hour  # Extract hour
weather_df['date'] = weather_df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')  # Keep format

for i in range(len(weather_df)):
    if weather_df.loc[i, 'hour'] == 0:
        prev_day = pd.to_datetime(weather_df.loc[i, 'date']) - pd.Timedelta(days=1)
        weather_df.loc[i, 'date'] = prev_day.strftime('%Y-%m-%d') + ' 24:00:00'

# Drop the extra 'hour' column
weather_df.drop(columns=['hour'], inplace=True)

# Verify changes
print(weather_df.head())

# Save the cleaned data
weather_df.to_csv('/home/ctand/EnergyVision/data/processed/weather_cleaned.csv', index=False)

