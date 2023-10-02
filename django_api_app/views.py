from django.shortcuts import render

# Create your views here.
from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from django.http import JsonResponse
import json

@api_view(['POST'])
# @permission_classes((permissions.AllowAny,))
def nanisha(request):
    if request.method=='POST':
        json_file=json.loads(request.body.decode("utf-8"))
        print('nanisha',json_file)

        sum=json_file['first_value']+json_file['second_value']

        result={"ststuss":200,"result":sum}
        return JsonResponse(result)

