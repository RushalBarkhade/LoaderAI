import pandas as pd
from abc import ABC,abstractmethod
import data_conversion
import dim_reducation
import feature_extraction

class AbstractLoader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __getitem__(self,pos):
        pass

    @abstractmethod
    def __len__(self):
        pass

class NumberLoader(AbstractLoader):
    def __init__(self,data,variable_type="discate",dim_reduce=None,feat_extract=None):
        """
        variable_type:is two types discrate or continuous type
                      default value is discate
        data:can be list,tuple,dict,series,dataFrame
        dim_reduce:can be list or dict
        feat_extract:can be list or dict
        """   
        if dim_reduce!=None:
            assert isinstance(dim_reduce,(list,dict)),"dim_reduce can be list or dict"
            self.dim_reduce = dim_reduce
        if feat_extract!=None:     
            assert isinstance(feat_extract,(list,dict)),"feat_extract can be list or dict"
            self.feat_extract = feat_extract
        if isinstance(data,(list,tuple,dict,pd.Series,pd.DataFrame)):
            self.data = data_conversion.data_converter(data)
   
    def __getitem__(self,pos):
        item = self.data[pos] 
        

        return item
    
    def __len__(self):
        return len(self.data)

if __name__ == "__main__":
    number = NumberLoader(['rushal'])
