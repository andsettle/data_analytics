# Import requests and pandas libraries
import requests
import pandas as pd
import osascript
import time
import subprocess

# Define the request URL
request_url = "https://api.resumatorapi.com/v1/applicants/from_apply_date/2023-03-01/to_apply_date/2023-03-31"

# Define the API key
api_key = "{REDACTED}"

# Initialize an empty data frame
data_frame = pd.DataFrame()

# Initialize a counter variable for the page number
page = 1

# Initialize a flag variable for the loop condition
has_more_data = True

# Loop until there is no more data
while has_more_data:
    # Append the page number and the API key to the request URL
    url = request_url + f"/page/{page}" + api_key
    # Send a GET request to the URL and store the response
    response = requests.get(url)
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Convert the response JSON data to a pandas data frame
        temp_df = pd.DataFrame(response.json())
        # Check if the data frame is empty
        if temp_df.empty:
            # Set the flag to False to exit the loop
            has_more_data = False
            # Print a message that all records have been appended
            osascript.run(f'display notification "All records have been appended and exported to excel, good luck!" with title "Luke Fetcher"')
        else:
            # Append the data frame to the main data frame
            data_frame = pd.concat([data_frame, temp_df], ignore_index=True)
            # Increment the page number by 1
            page += 1
            # Print a message that the current page is being appended
            print(f"Appending page {page} to results...")
    else:
        # Print an error message and exit the loop
        print(f"Request failed with status code {response.status_code}")
        has_more_data = False

# Save the data frame as a csv file
data_frame.to_excel("mar_applicants.xlsx", index=False)
subprocess.run(["open", "mar_applicants.xlsx"])