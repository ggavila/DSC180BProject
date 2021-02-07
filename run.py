#! /usr/bin/env python

import sys
import json
import pandas as pd
from etl import *
from eda import *

def main(targets):
    if 'data' in targets:
        
      with open('config/data-params.json') as fh:
        data_cfg=json.load(fh)
        
      top_1000()
      pageview_csv(data_cfg['articles'], data_cfg['pageview'])
    if 'eda' in targets:
         
      with open('config/data-params.json') as fh:
        data_cfg=json.load(fh)
      router=get_dfs(data_cfg['pageview'])
      top10er=get_top_10_average_daily_view(router, data_cfg['eda'])
      plot_top10(top10er, router, data_cfg['eda'])
    if 'test' in targets:
      pageview_csv("test/test.csv", "test/pageview")
      router=get_dfs('test/pageview')
      top10er=get_top_10_average_daily_view(router,'test/eda')
      plot_top10(top10er,router,'test/eda')

    return






if __name__ == "__main__":
    targets=sys.argv[1: ]
    main(targets)