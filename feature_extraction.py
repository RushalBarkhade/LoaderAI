from sklearn.feature_extraction import DictVectorizer
import numpy as np
import pandas as pd

def drop(data,columns=None,axis=0,inplace=False):
    return data.drop(columns,axis=axis,inplace=inplace)

def dropna(data,axis=0,inplace=False):
    return data.dropna(axis=axis,inplace=inplace)

class SingletonDictVectorizer:
    def __init__(self, *args, **kwargs):
        self.vector = DictVectorizer()
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(SingletonDictVectorizer,cls).__new__(cls)
        return cls.instance

    @property.getter
    def vector(self):
        return self.vector
    
    def fit(self,x):
        self.vector.fit(x)

    def transform(self,x):
        return self.vector.transform(x)

    def fit_transform(self,x):
        self.vector.inverse_transform
        return self.vector.fit_transform(x)
    
    def inverse_transform(self,y):
       return  self.vector.inverse_transform(y)
