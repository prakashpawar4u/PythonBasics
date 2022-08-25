import requests

# url = 'https://gorest.co.in/public-api/users'
# myjson = {'id':30,'name':'Prakash','email':'Prakash@gmaill.io','gender':'Male','status':'Active','created_at':'2021-01-14T03:50:03.564+05:30','updated_at':'2021-01-14T03:50:03.564+05:30'}
# headers = {"Authorization": "Bearer bba09dfca9d3e2a1944c916bd04efaf29f033e8b862c9e26145251b2ad909fb7"}
# resp_post = requests.post(url, json = myjson,headers=headers)
# print("Status Code:",resp_post.status_code)
# print("Resp text",resp_post.text)


#https://jsonplaceholder.typicode.com/posts
url = 'https://jsonplaceholder.typicode.com/posts/'
myjson = {'id':1,'userId':'Prakash','title':'Prakash@gmaill.io','body':'Sexy'}
#headers = {"Authorization": "Bearer bba09dfca9d3e2a1944c916bd04efaf29f033e8b862c9e26145251b2ad909fb7"}
resp_post = requests.post(url, json = myjson)
print("Status Code:",resp_post.status_code)
print("Resp text",resp_post.text)


#
# Resp text {
#   "userId": 1,
#   "id": 1,
#   "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#   "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
# }