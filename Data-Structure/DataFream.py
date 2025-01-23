import pandas as pd

x = {"a":[1,2,3,4],"b":[1,2,3,4],"c":[1,2,3,4]}
var =  pd.DataFrame(x)
print(var)

x = {"a":[1,2,3,4],"b":[1,2,3,4],"c":[1,2,3,4]}
var =  pd.DataFrame(x,columns=["a","b"])
print(var)


x = {"a":[1,2,3,4],"b":[1,2,3,4],"c":[1,2,3,4]}
var =  pd.DataFrame(x,columns=["a","b"],index=(1,2,3,4))
print(var)


print(var["a"][2])


d = {"s":pd.Series([1,2,3,4]),"d":pd.Series([1,2,3,3])}
var = pd.DataFrame(d)

print(var)