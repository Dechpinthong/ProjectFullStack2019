from django.shortcuts import render
from .models import Name, Book, Transaction
# from .forms import ItemForm

def home(request):
   return render(request,'index.html')

def list_book(request):
    context = dict()
    return render(request, 'listbook.html', context)

def list_borrower(request):
    context = dict()
    return render(request, 'borrower.html', context)

def list_publisher(request):
    context = dict()
    return render(request, 'publisher.html', context)

def list_binding(request):
    context = dict()
    return render(request, 'binding.html', context)