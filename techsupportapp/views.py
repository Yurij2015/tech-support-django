from django.shortcuts import render
from .supportform import SupportForm
from django.http import HttpResponse


# Create your views here.

def index(request):
    data = {"message": "Добро пожаловать на сайт поддержки!"}
    return render(request, "techsupportapp/index.html", context=data)


def supportform(request):
    support_form = SupportForm()
    if request.method == "POST":
        support_form = SupportForm(request.POST)
        if support_form.is_valid():
            message = support_form.cleaned_data["question"]
            name = support_form.cleaned_data["name"]
            return HttpResponse("<h3>Вопрос пользователя {1} - {0} - отправлен</h3>".format(message, name))
        # else:
        #     return HttpResponse("Некорректные данные!")
    # else:
        # support_form = SupportForm()
    return render(request, "techsupportapp/supportform.html", {"supportform": support_form})
