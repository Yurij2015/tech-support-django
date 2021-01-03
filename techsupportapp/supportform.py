from django import forms


class SupportForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите свое имя",
                           widget=forms.TextInput(attrs={"class": "form-control"}))
    question = forms.CharField(label="Запрос", widget=forms.Textarea(attrs={"class": "form-control"}))
