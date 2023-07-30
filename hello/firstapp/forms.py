from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО", min_length=2, max_length=20)
    age = forms.IntegerField(label="Возраст", min_value=16, max_value=120)
    comment = forms.CharField(label="Комментарий",
                              widget=forms.Textarea,required=False)
    field_order = ["age", "name", "comment"]

class ContactForm(forms.Form):
    age = forms.IntegerField(help_text='Введите возраст')
    nationality = forms.CharField()
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')


f = ContactForm(label_suffix='?')
