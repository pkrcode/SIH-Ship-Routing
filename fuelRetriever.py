import pickle
import pandas as pd

class FuelEfficiencyRetriever:
    def __init__(self, pkl_file='latitude_longitude_fuel_efficiency.pkl'):
        # Load the data once during initialization
        with open(pkl_file, 'rb') as f:
            self.data = pickle.load(f)

    def retrieve_fuel_efficiency(self, longitude, latitude):
        # Filter the data based on the provided longitude and latitude
        result = self.data[(self.data['Longitude'] == longitude) & (self.data['Latitude'] == latitude)]

        # Return the fuel efficiency score or a default value (e.g., 0) if not found
        if not result.empty:
            return result['fuel_efficiency'].values[0]
        else:
            return 0  # Default value if coordinates are not found

# Example usage
retriever = FuelEfficiencyRetriever()  # Load the pickle file only once
fuel_efficiency_score = retriever.retrieve_fuel_efficiency(68.875, 12.25)  # Example coordinates
print("Fuel Efficiency Score:", fuel_efficiency_score)
