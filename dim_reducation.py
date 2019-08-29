import numpy as np
from sklearn.decomposition import PCA,KernelPCA,SparsePCA,TruncatedSVD,IncrementalPCA

class SingletonPCA:
    def __init__(self, *args, **kwargs):
        self.pc = PCA()
       
    def __new__(cls):        
        if not hasattr(cls,'instance'):
            cls.instance=super(SingletonPCA,cls).__new__(cls)
        return cls.instance

    @property
    def pca(self):
        return self.pc

    @pca.setter
    def pca(self,x):
        self.pc = IncrementalPCA()

class SingletonSparsePCA:
    def __init__(self, *args, **kwargs):
        self.pca = SparsePCA()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(SingletonSparsePCA,cls).__new__(cls)
        return cls.instance

    @property
    def sparse_pca(self):
        return self.pca

    @sparse_pca.setter
    def sparse_pca(self,x):
        self.pca = IncrementalPCA()

class SingletonTruncatedSVD:
    def __init__(self, *args, **kwargs):
        self.pca = TruncatedSVD()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(SingletonTruncatedSVD,cls).__new__(cls)
        return cls.instance

    @property
    def truncated_pca(self):
        return self.pca

    @truncated_pca.setter
    def truncated_pca(self,x):
        self.pca = IncrementalPCA()

class SingletonIncrementalPCA:
    def __init__(self, *args, **kwargs):
        self.pca = IncrementalPCA()

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance=super(SingletonIncrementalPCA,cls).__new__(cls)
        return cls.instance

    @property
    def incrementalpca(self):
        return self.incrementalpca

    @incrementalpca.setter
    def incrementalpca(self,x):
        self.pca = IncrementalPCA()

if __name__ == "__main__":
    incremental = SingletonIncrementalPCA()
    print(incremental.pca)