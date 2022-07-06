from django.shortcuts import render
from .models import Quote
# Create your views here.

def quote(request):
    quotes = Quote.objects.all()
    context = {
        'quotes':quotes
    }
    return render(request, 'quote.html', context)
