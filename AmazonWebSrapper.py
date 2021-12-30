from selenium import webdriver
from bs4 import *
import pandas as pd

from webdriver_manager.chrome import ChromeDriverManager



products=[] #List to store name of the product


inp = input("Enter anything")

inp= inp.split()

new = "+".join(inp)
print(new)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.amazon.in/s?k=" + new + "&crid=2O39X0YLRAEI0&sprefix=samsung%2Caps%2C233&ref=nb_sb_noss_1")


content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
    
for a in soup.findAll("span", attrs={"class":'a-size-medium a-color-base a-text-normal'}):
    a = str(a)
    a = a.split('>')
    a = a[1]
    a = a.split('<')
    a = a[0]
    products.append(a)
 


#database printed
print(products)

#finally stored all output in csv file
df = pd.DataFrame({'Product Name':products}) 
df.to_csv('products.csv', index=False, encoding='utf-8') 

