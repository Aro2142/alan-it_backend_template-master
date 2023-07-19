from encodings.utf_8 import decode
import sqlite3
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView

class GetData(APIView):
    def get(self, request):
        conn = sqlite3.connect('Workhouse.sqlite3')
        cursor = conn.cursor()
        response = []
        cursor.execute('SELECT * FROM Stock JOIN ProductMovement ON Stock.date=ProductMovement.date JOIN Sales ON ProductMovement.date=Sales.date JOIN Company ON Stock.company_id=Company.company_id JOIN Warehouse ON Stock.warehouse_id=Warehouse.warehouse_id JOIN Product ON Stock.product_id=Product.product_id JOIN ProductSegmentation ON Product.product_id=ProductSegmentation.product_id')
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        response.append([{column: value for column, value in zip(columns, row)} for row in rows])
        response = response[0]
        return JsonResponse(response, safe=False)
