"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from django.conf.urls.static import  static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('user/',views.UserPageView.as_view(),name='user'),
    path('userf/',views.userForm,name='userf'),
    path('food/',views.FoodPageView.as_view(),name='food'),
    path('foodf/',views.foodform,name='foodf'),
    path('review/',views.ReviewPageView.as_view(),name='review'),
    path('reviewf/',views.reviewform,name='reviewf'),
    path('search/',views.SearchResultsView.as_view(),name='search'),
    path('searchf/',views.SearchFoodView.as_view(),name='searchf'),
    path('delete/<int:customer_id>/',views.delete,name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)