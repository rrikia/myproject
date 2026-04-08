from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy To Use'
    feature3.is_true = False
    feature3.details = 'Our service is easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'Our service is very affordable'

    
    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})

# if just a variable like name = 'Patrick' 
# instead of the dictionary cPontext
# return render(request, 'index.html', {'name': name})
# if u want multiple values, use a dictionary:

def counter(request):
    text = request.POST['text']
    # amount of words that the user input 
    amount_of_words = len(text.split())

    # send the amount of words to counter.html 
    # use key value pair in the line below 
    return render(request, 'counter.html', {'amount': amount_of_words})

