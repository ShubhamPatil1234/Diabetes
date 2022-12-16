#from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import DaibetesReport
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to DAIBETES PREDICTION OF PATIENT")
    return render_template("index.html")


@app.route('/predict_daibetes',methods=["POST","GET"])
def get_daibetes_prediction():

    if request.method == "GET":
        print("We are using GET Method")


        Glucose = eval(request.args.get("Glucose"))
        BloodPressure = eval(request.args.get("BloodPressure"))
        SkinThickness= eval(request.args.get("SkinThickness"))
        Insulin= eval(request.args.get("Insulin"))
        BMI= eval(request.args.get("BMI"))
        DiabetesPedigreeFunction= eval(request.args.get("DiabetesPedigreeFunction"))
        Age= eval(request.args.get("Age"))

        print("Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age\n",Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        med_ins = DaibetesReport(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        charges = med_ins.get_daibetes_data()

        return render_template("index.html", prediction = charges)
    else:
        print("We are using POST Method")

        Glucose = eval(request.form.get("Glucose"))
        BloodPressure = eval(request.form.get("BloodPressure"))
        SkinThickness= eval(request.form.get("SkinThickness"))
        Insulin= eval(request.form.get("Insulin"))
        BMI= eval(request.form.get("BMI"))
        DiabetesPedigreeFunction= eval(request.form.get("DiabetesPedigreeFunction"))
        Age= eval(request.form.get("Age"))

        print("Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age\n",Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)

        med_ins = DaibetesReport(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        charges = med_ins.get_daibetes_data()

        return render_template("index.html", prediction = charges)
        predicted_charges = model.predict([array])[0]
        

if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=config.PORT_NUMBER, debug=True)