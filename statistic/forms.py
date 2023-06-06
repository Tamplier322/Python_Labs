from django import forms


class StatisticForm(forms.Form):
    """
    form for static
    """
    schedule = forms.ImageField()

    class META:
        fields = ['schedule']