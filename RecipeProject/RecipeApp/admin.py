from django.contrib import admin
from .models import RecipeModel, CreatorModel

# Register your models here.
admin.site.register(RecipeModel)
admin.site.register(CreatorModel)
