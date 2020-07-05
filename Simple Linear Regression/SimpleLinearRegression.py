import numpy as np
from math import sqrt
class SLR:
    
    def fit(self,x,y):
        xbar=np.mean(x)
        ybar=np.mean(y)
        sx=0
        sy=0
        sxy=0
        for i in range(len(x)):
            sxy+=(x[i]-xbar)*(y[i]-ybar)
            sx+=(x[i]-xbar)**2
            sy+=(y[i]-ybar)**2
            
        self.r=sxy/sqrt(sx*sy)
        self.slope=self.r*(np.std(y)/np.std(x))
        self.intercept=ybar-(self.slope*xbar)
    
    def predict(self,x):
        preds=[]
        for i in x:
            preds.append(self.intercept+(self.slope*i))
        return preds
    
    def print_coeff(self):
        
        print('Pearsons Corelation coefficient: ',self.r)
        print('Slope: ',self.slope)
        print('Y Intercept: ',self.intercept)