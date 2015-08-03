# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:48:16 2015

@author: Taikor
"""

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(
   {'host':'180.153.177.169', 'port':'9200'}
)

a = es.get(index="palas_v1", doc_type="items", id="45abd6cb4515b075998b48e50d9d26a8")