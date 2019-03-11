from django.shortcuts import render, redirect,get_object_or_404
from .forms import RecipeForm, UserForm
from .models import CreatorModel, RecipeModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    userLogin = CreatorModel.objects.filter(username=request.user)
    recipe = RecipeModel.objects.all()
    context = {
        'userLogin':userLogin,
        'recipe':recipe
    }
    return render (request, "RecipeApp/index.html", context)


def newUser(request):
    # TO USE INFORMATION ENTERED IN FORM/PULL INFO FROM FORM TO DISPLAY
    new_user = UserForm(request.POST or None)
    # TO SAVE IF INFO VALIDATES
    if new_user.is_valid():
        # SAVES DATA AS PERSON
        new_user.save()
        # TO CREATE A USER/PERSON THAT CAN LOGIN
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        # TO RETURN TO INDEX AFTER SUBMIT
        return redirect('index')
    new_user = UserForm(request.POST or None)

    return render (request, 'RecipeApp/newUser.html', {'new_user':new_user})

@login_required
def newRecipe(request):
    new_recipe = RecipeForm(request.POST or None)
    if new_recipe.is_valid():
        # SAVES DATA AS PERSON
        new_recipe.save()
        return redirect('user')
    return render (request, 'RecipeApp/newRecipe.html',{'new_recipe':new_recipe})

def user(request):
    recipe = RecipeModel.objects.all()
    context = {
        'recipe':recipe
    }
    return render (request, 'RecipeApp/user.html',context)

def editRecipe(request,id):
    # TO GRAB SPECIFIC GAMER/USER
    meal = get_object_or_404(RecipeModel, pk=id)
    # TO GRAB SELECTED GAME AND SEND TO FORM
    edit_recipe = RecipeForm(request.POST or None)
    # TO SAVE CHANGES
    if edit_recipe.is_valid():
        edit_recipe.save()
        # SEND BACK TO INDEX
        return redirect('user')
    # ROUTE TO HTML PAGE
    return render(request, 'RecipeApp/newRecipe.html', {'new_recipe': edit_recipe})

def deleterecipe(request, id):
    # TO GRAB SPECIFIC ACCOUNT
    meal = get_object_or_404(RecipeModel, pk=id)
    # TO DELETE IF SUBMITED/SAVE DELETE
    if request.method == 'POST':
        meal.delete()
        # RETURN TO INDEX
        return redirect('user')
    # ROUTE TO/FROM DELETE CONFIRMATION PAGE
    return render(request, 'RecipeApp/delete.html', {'selectedmeal': meal})