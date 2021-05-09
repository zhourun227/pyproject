import pandas as pd
s = pd.Series([7,-3,4,-2])
print(s)
data = {'state': ['beijing', 'beijing', 'beijing', 'shanghai', 'shanghai', 'shanghai'],
        'year':[2000, 2001, 2002, 2001, 2002, 2003],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
data=pd.DataFrame(data)
f2 = pd.DataFrame(data, columns=['year','state','pop'],index=['a','b','c','d','e','f'])
print(data)
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj)
print(data.iloc[0:4,:])