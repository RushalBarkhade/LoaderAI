from abc import ABC,abstractmethod
import data_conversion
import dim_reducation
import feature_extraction

class AbstractLoader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def __getItem__(self,pos):
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

        assert data!=None,"data can`t be None"
        assert isinstance(dim_reduce,(list,dict)),"dim_reduce can be list or dict"
        assert isinstance(feat_extract,(list,dict)),"feat_extract can be list or dict"

        if isinstance(data,(list,tuple,dict)):
            self.data = data_conversion.data_converter(data)
        self.dim_reduce = dim_reduce
        self.feat_extract = feat_extract

    def __getItem__(self,pos):
        item = self.data[pos]
        return item
    
    def __len__(self):
        return len(self.data)

if __name__ == "__main__":
    number = NumberLoader(['rushal'])
