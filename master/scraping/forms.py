from django import forms


class DateFilterForm(forms.Form):
    FILTER_CHOICES = (
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
    )
    filter_by = forms.ChoiceField(choices=FILTER_CHOICES)
