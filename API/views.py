from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_api(request):
    print(request.body.decode())

    data = {
        "result": 'Hello World!'
    }
    return JsonResponse(data=data)
