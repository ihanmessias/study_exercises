from bs4 import BeautifulSoup

with open('./asimov_ex.html') as file:
    conteudo = file.read()
    
ex = BeautifulSoup(conteudo, 'lxml')
print(ex)

# Capturando primeiro paragrafo:
ex.find('p')
# Capturando list com todos os paragrafos:
ex.find_all('p')
# Capturando tudo dentro do Body:
ex.find_all('body')
# Capturando todas as tag com class="um"
tags = ex.find_all(class_='um')

for tag in tags:
    print(tag)
    
for tag in tags:
    print(tag.text)