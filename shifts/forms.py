from django import forms
from .models import Shift


class ShiftForm(forms.ModelForm):  # shiftForm
    clock_in = forms.TimeField(label='Clock In ',
                                widget=forms.TimeInput(
                                attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    clock_out = forms.TimeField(label='Clock Out',
                                widget=forms.TimeInput(
                                attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    break_time = forms.DurationField(label='Break',
                                    widget=forms.TimeInput(
                                    attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": ""}))

    class Meta():
        model = Shift
        fields = ['name', 'description']


class SelectDateForm(forms.Form):
    date_from = forms.DateField(widget=forms.SelectDateWidget(
                                attrs={"class": "", }, ), 
                                label="From")
    date_to = forms.DateField(widget=forms.SelectDateWidget(
                                attrs={"class": "", }), 
                                label="To")


class ShiftUpdateForm(forms.Form):
    clock_in = forms.TimeField(label='Clock In ',
                                widget=forms.TimeInput(
                                attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    clock_out = forms.TimeField(label='Clock Out',
                                widget=forms.TimeInput(
                                attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    break_time = forms.DurationField(label='Break',
                                      widget=forms.TimeInput(
                                      attrs={"class": "form-control", "placeholder": "hour:min:sec"}))

    date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": ""}))
