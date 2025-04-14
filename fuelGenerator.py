import pandas as pd
import pickle

# Load the CSV file into a DataFrame
df = pd.read_csv('final2_with_fuel_efficiency.csv')

# Extract the required columns (Latitude, Longitude, and Fuel Efficiency Score)
data_to_save = df[['Latitude', 'Longitude', 'fuel_efficiency']]

# Save the extracted columns to a .pkl file
with open('latitude_longitude_fuel_efficiency.pkl', 'wb') as f:
    pickle.dump(data_to_save, f)

print("Data has been saved to latitude_longitude_fuel_efficiency.pkl")
