import os
import sys
import json
import requests
import pandas as pd

def api_getpageview(article):
    '''
    Using GET method to get pageview data since 2020010100 (2020/1/1) to 2020123100 (2020/12/31)

    article: The article we are looking for
    category: Type of data get

    return: A csv contained information
    '''
    url="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{1}/daily/2020010100/2020123100".format(article)
    response=requests.get(url)

    return