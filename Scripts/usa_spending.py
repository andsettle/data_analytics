import requests

url = 'https://www.usaspending.gov'
agency_codes = {
    'Department of Agriculture (USDA)': '12',
    'Department of Commerce (DOC)': '13',
    'Department of Defense (DOD)': '97',
    'Department of Education (ED)': '91',
    'Department of Energy (DOE)': '89',
    'Department of Health and Human Services (HHS)': '75',
    'Department of Homeland Security (DHS)': '70',
    'Department of Housing and Urban Development (HUD)': '86',
    'Department of the Interior (DOI)': '14',
    'Department of Justice (DOJ)': '15',
    'Department of Labor (DOL)': '16',
    'Department of State (DOS)': '19',
    'Department of Transportation (DOT)': '69',
    'Department of the Treasury (Treasury)': '20',
    'Department of Veterans Affairs (VA)': '36'
    }

award_endpoint = f"/api/v2/agency/{agency_codes['Department of Defense (DOD)']}/awards/"
get_dod_awards = "https://usaspending.gov/api/v2/agency/097/object_class/"

response = requests.get(get_dod_awards)
print(response.text)