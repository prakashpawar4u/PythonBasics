import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
myjson = {'id':1,'userId':'Prakash','title':'Nisha@gmaill.io','body':'Blonde'}
#headers = {"Authorization": "Bearer bba09dfca9d3e2a1944c916bd04efaf29f033e8b862c9e26145251b2ad909fb7"}
resp_post = requests.put(url, json = myjson)
print("Status Code:",resp_post.status_code)
print("Resp text",resp_post.text)
