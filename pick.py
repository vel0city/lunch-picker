import random
import requests
import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=os.getenv('CONSUMER_KEY'),
    consumer_secret=os.getenv('CONSUMER_SECRET'),
    token=os.getenv('TOKEN'),
    token_secret=os.getenv('TOKEN_SECRET')
)

client = Client(auth)
params = {
    'radius_filter': int(os.getenv('SEARCH_RADIUS')),
    # Need to offset as it only returns a max of 20 results.
    'offset': random.randint(0, int(os.getenv('SEARCH_OFFSET')))
}

with open('categories', 'r') as c:
    params['categories'] = c.read()
categories = params['categories'].replace('\n', ',')

response = client.search_by_coordinates(float(os.getenv('SEARCH_LAT')), float(os.getenv('SEARCH_LONG')), **params)
choices = response.businesses
choice = random.choice(choices)

# Trim query params from the URL
url = choice.url.split('?')[0]

with open('drivers', 'r') as f:
    drivers = f.readlines()

body = {'message': u'THE PEOPLE\'S LUNCH will be {}.\n{} has been chosen to drive.\n{}'
    .format(choice.name, random.choice(drivers).strip(), url), 'message_format': 'text', 'color': 'yellow',
        'notify': True}
requests.post(os.getenv('HIPCHAT_URL'), body)
