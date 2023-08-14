import requests
params = {"machine_name": "Vmc"}
response = requests.get('http://127.0.0.1:8000/update_count')
print(response)
data = response.json()
final = dict(data)
for i in final['data']:
    # if 'Vmc' in final['data']:
        print(i['machine_name'], i['ok_count'],i['ng_count'])


# import datetime
# currunt_timestamp = datetime.datetime.now()



data = { 'machine_name':'Vmc','ng_count': 11+1,'ok_count': 100+1}
r = requests.patch(url='http://127.0.0.1:8000/update_count', data=data)
print(r.json())