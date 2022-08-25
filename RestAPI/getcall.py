import requests
import pprint
# url = 'https://gorest.co.in/public-api/users/123'
# #myjson = {'id':30,'name':'Prakash','email':'Prakash@gmaill.io','gender':'Male','status':'Active','created_at':'2021-01-14T03:50:03.564+05:30','updated_at':'2021-01-14T03:50:03.564+05:30'}
# headers = {"Authorization": "Bearer bba09dfca9d3e2a1944c916bd04efaf29f033e8b862c9e26145251b2ad909fb7"}
# resp_post = requests.get(url,headers=headers)
# print("Status Code:",resp_post.status_code)
# print("Resp text",resp_post.text)
#
#
# #https://www.taniarascia.com/making-api-requests-postman-curl/
# Here is the map of methods to endpoints we'll be using. /posts means all, and the 1 in /posts/1 represents /posts/{id}, so ID number1.
#
# Method	Endpoint
# GET	https://jsonplaceholder.typicode.com/posts
# POST	https://jsonplaceholder.typicode.com/posts
# PUT	https://jsonplaceholder.typicode.com/posts/1
# PATCH	https://jsonplaceholder.typicode.com/posts/1
# DELETE	https://jsonplaceholder.typicode.com/posts/1
# You can click those URLs to see the GET values they provide to the browser. You can use the browser for GET, but you'll have to use cURL or Postman to POST, PUT, PATCH or DELETE.


url = 'https://jsonplaceholder.typicode.com/posts/1'
# #myjson = {'id':30,'name':'Prakash','email':'Prakash@gmaill.io','gender':'Male','status':'Active','created_at':'2021-01-14T03:50:03.564+05:30','updated_at':'2021-01-14T03:50:03.564+05:30'}
# headers = {"Authorization": "Bearer bba09dfca9d3e2a1944c916bd04efaf29f033e8b862c9e26145251b2ad909fb7"}
response = requests.get(url)
json_data = response.json()
print("Type",type(response))
print("Status Code:",response.status_code)
print("Resp text",response.text)
print(json_data,type(json_data))
#pprint("Got hte response")