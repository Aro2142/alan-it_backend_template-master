import csv
from encodings.utf_8 import decode
import sqlite3
from django.http import JsonResponse
from rest_framework.utils import json
from rest_framework.views import APIView
import pandas

class GetData(APIView):


    def get(self, request):
        conn = sqlite3.connect('Workhouse.sqlite3')
        cursor = conn.cursor()

        tables = ['Company', 'Product', 'ProductMovement', 'ProductSegmentation', 'Sales', 'Stock', 'Warehouse']
        response = []

        for table in tables:
            cursor.execute('SELECT Sales.amount, Stock.date, Stock.product_id FROM Sales INNER JOIN Stock ON Sales.date = Stock.date')
            #cursor.execute(f'SELECT "name" '
             #              f'FROM {table}')
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            response.append([{column: value for column, value in zip(columns, row)} for row in rows])



        # Process data for each table individually


        return JsonResponse(response, safe=False)

    #    flag = True                            [{по продажам}]
     #   response = []
      #  with open('AAAA.sqlite3', newline='', encoding='utf-8') as f:
       #     reader = csv.reader(f)
        #    for row in reader:
         #       if flag:
         
          #             names = row
           #            flag = False
            #           continue
             #   else:
              #         response.append({k: v for k, v in zip(names, row)})
        # return JsonResponse(response, safe=False)