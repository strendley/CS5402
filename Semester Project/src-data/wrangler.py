from os import listdir
import pandas as pd
import numpy as np
data_files = []
dataframes = []
df = pd.DataFrame()
data_dir = "src-data"
out_dir = data_dir + "/out"
for filename in listdir(data_dir):
    has_idx = True
    file_list = filename.split('.')
    if(len(file_list) > 1):
        if filename.split('.')[1] == 'csv':
            data_files.append(filename)
            df_temp = (pd.read_csv(data_dir + '/' + filename))
            df_temp.drop([0], inplace=True)
            df_temp.drop(columns="Unnamed: 0", inplace=True)
            #There may be a more elegant way to do this check but this will suffice.
            for idx,row in enumerate(df_temp['0']):
                if(row != idx):
                    has_idx = False
            if(has_idx == True):
                #There may also be a more elegant way to do this rename.
                df_temp.rename(columns={"1":"text", "2":"id", "3":"subreddit", "4":"meta", "5":"time", "6":"author", "7":"ups", "8":"downs", "9":"authorlinkkarma", "10":"authorkarma", "11":"authorisgold"}, inplace=True)
                df_temp.drop(columns="0")
            df_temp.rename(columns={"0":"text", "1":"id", "2":"subreddit", "3":"meta", "4":"time", "5":"author", "6":"ups", "7":"downs", "8":"authorlinkkarma", "9":"authorkarma", "10":"authorisgold"}, inplace=True)
            df_temp.to_csv(out_dir + '/' + filename, index=False)
            dataframes.append(df_temp)