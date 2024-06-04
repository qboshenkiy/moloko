from django import forms

class PhoneForm(forms.Form):
    name = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
