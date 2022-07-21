from django.http import JsonResponse
from rest_framework.views import APIView
import json

#Good
class GetData(APIView):
    def get(self, request):
       with open('short.json', 'r', encoding = 'utf-8') as f:
        data = json.load(f)
        return JsonResponse(data, safe=False)
        #return JsonResponse({"response": "ok"})


