from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Mi primera Web con DJango")


