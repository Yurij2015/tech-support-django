from django.shortcuts import render


# from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "index.html")

# def index(request):
#     return HttpResponse("<h2>Главная</h2>")


# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
#
# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")
#
#
# def techsupporrequests(requewt, techsupportrequestid=77):
#     output = "<h2>Номер запроса в техподдержку № {0} </h2>".format(techsupportrequestid)
#     return HttpResponse(output)
#
#
# def users(request, id=88, name="Yurij"):
#     output = "<h2>Пользователь: {0}; Имя пользователя: {1} </h2>".format(id, name)
#     return HttpResponse(output)
