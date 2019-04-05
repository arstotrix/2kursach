from bs4 import BeautifulSoup
with open('Ado.xml', encoding='utf-8') as f:
    text = f.read()
soup = BeautifulSoup(text, 'lxml')
body = soup.find('body')


print(type(body))
