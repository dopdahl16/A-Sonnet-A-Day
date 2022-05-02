import requests
import random
import re

#URL = 'http://www.shakespeares-sonnets.com/all.php'

sonnet_no = random.randint(1, 154)
URL = "http://www.shakespeares-sonnets.com/sonnet/" + str(sonnet_no)
page = requests.get(URL)
sonnet_text = page.text.split("<h1 class='title'")[1].split("<div class='separator")[0].split(">", 1)[1]

sonnet_text = re.sub('<[^<]+?>', '', sonnet_text).replace("&nbsp;", "  ")
print(sonnet_text)
print(URL)
