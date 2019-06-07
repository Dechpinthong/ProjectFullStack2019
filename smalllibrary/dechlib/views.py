from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from dechlib.models import Name, Book, Transaction, Binding, Publisher
# from .forms import ItemForm


@login_required
def dech_page(request):
    return render(request, 'listbook.html')

def home1(request):
      context = dict()

      if request.user.is_authenticated:
        context['dechy'] = 'Welcome Fuck {}'.format(request.user)
      else:
        context['dechy'] = 'Welcome Fuck ass'

      return render(request, 'home1.html', context)

@login_required
def logoutdech(request):
    logout(request)
    return redirect('home1')


def list_book(request):
    books = Book.objects.all().order_by('name')
    context = dict()
    context['books'] = books
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