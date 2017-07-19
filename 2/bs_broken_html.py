from bs4 import BeautifulSoup
broken_html = '<ul class=country><li>Area<Li>Population</ul>'

soup = BeautifulSoup(broken_html,'html.parser')
fixed_html = soup.prettify()

ul = soup.find('ul',attrs={'class':'country'})
#ul.find('li')
print ul.find_all('li')


