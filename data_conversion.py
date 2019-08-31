import numpy as np 
import pandas as pd

def data_converter(data):
    #assert data!=None,"Data can not be None"
    if type(data)==list:
        return list2numpy(data)
    elif type(data)==tuple:
        return tuple2numpy(data)
    elif type(data)==dict:
        return dict2numpy(data)
    elif type(data)==pd.DataFrame:
        return dataframe2dict(data)
    elif type(data)==pd.Series:
        return series2numpy(data)

def series2numpy(data):
    return np.array(data)

def dataframe2dict(data):
    return {i:np.array(data[i]) for i in data.columns}

def dict2dataframe(data):
    return pd.DataFrame(data)

def list2series(data):
    return pd.Series(data)

def dict2numpy(data):
    return {key:np.array(data[key]) for key in data.keys()}

def list2numpy(data):
    return np.array(data)

def tuple2numpy(data):
    return np.array(data)

if __name__ == "__main__":
    name = {"a":[12,3,6,45,6],"b":[1,2,4,3,6,7]}
    print({x:np.array(name[x]) for x in name.keys()})