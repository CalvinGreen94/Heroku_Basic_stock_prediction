import numpy as np
from flask import Flask, session,abort,request, jsonify, render_template,redirect,url_for,flash
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler as mini
import os
import stripe
import datetime

app = Flask(__name__)
pub_key ='pk_live_2pO0yUvt9xKyjAo9rca8Vkc600FWtgJuqZ'

model = pickle.load(open('models/bit_model.pkl', 'rb'))
eth_model = pickle.load(open('models/eth_model.pkl', 'rb'))
AAPL_model = pickle.load(open('models/AAPL_model.pkl', 'rb'))
MSFT_model = pickle.load(open('models/MSFT_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

def index():
    return render_template('index.html',pub_key=pub_key)

@app.route('/pay',methods=['POST'])
def pay():
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=19900,
        currency='usd',
        description='The Product'
    )

@app.route('/predict_bitcoin',methods=['POST'])
def predict_bitcoin():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/BTC-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['High'],axis=1)
    y= data['High']
    mini = mini()
    X = mini.fit_transform(X)
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
    y = model.predict(future_x)
    print(y[3289:3290])
    output =y[3289:3290]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED HIGH FOR Bitcoin ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_ethereum',methods=['POST'])
def predict_ethereum():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/ETH-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['High'],axis=1)
    y= data['High']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[1436:1443]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/ETH-USD.csv')
    date = bata['Date']
    date = date[1442:1443]
    print(date)
    bata = pd.read_csv('data/ETH-USD.csv')
    date = bata['Date']
    print('PREDICTED HIGH')
    y = eth_model.predict(future_x)
    print(y[1442:1443])
    y = eth_model.predict(future_x)
    print(y[1442:1443])
    output =y[1442:1443]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED HIGH FOR Ethereum ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_APPLE',methods=['POST'])
def predict_APPLE():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/AAPL.csv')
    data = data.fillna(28.630752329973255)
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['High'],axis=1)
    y= data['High']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[9725:9732]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/AAPL.csv')
    date = bata['Date']
    date = date[9731:9732]
    print(date)
    bata = pd.read_csv('data/AAPL.csv')
    date = bata['Date']
    print('PREDICTED HIGH')
    y = AAPL_model.predict(future_x)
    print(y[9731:9732])
    y = AAPL_model.predict(future_x)
    print(y[9731:9732])
    output =y[9731:9732]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED HIGH FOR APPLE ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_MSFT',methods=['POST'])
def predict_MSFT():
    '''
    For rendering results on HTML GUI
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
    data = pd.read_csv('data/MSFT.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['High'],axis=1)
    y= data['High']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[8399:8406]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/MSFT.csv')
    date = bata['Date']
    date = date[8405:8406]
    print(date)
    bata = pd.read_csv('data/MSFT.csv')
    date = bata['Date']
    print('PREDICTED HIGH')
    y = MSFT_model.predict(future_x)
    print(y[8405:8406])
    y = MSFT_model.predict(future_x)
    print(y[8405:8406])
    output =y[8405:8406]
    date = datetime.date.today()
    return render_template('index.html', prediction_text='THANK YOU FOR YOUR PURCHASE,\n PREDICTED HIGH FOR MICROSOFT ON THE DAY OF {} IS $ {}'.format(date,output))

@app.route('/predict_api',methods=['GET'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler as mini
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
    data = pd.read_csv('data/BTC-USD.csv')
    data= data.drop(['Date'], axis =1)
    data = data.drop('Adj Close',axis=1)
    X= data.drop(['High'],axis=1)
    y= data['High']
    mini = mini()
    X = mini.fit_transform(X)
    future_x = X
    X = X[3281:3288]
    # future_x = X[-1]
    # x = X[:-1]
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    date = date[3287:3288]
    print(date)
    bata = pd.read_csv('data/BTC-USD.csv')
    date = bata['Date']
    print('PREDICTED HIGH')
    y = model.predict(future_x)
    print(y[3287:3288])

    output =y[3287:3288]

    return jsonify(output)
@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080) #debug=True,host="0.0.0.0",port=50000
