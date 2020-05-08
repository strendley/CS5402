#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:33:16 2020

@author: user
"""

import os
import glob
import pandas as pd

# Move to the path that holds our CSV files
csv_file_path = 'processed-data/'
os.chdir(csv_file_path)

ext = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(ext))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_files])
combined_csv.rename(columns={"0":"text", "1":"id", "2":"subreddit", "3":"meta", "4":"time", "5":"author", "6":"ups", "7":"downs", "8":"authorlinkkarma", "9":"authorkarma", "10":"authorisgold"}, inplace=True)

combined_csv.to_csv("combined_csv.csv",index=False,encoding='utf-8-sig')