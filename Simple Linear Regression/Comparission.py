import numpy as np
from sklearn.linear_model import LinearRegression
from SimpleLinearRegression import SLR

xtrain=np.array([651,762,856,1063,1190,1298,1421,1440,1518]).reshape(-1,1)
ytrain=np.array([23,26,30,34,43,48,52,57,58]).reshape(-1,1)
xtest=np.array([641,1024]).reshape(-1,1)

model=LinearRegression()
model.fit(xtrain,ytrain)
print(model.coef_)
pred_ideal=model.predict(xtest)

xtrain=[651,762,856,1063,1190,1298,1421,1440,1518]
ytrain=[23,26,30,34,43,48,52,57,58]
xtest=[641,1024]
model=SLR()
model.fit(xtrain,ytrain)
model.print_coeff()
pred_my=model.predict(xtest)