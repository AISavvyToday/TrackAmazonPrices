import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.com/Apple-iPhone-GSM-Unlocked-64GB/dp/B0775MV9K2/ref=lp_18637575011_1_1?srs=18637575011&ie=UTF8&qid=1583746873&sr=8-1'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36 OPR/67.0.3575.31'}

def check_price():
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	price = soup.find(id='priceblock_ourprice').get_text()
	converted_price = float(price[0:5])

	print(converted_price.strip())

	if converted_price < 1.700:
		send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()

	server.starttls()
	server.ehlo()

	server.login('jacmuhuri@gmail.com', '0712472060')

	subject = 'Price Went Down'
	body = 'Check the amazon link: https://www.amazon.com/Apple-iPhone-GSM-Unlocked-64GB/dp/B0775MV9K2/ref=lp_18637575011_1_1?srs=18637575011&ie=UTF8&qid=1583746873&sr=8-1'
	msg = f'Subject: { subject }\n\n{ boddy }'

	server.sendmail(
		'jacmuhuri@gmail.com',
		'muhuri.json@gmail.com',
		msg

		)
	print('Email sent')

	server.quit()


while(True):
	check_price()
	time.sleep()


