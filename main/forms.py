from django.forms import ModelForm
from main.models import BuyEntry

class BuyEntryForm(ModelForm):
    class Meta:
        model = BuyEntry
        fields = ["name", "address", "age"]