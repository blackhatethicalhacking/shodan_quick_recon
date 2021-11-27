import shodan
import time
import requests
import re

# Enter Your shodan API key
SHODAN_API_KEY = 'INSERT_MY_API_HERE'
api = shodan.Shodan(SHODAN_API_KEY)
#Function that uses search from keywords
try:
        # Search Shodan
        results = api.search('apache')

        # Print the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError, e:
        print('Error: {}'.format(e))
#Written by Black Hat Ethical Hacking - blackhatethicalhacking.com
