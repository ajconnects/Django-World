from django.shortcuts import render
from .model_m1 import train_model, train_marks_model

# Create your views here.
def predict1(request):

    # get a model from the train
    trained_model = train_marks_model()

    

    pass

def predict2(request):
    pass

def predict3(request):
    pass