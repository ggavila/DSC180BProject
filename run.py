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
      tops=pd.read_csv(data_cfg['articles'])['Page title'].values
      for i in tops:
        print(i)
    return






if __name__ == "__main__":
    targets=sys.argv[1: ]
    main(targets)