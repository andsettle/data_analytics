import pandas as pd
from geopy.geocoders import Nominatim

# Read the Excel file into a pandas dataframe
df = pd.read_excel('address.xlsx')

# Create a geocoder instance
geolocator = Nominatim(user_agent='get_coords')

# Loop through the addresses and get the coordinates
for i, address in enumerate(df['Address']):
    location = geolocator.geocode(address)
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        # Update the dataframe with the coordinates
        df.at[i, 'Latitude'] = latitude
        df.at[i, 'Longitude'] = longitude

# Write the updated dataframe back to the Excel file
df.to_excel('address.xlsx', index=False)
