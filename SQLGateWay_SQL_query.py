'''
Created on Sep 27, 2017

@author: lauthjo
'''


import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name
from bs4.builder._htmlparser import BeautifulSoupHTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen

class SQLGatewaySQLQuery(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('oneagent_sdk.demo_app'))
        pgi_id = pgi.group_instance_id
        
        url = "http://localhost:8080/SQL%20GateWay/SQLGatewayServlet"
        
        payload = "sqlStatement=select%20count(*)%20from%20test"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        
        
                
     #   self.results_builder.absolute(key='random', value=stats['random'], entity_id=pgi_id)
     #   self.results_builder.relative(key='counter', value=stats['counter'], entity_id=pgi
     