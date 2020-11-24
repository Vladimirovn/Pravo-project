from constance import config
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views import View

from main.form import MailForm
from main.models import Review
from django.conf import settings


class Landing(View):
    template = "main.html"

    model = Review
    queryset = Review.objects.all()

    def get(self, request):
        return render(request, self.template, {
            "reviews": self.queryset[:4],
            "config": config,
            "form": MailForm(),
            "is_answer": False,
        })


def rights_view(request):
    try:
        return FileResponse(open(f'{settings.BASE_DIR}/static/pdf/Consent_to_working_personal.pdf', 'rb'),
                            content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


def send_request_on_mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['mail'],
                build_mail_text(
                    form.cleaned_data['name'],
                    form.cleaned_data['mail'],
                    form.cleaned_data['body'],
                    form.cleaned_data['promo'],
                    form.cleaned_data['phone']
                ),
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
            send_mail(
                "Право на адвоката – Заявка принята и находится в обработке",
                build_mail_for(),
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['mail']],
                fail_silently=True,
            )
            return render(request, "main.html", {
                "reviews": Review.objects.all()[:4],
                "config": config,
                "form": MailForm(),
                "is_answer": True,
                "result": True,
                "result_msg": "Мы получили Вашу заявку на бесплатную консультацию. В ближайшее время с Вами свяжется \
                              первый освободившийся специалист. Благодарим за доверие в решении Вашего вопроса!"

            })
        return \
            render(request, "main.html", {
                "reviews": Review.objects.all()[:4],
                "config": config,
                "form": MailForm(),
                "is_answer": True,
                "result": True,
                "result_msg": "Что-то пошло не так.. Вероятнее всего вы неправильно заполнили поле кода с картинки. \
                                Письмо не было отправленно попробуйте еще раз.."

            })


def build_mail_text(name, mail, body, promo, phone):
    return f"""
    НОВОЕ ОБРАЩНИЕ!!!
    
    ОТ {name} ПОЧТА {mail}
    
    Купон  {promo}
    
    Телефон  {phone}
    
    Обращение:
    
    {body}
    
    """


def disclaimer_ru():
    return """Настоящее сообщение и любые прикрепленные к нему файлы (вместе именуемые «сообщение») предназначены исключительно для адресата. Настоящее сообщение может содержать конфиденциальную, частную и/или не подлежащую разглашению информацию.Любой несанкционированный просмотр, удержание, копирование, раскрытие или распространение данного сообщения строго запрещены.
В случае, если Вы не являетесь адресатом данного сообщения, пожалуйста, удалите его и все его копии из Вашей системы, уничтожьте любые бумажные копии и сообщите отправителю посредством ответа. Вы не должны, прямо или косвенно, использовать, раскрывать, распространять, печатать, копировать, а также предпринимать какие-либо действия, полагаясь на данное сообщение, если Вы не являетесь его адресатом.
Любые ошибки передачи данного сообщения не являются основаниями для отмены или утраты конфиденциальности или других средств правовой защиты. Отправитель не несет ответственности за любые убытки или ущерб, возникшие в результате использования данного сообщения или от каких-либо вирусов, которые могут содержаться в прикрепленных к сообщению файлах и/или каком-либо указанном в сообщении Интернет сайте. Любые взгляды или мнения, изложенные в данном сообщении, принадлежат исключительно его автору."""


def disclaimer_en():
    return """This message and any files attached to it (together, the “e-mail”) are for the sole use of the intended recipient(s). This e-mail may contain confidential, proprietary and/or legally privileged information. Any unauthorized review, retention, duplication, disclosure, or distribution of this e-mail is strictly prohibited.
If you are not the intended recipient of this e-mail, please delete it and all copies of it from your system, destroy any hard copies of it and notify the sender by reply e-mail. You must not, directly or indirectly, use, disclose, distribute, print, copy, or take any action in reliance on, any part of this e-mail if you are not the intended recipient. No confidentiality, privilege or other legal protection is waived or otherwise lost by any transmission errors related to this e-mail. Does not accept liability for any loss or damage resulting from the use of this e-mail or from any viruses that the files attached and/or any website linked to this e-mail may contain. Any views or opinions expressed in this e-mail are solely those of the author."""

def build_mail_for():
    text = f'''Здравствуйте!
Команда сервиса "Право на адвоката" благодарит Вас за оказанное доверие в решении Вашего вопроса. Мы получили Вашу заявку на консультацию. В ближайшее время с Вами свяжется первый освободившийся специалист.\n\n
С уважением,
Право на адвоката.
info@pravonaadvokata.ru
www.pravonaadvokata.ru

Дисклеймер:
{disclaimer_ru()}

Disclaimer:
{disclaimer_en()}'''
    return text
