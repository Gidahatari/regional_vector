from numpy import genfromtxt
mis_datos = genfromtxt('Variables_Climaticas.csv', delimiter=',')
mis_datos_corr = mis_datos[1:,:]
mis_datos_corr
from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit(mis_datos_corr[:,1:],mis_datos_corr[:,:1])
clf.coef_
clf.intercept_
clf.predict(mis_datos_corr[:,1:])





