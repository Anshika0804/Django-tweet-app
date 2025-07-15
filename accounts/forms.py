from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "bio", "date_of_birth", "profile_picture"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type":"date"})
        }