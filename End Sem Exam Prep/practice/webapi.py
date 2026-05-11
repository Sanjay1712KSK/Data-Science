import requests as r
url="https://jsonplaceholder.typicode.com/todos/1"
res=r.get(url)
data=res.json()
print(data)
'''question from - End Sem Exam Prep/PYQs/21CSS303T 08.07.2024.pdf
                  End Sem Exam Prep/PYQs/21CSS303T 13.05.2024 AN.pdf
                  End Sem Exam Prep/PYQs/21CSS303T 14.07.2025 AN.pdf'''