import requests
result = requests.get("http://blog.utkarsh-kaushik.com/programmers-love-with-ctrls/")
print(result.status_code)
print(result.headers)
print(result.text)
result.encoding = result.apparent_encoding
file = open("test1.html", mode = 'w')
file.write(result.text)
file.close()