from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("diabetes.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def man():
    return render_template("main.html")


@app.route("/predict", methods=["POST"])
def home():
    pregnancies = float(request.form["Pregnancies"])
    glucose = float(request.form["Glucose"])
    blood_pressure = float(request.form["BloodPressure"])
    skin_thickness = float(request.form["SkinThickness"])
    insulin = float(request.form["Insulin"])
    bmi = float(request.form["BMI"])
    diabetes_pedigree_function = float(request.form["DiabetesPedigreeFunction"])
    age = float(request.form["Age"])
    # Code to predict the outcome:
    to_predict = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    prediction_of_to_predict = model.predict(to_predict)
    if prediction_of_to_predict[0] == 1:
        result = "The patient has diabetes."
    elif prediction_of_to_predict[0] == 0:
        result = "The patient doesn't have diabetes."
    return render_template("main.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)
