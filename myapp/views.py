from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# if just a variable like name = 'Patrick' 
# instead of the dictionary context
# return render(request, 'index.html', {'name': name})

# if u want multiple values, use a dictionary:
'''
def index(request):
    # Dictionary
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British'
    }

    return render(request, 'index.html', context)
'''

def counter(request):
    text = request.POST['text']
    # amount of words that the user input 
    amount_of_words = len(text.split())

    # send the amount of words to counter.html 
    # use key value pair in the line below 
    return render(request, 'counter.html', {'amount': amount_of_words})

