#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_livros = []


# In[3]:


def pegaLivros(livros):
    contador = 0
    for livro in livros:
        titulo = livro.find(itemprop='name')
        link = livro.find('meta')
        autor = livro.find(itemprop='author')
        real = livro.find('div', attrs={'class':'precos'})
        novos = livro.find('div', attrs={'class':'quantidades'})
        por = livro.find('span', attrs={'class':'precos'})
    

        print('Titulo do Produto:', titulo.text)
        print('Link do Produto:', link['content'])
        print('Autor do Produto:', autor.text)
        print('Preço do Produto:', real.text)
        print('Produtos Novos:', novos.text)
    
    
        site2 = requests.get(link['content'])
        soup2 = BeautifulSoup(site2.content, 'html.parser')
        nota = soup2.find('span', attrs={'class':'stars-info'})
        if (nota == None):
            print('Nenhuma Avaliação!')
            lista_livros.append([titulo.text, link['content'], autor.text, real.text, novos.text])  
        else:
            print('Avaliações:', nota.text)
            lista_livros.append([nota.text])  
            
        tipo = soup2.find('div', attrs={'class':'info-container'})  
        if(tipo == None):
            print('\n Sem mais informações. \n')
            lista_livros.append([titulo.text, link['content'], autor.text, real.text, novos.text, nota.text]) 
        else:
            print(tipo.text)            
            lista_livros.append([tipo.text])
        
        desc = soup2.find('span', attrs={'class':'description-text'})
        if(desc == None):
            print('\n Sem mais informações \n')
            lista_livros.append([titulo.text, link['content'], autor.text, real.text, novos.text, nota.text]) 
        else:
            print(desc.text)
            lista_livros.append([desc.text])
            
            
            
        contador = contador + 1
    print("Número de livros encontrados:", contador) 
def pegaSite(URL):
    site = requests.get(URL)
    soup = BeautifulSoup(site.content, 'html.parser')
    return soup

URL_Base = 'https://www.estantevirtual.com.br'

pesquisa = '/busca?q=' + input('Digite o nome do livro: ')

URL = URL_Base + pesquisa

soup = pegaSite(URL)

livros = soup.find_all('a', class_ = 'livro')

pegaLivros(livros)

flag_prox = soup.find('a', attrs={'class':'next'})

while(len(flag_prox['class']) != 4):
        proxima_pagina = soup.find('a', class_ = 'next')
        URL_prox = URL_Base + proxima_pagina['href']
        soup = pegaSite(URL_prox)
        livros = soup.find_all('a' , class_ = 'livro')
        pegaLivros(livros)
        flag_prox = soup.find('a', attrs={'class':'next'})
    
print('\n\n')


# In[ ]:





# In[ ]:


estante = pd.DataFrame(estante)


# In[ ]:


print(estante)


# In[ ]:


estante.to_csv('estante.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




