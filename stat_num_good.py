import os
from functools import reduce
import json
from os import listdir
from os.path import isfile, join
from collections import defaultdict
import glob
import numpy as np

memes_path = "dataset/memes/*"
files = glob.glob(memes_path)
ave_list = np.zeros(99)


for i in range (0, len(files)):

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
print(ave_list_bi)
