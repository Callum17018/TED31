import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

"""
This program gets data from a google sheet then writes it as json to a file

For example if you create a colum on the google sheets called numbers then filled
the colum with random numbers the json file will then have an object called numbers with 
the numbers inside of it

© Copyright 2021 Callum Rutledge
"""


def download_data():
    '''
    Downloads the data from the google sheet and sets it to the data.txt file
    :return: None
    '''
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1DTzCqp0TnrJeACw-30bNIUXyzCm4wtNq63-yk8BGdnQ/edit#gid=950405584").worksheet("Sheet2")

    # Extract and print all of the values
    list_of_hashes = sheet.get_all_records()
    list_of_hashes = sheet.get_all_values()
    print(list_of_hashes)
    with open('data.txt', 'w') as outfile:
        json.dump(list_of_hashes, outfile)

download_data()