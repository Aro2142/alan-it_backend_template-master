import json
#with open('C:\\Users\\Aro\\Desktop\\Сборка проекта правильно\\alan-it_backend_template-master\\short.json', encoding='utf-8') as f:
    #d = json.load(f)
    #

import pandas as pd
df = pd.read_json('C:\\Users\\Aro\\Desktop\\Сборка проекта правильно\\alan-it_backend_template-master\\xrcrv-n2nu0.json')
#df = pd.DataFrame(df,columns = ['year','month','day','customer_segment','customer_type','product_segment','product_type','manager','company','service','retail','customerType','unit','product','region','customer','sales','amount','profit'])
#df = df.to_json()
print(df)