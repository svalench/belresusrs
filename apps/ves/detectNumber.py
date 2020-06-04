import json

from django.http import HttpResponse

from nomer.mainTCP import detect


def detectNumber(request):
    number=detect(request.POST['path'])
    payload = {'success': True,'number':number}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')