import requests
import json

#GET
get_url = "https://jsonplaceholder.typicode.com/todos/1"
get_response = requests.get(get_url)
#print(get_response.json())

#POST
to_do_item = {"userId":2,"title":"my to do","complated":False}
post_url = "https://jsonplaceholder.typicode.com/todos"
headers = {"Content-Type": "application/json"}
# post_response = requests.post(post_url,json=to_do_item,headers=headers)
post_response = requests.post(post_url,data=json.dumps(to_do_item),headers=headers)
# print(post_response.json())

#PUT
put_url = "https://jsonplaceholder.typicode.com/todos/15"
to_do_item_put = {"userId":2,"title":"put tttiiiittttllllleee","complated":False}

put_response = requests.put(put_url,to_do_item_put)
print(put_response.json())

