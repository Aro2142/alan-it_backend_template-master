import csv
from encodings.utf_8 import decode
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
import pandas
class GetData(APIView):



    def get(self, request):

        flag = True
        response = []
        with open('short.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if flag:
                       names = row
                       flag = False
                       continue
                else:
                       response.append({k: v for k, v in zip(names, row)})
        return JsonResponse(response, safe=False)

