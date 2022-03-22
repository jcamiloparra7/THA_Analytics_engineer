## Set up ---- Tries to import non built in packages, if theyre not part of the virtual env, then it installs them via Pip

import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])     

import_or_install('requests')


import requests
import csv
import os


## Retrieving data from the API, after that only assigning useful info.


response_API = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
brute_rates = response_API.json()[0]['rates']
datemark = response_API.json()[0]['effectiveDate']
processed_rates = {}

## Cleaning process -- Accessing only the useful data in our dictionaries and changing the strorage structure for future manipulation.

for dictionary in brute_rates:
    processed_rates.update({dictionary['code']: dictionary['mid']})


## Adding PLN exc rate and removing EUR, formating our watermark  

processed_rates.update({'PLN': 1})
eur_rate = processed_rates.pop('EUR')
processed_datemark = datemark.replace('-', '')

## Key process -- Transforming our exchange rates, for CSV functions input

csv_name = 'nbp_exchange_rates_' + processed_datemark + '.csv'
csv_headers = ['date', 'currency_code', 'euro_rate' , 'inverse']
csv_content = []

for c_code , rate in processed_rates.items():

    rate = round(eur_rate/rate, 4)
    inverse_rate = round(1/rate, 4)

    csv_content.append([processed_datemark, c_code, rate, inverse_rate])


## Writing of CSV file

with open(csv_name, 'w', newline= '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_headers)
    writer.writerows(csv_content)

path = os.path.dirname(os.path.realpath(__file__))
print('-------Succesful process ------\n' + csv_name + ' has been generated inside ' + path)
