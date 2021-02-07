#! /usr/bin/env python

import sys
import json
import pandas as pd
from etl import *


def main(targets):
    if 'data' in targets:
        
      with open('config/data-params.json') as fh:
        data_cfg=json.load(fh)
        
      top_1000()
      pageview_csv(data_cfg['articles'], data_cfg['data/pageview'])
    if 'test' in targets:
      pageview_csv("test/test.csv", "test/pageview")

    return






if __name__ == "__main__":
    targets=sys.argv[1: ]
    main(targets)