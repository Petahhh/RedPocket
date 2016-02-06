from django import forms

class NewGoal(forms.Form):
    name = forms.CharField(max_length=60)
    goal = forms.DecimalField()
