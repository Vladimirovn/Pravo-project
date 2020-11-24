from captcha.fields import CaptchaField
from django import forms


class MailForm(forms.Form):
    name = forms.CharField(max_length=128, label="Имя")
    promo = forms.CharField(max_length=128, label="Купон на скидку", required=False)
    phone = forms.CharField(max_length=16, label="Телефон", required=False)
    mail = forms.EmailField(max_length=128, label="E-mail")
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 100}),
                           label="Описание вопроса (ситуации). Удобное время для связи.")
    captcha = CaptchaField(label="Введите код с картинки")
    check_agry = forms.BooleanField(label='Я даю свое согласие на обработку данных',
                                    widget=forms.widgets.CheckboxInput(check_test=lambda x: x is True))
