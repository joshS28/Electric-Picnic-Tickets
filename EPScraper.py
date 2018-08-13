from requests import get
from bs4 import BeautifulSoup
import os
import time

# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

url = 'https://www.adverts.ie/for-sale/q_Electric+picnic/sortby_best_refresh_date-desc/'

response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)
movie_containers = html_soup.find_all('div', class_ = 'sr-grid-cell quick-peek-container')
#print(type(movie_containers))
#print(len(movie_containers))
first_movie = movie_containers[0]
#print(first_movie)


price1 = first_movie.find('div', class_ = 'price')
#print(price1)
price = price1.a.text
print(price)

pri = price[1:]
print(pri)

title1 = first_movie.find('div', class_ = 'title')
title = title1.a.text
print(title)

loc1 = first_movie.find('div', class_ = 'location')
#print(loc1)
loc = loc1.a.text
print(loc)

test = '"{}"'.format(pri)
print(test)

test1 = '"{}"'.format(title)
test2 = '"{}"'.format(loc)



#test = loc1.a[1]
#print(test)

#loc2 = loc1.find('a', class_ = 'location')
#loc2 = loc1.a[1]
#print(loc2)
# Calling the function
notify(title    = test1,
       subtitle = test,
       message  = test2)


while True:
	url = 'https://www.adverts.ie/for-sale/q_Electric+picnic/sortby_best_refresh_date-desc/'

	response = get(url)

	html_soup = BeautifulSoup(response.text, 'html.parser')
	type(html_soup)
	movie_containers = html_soup.find_all('div', class_ = 'sr-grid-cell quick-peek-container')
	#print(type(movie_containers))
	#print(len(movie_containers))
	first_movie = movie_containers[0]
	#print(first_movie)


	price1q = first_movie.find('div', class_ = 'price')
	#print(price1)
	priceq = price1q.a.text
	print(priceq)

	priq = priceq[1:]
	print(priq)

	title1q = first_movie.find('div', class_ = 'title')
	titleq = title1q.a.text
	print(titleq)

	loc1q = first_movie.find('div', class_ = 'location')
	#print(loc1)
	locq = loc1q.a.text
	print(locq)

	testq = '"{}"'.format(priq)
	print(testq)

	test1q = '"{}"'.format(titleq)
	test2q = '"{}"'.format(locq)

	if(title!=titleq):
		notify(title    = test1q,
       	subtitle = testq,
       	message  = test2q)
    


	time.sleep(60)



	



#print(response.text[:500])