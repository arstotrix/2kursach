from bs4 import BeautifulSoup

def body_out(fname): #достаём тело из текста
    with open(fname, encoding= 'utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
    body = soup.find('body')
    return body
def main():
    body = body_out('Ham.xml')
    divs = body.tei.findall('div')
    print(divs)
if __name__ == '__main__':
    main()


