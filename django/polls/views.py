from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! It is Thursday my dudes!")
