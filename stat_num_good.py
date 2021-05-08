import os
from functools import reduce
import json
from os import listdir
from os.path import isfile, join
from collections import defaultdict
import glob
import numpy as np
import pandas as pd


memes_path = "dataset/memes/*"
files = glob.glob(memes_path)
ave_list = np.empty((99,1))
img_path_list = np.empty((99,1), dtype=object)
img_name_list = np.empty((99,1), dtype=object)

for i in range (0, len(files)):
    img_name = files[i].replace("dataset/memes/","").replace(".json","")
    if img_name == "Tuxedo-Winnie-The-Pooh":
        img_path = img_name + ".png"
    else:
        img_path = img_name + ".jpg"
    img_name_list[i] = img_name
    img_path_list[i] = img_path
    json_open = open(files[i], 'r') #replace 0 with i in a for loop
    json_load = json.load(json_open)
    num_of_memes = len(json_load)
    sum_good = 0
    num_good = 0

    for j in range(0, num_of_memes):
        if json_load[j]['metadata']['img-votes'] == 0:
            num_good = 0
        else:
            if "," in json_load[j]['metadata']['img-votes']:
                num_good = int(json_load[j]['metadata']['img-votes'].replace(",",""))
            else:
                num_good = int(json_load[j]['metadata']['img-votes'])
        sum_good += num_good

    ave_good = sum_good / num_of_memes
    ave_list[i] = ave_good

#print(ave_list)
ave_list_bi = ave_list / max(ave_list)
#print(ave_list_bi)
#print(img_path_list)

csv_num = np.concatenate([img_name_list, img_path_list, ave_list_bi], axis=1)
#print(csv_num)

df = pd.DataFrame(csv_num, columns = ['img_name', 'img_path', 'ave_score'])
print(df)
df.to_csv('data.csv')