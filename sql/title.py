from urllib.request import Request, urlopen
import ssl
from bs4 import BeautifulSoup

# The URL we want to scrape
url = 'https://www.abc.net.au/news/justin'

#################################################
#################################################
### COPY/PASTE THIS BLOCK AS IS

# Open URL (i.e., make request) + disguise agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
req = Request(url, headers=headers)
context = ssl._create_unverified_context()

# To fetch html and store in variable 'html'
uClient = urlopen(req, context=context)
html = uClient.read()  # html is stored in variable html
uClient.close()

#################################################
#################################################

### Interpret the page source as html
soup = BeautifulSoup(html, 'html.parser')

### Find the hyperlinks (href) in all of these <a>-tags and store them in the variable hyperlink

titles = soup.find_all('a','_3T9Id _2f8qj FQVx7 _2tPjN _1QHxY _3OwCD')

with open(r"titles.txt", "w",encoding='utf-8') as file:
    for title in titles:
        file.write(title.string+'\n\n')

contents = soup.find_all('div','_3P1Sq _1deB8 _1hGzz _1-RZJ _1yL-m')

with open(r"contents.txt", "w",encoding='utf-8') as file:
    for content in contents:
        file.write(content.string+'\n\n')
