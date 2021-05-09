'''
import pandas as pd


data=pd.read_csv("D:\\pythontrst\\titanic.csv",encoding='ISO-8859-1')

x=data[['pclass', 'age', 'sex']]
y=data['survived']

x['age'].fillna(x['age'].mean(), inplace=True)   #处理缺失值
'''
import json
obj = json.loads('{"id":"1"}')
print(json.loads('{"id":"1"}'))

j=json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(j)

import pandas as pd
import json

from pandas.io.json import json_normalize

#转换json
data=pd.read_csv("E:\\NIFI\\nifi-1.12.1-bin\\input\\mytest\\titanic.csv",encoding='ISO-8859-1')
data1=data.head(20)
#print(data1)
#data1=pd.DataFrame(data)
#print(data1)
data_new=data1.to_json(orient='records')
print(data_new)

#转换为dataframe
data_str = open('E:\\NIFI\\nifi-1.12.1-bin\\input\\mytest1\\songs.json').read()
df = pd.read_json(data_str,orient = 'records')
print(df.head())

'''
data_str = open('E:\\NIFI\\nifi-1.12.1-bin\\input\\mytest1\\songs.json').read()
data_list = json.loads(data_str)
df_1 = json_normalize(data_list)
#print(df_1.head())
'''