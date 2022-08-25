import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
plt.style.use('bmh')


df = pd.read_csv("data.csv",index_col=[0])
df.index = pd.to_datetime(df.index)
print (df.head)


print (df.shape)

#df = df[['Close']]
#print ("head",df.head(5))


df.Close.plot(figsize=(15,7))
plt.xlabel('Date')
plt.ylabel('NIFTY50 Closing price INR')
plt.title('NIFTY50 index ')
#plt.grid()
plt.plot(df['Open'])
#plt.show()



#Create a variable to pridict 'x' days out into the future
future_days = 1

#create a new column(target data) shifted 'x' units/days up
df['Prediction']=df[['Open']].shift(-future_days)
print (df.head(5))


#Creat the feature data set X and convert it to a numpy array and remove last 'x' rows/days
X = np.array(df.drop(['Prediction'],1))[:-future_days]
print (X)

#Create the target data set (y) and convert it to numpy array get all of the target values except last 'x' rows/days
y = np.array(df['Prediction'])[:-future_days]
print (y)

#Split the data into 75% training and 25% testing
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

#Create models
#Create the decision tree regressor model
tree = DecisionTreeRegressor().fit(x_train,y_train)
#Create the linear regression model
lr = LinearRegression().fit(x_train,y_train)

#Get the last 'x' rows of the feature data set
x_future = df.drop(['Prediction'],1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
print (x_future)


#show the model tree prediction
tree_prediction = tree.predict(x_future)
print("tree model prediction",tree_prediction)
print("====\n")

#Show the model linear regression prediction
lr_prediction = lr.predict(x_future)
print ("linear model prediction",lr_prediction)




#Visualize the data
predictions = tree_prediction

valid = df[X.shape[0]:]
valid['Prediction'] = predictions

'''
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price INR')
plt.plot(df['Close'])
plt.plot(valid['Close','Prediction'])
plt.legend(['Orig','Val','Pred'])
plt.show()


#Visualize the data
predictions = lr_prediction

valid = df[X.shape[0]:]
valid['Prediction']=predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Days')
plt.ylabel('Close Price INR')
plt.plot(df['Close'])
plt.plot(valid['Close','Prediction'])
plt.legend(['Orig','Val','Pred'])
plt.show()

'''








