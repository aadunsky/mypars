import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cont = soup.find('section').find('div', class_='container')
    mynam = cont.find_all('h3', class_='title')
    urls = cont.find_all('a')
    sp = []
    for cpi in mynam: sp = cpi.text
    for up in urls:
        spis = up.get('href')
        nurl ='https://demigos.com/'+spis
        print(sp,' - ',nurl)
    print(type(nurl))



        #urls = c.urls.get('href')
        #data = {'names': names,'urls':urls}
        #print(data)
   #return html
    #for i in namesekc, urlsite:


def main():
    url = 'https://demigos.com/'
    get_data(get_html(url))

if __name__ == '__main__':
    main()
