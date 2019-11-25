from django.forms import ModelForm
from .models import Rating


class SiteForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'content', 'usability']