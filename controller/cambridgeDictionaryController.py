import requests

headers = {
    "User-Agent" : "Mozilla/5.0"
}
response = requests.get("https://dictionary.cambridge.org/dictionary/english-chinese-traditional/good", headers=headers)
print(response.text.find("pr dsense "))