from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"msg": "Hello World!"})