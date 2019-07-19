# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler as mini
from sklearn.model_selection import train_test_split
data = pd.read_csv('data/BTC-USD.csv')
df0,df1 = data.shape[0], data.shape[1]
print('Bitcoin Data Has {} Transactions with {} features'.format(df0,df1))
data= data.drop(['Date'], axis =1)
data = data.drop('Adj Close',axis=1)
#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.
X= data.drop(['High'],axis=1)
y= data['High']
mini = mini()
X = mini.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X_train, y_train)

# Saving model to disk
pickle.dump(regressor, open('models/bit_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/bit_model.pkl','rb'))
future_x = X
X = X[3283:3290]
# future_x = X[-1]
# x = X[:-1]
bata = pd.read_csv('data/BTC-USD.csv')
date = bata['Date']
date = date[3289:3290]
print(date)
bata = pd.read_csv('data/BTC-USD.csv')
date = bata['Date']
print('PREDICTED HIGH')
y = model.predict(future_x)
print(y[3289:3290])




eth_data = pd.read_csv('data/ETH-USD.csv')
df0,df1 = eth_data.shape[0], eth_data.shape[1]
print('{} dates'.format(df0))
eth_data= eth_data.drop(['Date'], axis =1)
eth_data = eth_data.drop('Adj Close',axis=1)
eth_X= eth_data.drop(['High'],axis=1)
eth_y= eth_data['High']
eth_X = mini.fit_transform(eth_X)
eth_X_train,eth_X_test,eth_y_train,eth_y_test = train_test_split(eth_X,eth_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(eth_X_train, eth_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/eth_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/eth_model.pkl','rb'))
eth_future_x = eth_X
eth_X = eth_X[1436:1443]
    # future_x = X[-1]
    # x = X[:-1]
eth_bata = pd.read_csv('data/ETH-USD.csv')
eth_date = eth_bata['Date']
eth_date = eth_date[1442:1443]
print(eth_date)
eth_bata = pd.read_csv('data/ETH-USD.csv')
eth_date = eth_bata['Date']
print('PREDICTED HIGH')
eth_y = model.predict(eth_future_x)
print(eth_y[1442:1443])
eth_y = model.predict(eth_future_x)
print(eth_y[1442:1443])

eth_output =eth_y[1442:1443]

AAPL_data = pd.read_csv('data/AAPL.csv')
df0,df1 = AAPL_data.shape[0], AAPL_data.shape[1]
print('{} dates'.format(df0))
AAPL_data = AAPL_data.fillna(28.630752329973255)
AAPL_data= AAPL_data.drop(['Date'], axis =1)
AAPL_data = AAPL_data.drop('Adj Close',axis=1)
AAPL_X= AAPL_data.drop(['High'],axis=1)
AAPL_y= AAPL_data['High']
AAPL_X = mini.fit_transform(AAPL_X)
AAPL_X_train,AAPL_X_test,AAPL_y_train,AAPL_y_test = train_test_split(AAPL_X,AAPL_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(AAPL_X_train, AAPL_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/AAPL_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/AAPL_model.pkl','rb'))
AAPL_future_x = AAPL_X
AAPL_X = AAPL_X[9725:9732]
    # future_x = X[-1]
    # x = X[:-1]
AAPL_bata = pd.read_csv('data/AAPL.csv')
AAPL_date = AAPL_bata['Date']
AAPL_date = AAPL_date[9731:9732]
print(AAPL_date)
AAPL_bata = pd.read_csv('data/AAPL.csv')
AAPL_date = AAPL_bata['Date']
print('PREDICTED HIGH')
AAPL_y = model.predict(AAPL_future_x)
print(AAPL_y[9731:9732])
AAPL_y = model.predict(AAPL_future_x)
print(AAPL_y[9731:9732])

AAPL_output =AAPL_y[9731:9732]


MSFT_data = pd.read_csv('data/MSFT.csv')
df0,df1 = MSFT_data.shape[0], MSFT_data.shape[1]
print('{} dates'.format(df0))
MSFT_data= MSFT_data.drop(['Date'], axis =1)
MSFT_data = MSFT_data.drop('Adj Close',axis=1)
MSFT_X= MSFT_data.drop(['High'],axis=1)
MSFT_y= MSFT_data['High']
MSFT_y.mean()
MSFT_X = mini.fit_transform(MSFT_X)
MSFT_X_train,MSFT_X_test,MSFT_y_train,MSFT_y_test = train_test_split(MSFT_X,MSFT_y,test_size=.64)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(MSFT_X_train, MSFT_y_train)

# Saving model to disk
pickle.dump(regressor, open('models/MSFT_model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('models/MSFT_model.pkl','rb'))
MSFT_future_x = MSFT_X
MSFT_X = MSFT_X[8399:8406]
    # future_x = X[-1]
    # x = X[:-1]
MSFT_bata = pd.read_csv('data/MSFT.csv')
MSFT_date = MSFT_bata['Date']
MSFT_date = MSFT_date[8405:8406]
print(MSFT_date)
MSFT_bata = pd.read_csv('data/MSFT.csv')
MSFT_date = MSFT_bata['Date']
print('PREDICTED HIGH')
MSFT_y = model.predict(MSFT_future_x)
print(MSFT_y[8405:8406])
MSFT_y = model.predict(MSFT_future_x)
print(MSFT_y[8405:8406])

MSFT_output =MSFT_y[8405:8406]
