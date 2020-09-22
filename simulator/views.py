from django.shortcuts import render
from django.http import HttpResponse

#responses for different parts of our site. 

portfolio = [
    {'name' : 'AMZN',
    'amount' : '10',
    'price' : 500,
    },
    {'name' : 'AAPL',
    'amount' : '10',
    'price' : 125,
    }
]
def home(request):
    return render(request,'simulator/home.html')

def about(request):
    return render(request,'simulator/about.html')

def userPortfolio(request):
    context = {
        'portfolio' : portfolio
    }
    return render(request,'simulator/portfolio.html',context)

