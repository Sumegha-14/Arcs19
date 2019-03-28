from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import AQI_levels as aqi
import helpers as hlp
# Your API definition
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello'
#model = joblib.load(open('model.pkl','rb'))

@app.route('/predict', methods=['POST'])
def predict():
    arr=request.json
    features = arr['features'] 
    print(features) 
    a,b=hlp.get_index(features[0],features[1])
    #a = 1
    #b = 2
    l=[]
    for i in range (15):
        if i==a:
            l.append(1)
        else:
            l.append(0)
    for i in range (12):
        if i==b:
            l.append(1)
        else:
            l.append(0)            
    print(len(l))
    #test=np.array([l])
    test = np.array(l).reshape(1,len(l))
    lr = joblib.load("./model_air.pkl")
    result = lr.predict(test)
    print(result)
    res1 = result.tolist()
    
    w = aqi.get_details(res1[0][0])
    print(w+"PM10 level: "+str(res1[0][0]))

    #result1=predicted(symptoms)
    return w+"PM10 level: "+str(res1[0][0]);
        
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 1276 # If you don't provide any port the port will be set to 12345

    lr = joblib.load("model_air.pkl") # Load "model.pkl"
    print ('Model loaded')
    
    app.run(port=port, debug=True)
    app.run()