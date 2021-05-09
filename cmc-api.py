import requests
from requests import Session
import secret
from pprint import pprint as pp

# Documentation: https://coinmarketcap.com/api/documentation/v1/

# Test requests
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = { 
            'Accepts': 'application/json', 
            'X-CMC_PRO_API_KEY': secret.API_KEY,
          }
r = requests.get(url, headers=headers)
#r.status_code

# Build class for further REST API calls

class CMC:
      def __init__(self, token):
            self.apiurl = 'https://pro-api.coinmarketcap.com'
            self.headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
            self.Session = Session()
            self.session.headers.update(self.headers)
      
      def getAllCoins(self):
            url = self.apiurl + '/v1/cryptocurrency/map'
            r = self.session.get(url) 
            data = r.json()['data']
            return data
      
      #def getPrice(self, symbol):
        

cmc = CMC(secret.API_KEY)

pp(cmc.getAllCoins())
