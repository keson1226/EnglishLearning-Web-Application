from requests import get
from bs4 import BeautifulSoup


### HTTP Request Setting and Sending ###
headers = {
    "User-Agent" : "Mozilla/5.0"
}
response = get("https://dictionary.cambridge.org/dictionary/english-chinese-traditional/good", headers=headers)


### Use BeautifulSoup to parse Raw HTML as Soup ###
html = BeautifulSoup(response.content, 'html.parser')


### 
# If The Dictionary give result,
#   the <body>'s class value will be "break default_layout",
# else 
#   will be "break home_layout" 
###
if "home_layout" in html.body['class'] :
    pass
else :

    ### Find CambridgeDictionary Important Data of Soup ###
    kkk = html.find_all(class_ = "def ddef_d db")[0]
    with open('./data', 'w', encoding='utf-8') as file:
        file.write(kkk.text)
        # TODO : edit this section