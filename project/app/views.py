from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from app.forms import UserRegistrationForm
from .models import customer, fooditem, reviews
from .forms import customerForm, fooditemForm, reviewForm
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

class UserPageView(ListView):
    model = customer
    template_name = 'user.html'
def userForm(request):
    if request.method=='POST':
        users = customerForm(request.POST)
        if users.is_valid():
            users.save()
            return redirect('user')
        else:
            return HttpResponse("Entered data is invalid!")
    else:
        users = customerForm() 
        return render(request,'userform.html',{'data': users})
    
class FoodPageView(ListView):
    model = fooditem
    template_name = 'food.html'
def foodform(request):
    if request.method=='POST':
        food = fooditemForm(request.POST, request.FILES)
        if food.is_valid():
            food.save()
            return redirect('food')
        else:
            return HttpResponse("Entered data is invalid!")
    else:
        food = fooditemForm()
        return render(request,'foodform.html',{'data':food})
    
class ReviewPageView(ListView):
    model = reviews
    template_name = 'review.html'
def reviewform(request):
    if request.method=='POST':
        review = reviewForm(request.POST)
        if review.is_valid():
            review.save()
            return redirect('review')
        else:
            return HttpResponse("Entered data is invalid!")
    else:
        review = reviewForm()
        return render(request,'reviewform.html',{'data':review})

class SearchResultsView(ListView):
    model = customer
    template_name = 'search.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = customer.objects.filter(Q(username__icontains=query)|Q(useraddress__icontains=query))
        return object_list
class SearchFoodView(ListView):
    model = fooditem
    template_name = 'searchf.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = fooditem.objects.filter(Q(foodname__icontains=query)|Q(foodprice__icontains=query))
        return object_list
    
def delete(request,customer_id):
    cust_id = int(customer_id)
    cust_sel = customer.objects.get(id = cust_id)
    cust_sel.delete()
    return redirect('user')
