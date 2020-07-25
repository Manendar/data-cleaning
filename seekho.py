import json
import requests
import datetime

request = requests.get("https://www.quandl.com/api/v3/datasets/EUREX/FCPEG2020.json?api_key=yBG2QbE1yNM3yBZzym9U")
data = request.text
json_data = json.loads(data)
# print(json_data)
# column_names = json_data['dataset']['column_names']
# print(column_names)

## the data gett created from the json string
data_list=[]
dt = datetime.datetime.now().strftime('%d-%m-%Y')
for item in json_data['dataset']['data']:
    new_dict = {'name':json_data['dataset']['name']}
    new_dict['Date'] = item[0]
    new_dict['Open'] = item[1]
    new_dict['High'] = item[2]
    new_dict['Low'] = item[3]
    new_dict['Settle'] = item[4]
    new_dict['Volume'] = item[5]
    new_dict['Prev. Day Open Interest'] = item[6]
    data_list.append(new_dict)
#     print(new_dict) 

# finally we are writing the created data to a json file.

with open(f'C:/Users/Admin/Desktop/Bloomberg_petroleum_{dt}.json','w') as wf:
    json.dump(data_list,wf,indent=2)
