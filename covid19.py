from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Navaneeth R\programs\web scraping\projects\chromedriver_win32\chromedriver.exe"
)
driver.get("https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?")
content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

countries = []
cases = []
new_cases = []

for data in soup.find_all("tr", {"class": "odd"}):
    country = data.find_all("td")[1]
    case = data.find("td", {"class": "sorting_1"})
    new = data.find_all("td")[3]
    countries.append(country.text)
    cases.append(case.text)
    new_cases.append(new.text)

for data in soup.find_all("tr", {"class": "even"}):
    country = data.find_all("td")[1]
    case = data.find("td", {"class": "sorting_1"})
    new = data.find_all("td")[3]
    countries.append(country.text)
    cases.append(case.text)
    new_cases.append(new.text)


driver.close()


print("Cases\tCountries\tNew Cases")
for i in range(len(countries)):
    print(cases[i], "\t", countries[i], "\t", new_cases[i])

