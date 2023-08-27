from django.shortcuts import render


# our home page view
def home(request):
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(	Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    import pickle
    model = pickle.load(open("diabetes_prediction_ml_model.sav", "rb"))
    scaled = pickle.load(open("scaler.sav", "rb"))
    prediction = model.predict(sc_X.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]))

    if prediction == 0:
        return "not diabetes"
    elif prediction == 1:
        return "diabetes"
    else:
        return "error"


# our result page view
def result(request):
    Pregnancies = int(request.GET['Pregnancies'])
    Glucose = int(request.GET['Glucose'])
    BloodPressure = int(request.GET['BloodPressure'])
    SkinThickness = int(request.GET['SkinThickness'])
    Insulin = int(request.GET['Insulin'])
    BMI = int(request.GET['BMI'])
    DiabetesPedigreeFunction = int(request.GET['DiabetesPedigreeFunction'])
    Age = int(request.GET['Age'])

    result = getPredictions(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age )

    return render(request, 'result.html', {'result': result})
