import requests as r
url="https://jsonplaceholder.typicode.com/todos/1"
res=r.get(url)
data=res.json()
print(data)