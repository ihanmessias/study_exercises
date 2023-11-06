# -~ Import Libs ~-
import requests
import pandas as pd
from bs4 import BeautifulSoup

# -~ Web Scraping ~-
def ibge_scraping(uf: str): 
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    page = requests.get(uf_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    ind = soup.select('.indicador')

    ind_dict = {
        dado.select('.ind-label')[0].text:dado.select('.ind-value')[0].text for dado in ind
    }

    for i in ind_dict:
        if ']' in ind_dict[i]:
            ind_dict[i] = ind_dict[i][:-9]

    df = pd.DataFrame(list(ind_dict.items()), columns=['Indicador', 'Valor'])
    return df

print(ibge_scraping('df'))