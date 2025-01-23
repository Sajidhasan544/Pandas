import pandas as pd

x = [3,4,6,2]

var = pd.Series(x)
print(var)
print(type(var))
print(var[2])



var = pd.Series(x,index=["a", "b", "c","d"])
print(var)
print(var["a"])

var = pd.Series(x,index=["a", "b", "c","d"],dtype="float")
print(var)
print(var["a"])

var = pd.Series(x,index=["a", "b", "c","d"],dtype="float",name="numbers")
print(var)
print(var["a"])

dic = {"names":["python","c","c++","java"],"rank":[1,4,2,3] ,"poor":[12,432,54,654]}

var = pd.Series(dic)

print(var)