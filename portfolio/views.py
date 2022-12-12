from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio_index(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios
    }
    return render(request, 'portfolio_index.html', context)

def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'portfolio_detail.html', context)