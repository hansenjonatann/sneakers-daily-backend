import numpy as np
from flask import Flask , request , jsonify 
import pickle

# Membuat aplikasi Flask
app = Flask(__name__)

# Melakukan pengambian data pikle
model = pickle.load(open('sneakers.pkl' , 'rb'))

# Membuat routing utama untuk testing 
@app.route('/')
def Home():
    return {"status": "Ok" , "message" : "Server is running"}

# Membut routing untuk predict 
@app.route('/predict' , methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return {"status": True , 'statuscode': 200 , 'prediction_test' : 'The prediction is {}'.format(prediction)}


if __name__ == '__main__':
    app.run(debug=True)

