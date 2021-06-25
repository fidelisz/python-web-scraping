import requests
from bs4 import BeautifulSoup

def pegaProdutos(produtos):
    contador = 0
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-4'})
        link = produto.find('a', attrs={'class':'a-link-normal s-no-outline'})
        print('Titulo do produto:', titulo.text)
        print('Link do Produto:', link['href'])
        preco = produto.find('span', attrs={'class':'a-price-whole'})
        if(preco):
            decimas = produto.find('span', attrs={'class':'a-price-fraction'})
            print('Preço: R$', preco.text + decimas.text)
        else:
            print('Sem preço!')
        nota = produto.find('span', attrs={'class':'a-declarative'})
        if(nota):
            print(nota.text)
        else:
            print('Sem Avaliação!')
        autor = produto.find('div', attrs={'class':'a-row a-size-base a-color-secondary'})
        if(autor):
            print(autor.text)
        else:
            print('Sem autor')

        print('\n\n')
        contador = contador + 1
    print("Número de produtos encontrados:", contador) 

    
def pegaSite(URL):
    site = requests.get(URL)
    while(site.status_code != 200):
        site = requests.get(URL)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup

URL = 'https://www.amazon.com.br/s?k='
pesquisa = input('Digite o nome do produto: ')
URL = URL + pesquisa + '&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss'
soup = pegaSite(URL)
produtos = soup.find_all('div', class_ = 'a-section a-spacing-medium')




pegaProdutos(produtos)

flag_prox = soup.find('li', attrs={'class':'a-disabled a-last'})

while(flag_prox == None):
        proxima_pagina = soup.find('li', class_ = 'a-last').find('a')
        URL_prox = 'https://www.amazon.com.br' + proxima_pagina['href']
        soup = pegaSite(URL_prox)
        produtos = soup.find_all('div', class_ = 'a-section a-spacing-medium')
        pegaProdutos(produtos)
        flag_prox = soup.find('li', attrs={'class':'a-disabled a-last'})

   

   

