import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
rf_model = pickle.load(open('rf_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    # print(data)
    # #print(np.array(list(data.values())).reshape(1,-1))
    # #new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    # data.pop('trans_date_trans_time')
    # data = np.array(list(data.values())).reshape(1,-1)
    print(f"Original Data \n : {data}")
    data = [data]
    print(f"Transform Data \n : {data}")
    data_df = pd.DataFrame(data)
    print(data_df.dtypes)
    output=rf_model.predict(data)
    print(output[0])
    

    return jsonify(output[0])

#@app.route('/predict',methods=['POST'])
#def predict():
#    data=[float(x) for x in request.form.values()]
#    #final_input=rf_model.transform(np.array(data).reshape(1,-1))
#    final_input=np.array(list(data.values())).reshape(1,-1)
#    print(final_input)
#    output=rf_model.predict(final_input)[0]
#    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



if __name__=="__main__":
    app.run(debug=True)