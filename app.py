from flask import Flask,request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.0%}'.format(prediction[0][1])

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Hutan Anda dalam Bahaya.\nPeluang terjadinya kebakaran adalah {}'.format(output))
    else:
        return render_template('forest_fire.html',pred='Hutan Anda aman.\n Peluang terjadinya kebakaran adalah {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True,port=5001)