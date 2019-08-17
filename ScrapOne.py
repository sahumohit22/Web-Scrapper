from bs4 import BeautifulSoup
import requests
import urllib.request 

product = input("enter product to search:\n")

my_url = 'https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'.format(product)

response = requests.get(my_url)

page_html = response.text

soup = BeautifulSoup(page_html , "html.parser")

containers = soup.findAll("div", {"class": "_3O0U0u"})

#create file Product.csv
filename = "products.csv"
f = open(filename , "w")

headers = "Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
	product_name = container.div.img["alt"]

	price_container = container.findAll("div",{"class": "col col-5-12 _2o7WAb"})
	price = price_container[0].text.strip()

	rating_container = container.find("div",{"class":"hGSR34"})
	rating = rating_container.text

	#string parsing
	#remove comma
	trim_price = ''.join(price.split(','))

	#create list of element seperated by "₹"
	rm_rupee = trim_price.split("₹")
	add_rs_price = "Rs." + rm_rupee[1]
	
	#create list 
	split_price = add_rs_price.split('E')
	final_price = split_price[0]

	print(product_name.replace(",", "|") + " , " + final_price + " , " + rating + "\n")
	f.write(product_name.replace(",", "|") + " , " + final_price + "," + rating + "\n")

f.close() 
