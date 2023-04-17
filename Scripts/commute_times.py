import googlemaps
import pandas as pd

# Replace YOUR_API_KEY with your actual API key
gmaps = googlemaps.Client(key='{REDACTED}')

# Read the Excel file into a pandas dataframe
df = pd.read_excel('address.xlsx')

# Define the destination address
destination = '{REDACTED}'

# Define a function to calculate the commute time


def get_commute_time(row):
    origin = (row['Latitude'], row['Longitude'])
    result = gmaps.directions(origin, destination, mode='driving', departure_time='now')
    return result[0]['legs'][0]['duration']['text']

# Apply the function to each row in the dataframe


df['Commute Time'] = df.apply(get_commute_time, axis=1)

# Save the results to a new Excel file
df.to_excel('Commerce.xlsx', index=False)

# Print Complete
print("File has been saved!")
