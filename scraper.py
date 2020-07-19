import requests # for making standard html requests
from bs4 import BeautifulSoup # magical tool for parsing html data
import json # for parsing data
from pandas import DataFrame as df # premier library for data organization

page = requests.get("https://scrapethissite.com/pages/simple/")
soup = BeautifulSoup(page.text, 'html.parser')
page.encoding = 'ISO-885901'
countries_list = []
country_name_list = soup.find_all(attrs={'class':'country-name'})
country_capital_list = soup.find_all(attrs={'class':'country-capital'})
country_population_list = soup.find_all(attrs={'class':'country-population'})
country_area_list = soup.find_all(attrs={'class':'country-area'})
control = 0
country_area_list.__getitem__
for i in country_name_list:
    country_name = country_name_list.__getitem__(control).text.strip()
    country_capital = country_capital_list.__getitem__(control).text.strip()
    country_population = int(float(country_population_list.__getitem__(control).text.strip()))
    country_area = int(float(country_area_list.__getitem__(control).text.strip()))
    myObj = {"Country": country_name, "Capital":country_capital, "Population":country_population, "Area": country_area}
    countries_list.append(myObj)
    control += 1

# print(countries_list)
countries_list_json = json.dumps(countries_list)
print(countries_list_json)
with open('data.JSON', 'w') as outfile:
    json.dump(countries_list, outfile)