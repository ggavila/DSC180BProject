import os
import sys
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

def top_1000():
    '''
    get top 1000 articles of COVID in wikipedia from 2020/1/1 to 2020/12/31
    '''
    url="https://en.wikipedia.org/wiki/Wikipedia:WikiProject_COVID-19/Popular_pages"
    response=requests.get(url)
    page=BeautifulSoup(response.text, 'html.parser')
    table=page.find_all('table')[3]
    readable=pd.read_html(table.prettify())
    readable[0].to_csv("data/raw/top1000.csv", index=False)
    return

def api_getpageview(article):
    '''
    Using GET method to get pageview data since 2020010100 (2020/1/1) to 2020123100 (2020/12/31)

    article: The article we are looking for
    category: Type of data get

    return: A csv contained information
    '''
    url="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{0}/daily/2020010100/2020123100".format(article)
    response=requests.get(url)

    return
