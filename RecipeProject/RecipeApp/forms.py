from django import forms
from .models import RecipeModel, CreatorModel


# to sync person model to form
class RecipeForm(forms.ModelForm):
    class Meta():
        model = RecipeModel
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta():
        model = CreatorModel
        exclude = ["userForeignKey"]
        fields = '__all__'

        def clean(self):
            pass1 = self.cleaned_data["password1"]
            pass2 = self.cleaned_data["password2"]

        # IN THE CASE THAT THEY DO NO MATCH
            if pass1 != pass2:
             raise forms.ValidationError("Passwords Do Not Match")

        # RETURN CANT CALL SPECIFIC VARIABLE, DOESNT WORK IF ONE IS CALLED
            return
