import os
import json
import pandas as pd

dir_path = os.path.dirname(__file__)

with open(dir_path + '/logo_extract.json') as f1:
    data1 = json.load(f1)

with open(dir_path + '/address_extract.json') as f2:
    data2 = json.load(f2)

with open(dir_path + '/phone_extract.json') as f3:
    data3 = json.load(f3)

df1 = pd.DataFrame([data1])
df2 = pd.DataFrame([data2])
df3 = pd.DataFrame([data3])


MergeJson = pd.concat([df1, df2, df3], axis=1)

MergeJson.to_json(dir_path + "/merge_json.json")
