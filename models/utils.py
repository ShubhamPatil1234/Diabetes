import pickle
import json
import pandas as pd
import numpy as np
import config


class DaibetesReport():
    def __init__(self, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age
    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_daibetes_data(self):

        self.load_model()  # Calling load_model method to get model and json_data
        # array = np.zeros(x.shape[1])
        array = np.zeros(len(self.json_data['columns']))
        array[0] = self.Glucose
        array[1] = self.BloodPressure
        array[2] = self.SkinThickness
        array[3] = self.Insulin
        array[4] = self.BMI
        array[5] = self.DiabetesPedigreeFunction
        array[6] = self.Age

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        # print("predicted_charges",predicted_charges)
        # return np.around(predicted_charges, 2)
    
        if predicted_charges==1:
            print("you are daibetic person,avoid eating sweets")
        else:
            print("you are not daibetes patient,enjoy your sweets")
            
        prediction = "Hey, you are having diabetes symptoms,avoid sweets!" if predicted_charges == 1 else "Hey you are having no issues with daibetes Enjoy!!"
        return prediction        

if __name__ == "_main_":
    Glucose=148.0
    BloodPressure=70.0
    SkinThickness=35.0
    Insulin=0.0
    BMI=33.6
    DiabetesPedigreeFunction=0.627
    Age=50.0

    med_ins = DaibetesReport(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    charges = med_ins.get_daibetes_data()
    print()