from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

 

def predict(request):
    return render(request, 'predict.html')

 

def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Age = float(request.POST.get('Age'))
        air_pollution = float(request.POST.get('air_pollution'))
        alcohol_use = float(request.POST.get('alcohol_use'))
        genetic_risk = float(request.POST.get('genetic_risk'))
        chronic_lung_disease = float(request.POST.get('chronic_lung_disease'))
 
        # Unpickle model C:\Users\TECHNICIAN\Desktop\CANCER-END-END\django_cancer_ml\mysite\new_model.pickle
        model = pd.read_pickle(r'C:\Users\TECHNICIAN\Desktop\CANCER-END-END\django_cancer_ml\mysite\new_model.pickle')
        #pd.to_pickle(model,)

        # Make prediction
        result = model.predict([[Age, air_pollution, alcohol_use, genetic_risk,chronic_lung_disease]])

        Level = result[0]

        PredResults.objects.create(Age=Age, air_pollution=air_pollution, alcohol_use=alcohol_use,
                                   genetic_risk=genetic_risk,chronic_lung_disease=chronic_lung_disease, Level=Level)

        return JsonResponse({'Level': Level, 'Age': Age,
                             'air_pollution': air_pollution, 'alcohol_use': alcohol_use, 
                             'genetic_risk': genetic_risk,'chronic_lung_disease':chronic_lung_disease},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
