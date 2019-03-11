from django.urls import path, include
from . import views

# ROUTING TO FUNCTIONS
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('newUser/', views.newUser, name='newUser'),
    path('newRecipe/', views.newRecipe, name='newRecipe'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('/editRecipe/<int:id>/', views.editRecipe, name='editRecipe'),
    path('/delete/<int:id>/', views.deleterecipe, name='delete'),

]