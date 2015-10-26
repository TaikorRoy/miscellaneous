# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:48:16 2015

@author: Taikor
"""

from datetime import datetime
from elasticsearch import Elasticsearch
import json
import requests

"""
es = Elasticsearch(
   [{'host':'180.153.177.169', 'port':'9200'}]
)

a = es.search(index="palas_v1", body={"issueID": "Reader", "pubDate":"2015-08-12"}, size=10)
"""

url = "http://tank.palaspom.com:9200/palas_v1/_search"
query = {"query":{"bool":{"must":[{"query_string":{"default_field":"items.analyzeData.issueID","query":"Reader"}},{"range":{"items.pubDate":{"from":"2015-08-21T00:00:01+08:00","to":"2015-08-21T10:00:00+08:00"}}}],"must_not":[],"should":[]}},"from":n,"size":25,"sort":[],"facets":{}}
r = requests.post(url, data=json.dumps(query))
obj = json.loads(r.text)


            
        
        
    
        
    


