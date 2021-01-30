import requests
import random

URL = 'http://www.shakespeares-sonnets.com/all.php'
page = requests.get(URL)
text = page.text
c = text.split("<a href='/sonnet/")
print(page.text)
a = random.randint(1, 154)