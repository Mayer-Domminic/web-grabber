import re
from bs4 import BeautifulSoup
import requests

i=0
# gets url html
html = requests.get("https://www.coindesk.com/").text

# writing website resuls to output.txt for testing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(html)
    f.close()

# sets html to a soup
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a', href=True): 
    i=i+1
    print(link['href'])
ik=0
for link in soup.find_all('a', attrs={"target"}): 
    ik=i+1

print(i, ik)