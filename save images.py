import urllib
import urllib.request
from urllib.parse import urlparse
import os
from selenium import webdriver


driver = webdriver.Chrome()
for k in range(131,336):
	driver.get(f'https://manga-boku-no-hero.com/manga/boku-no-hero-academia-chapter-{k}/')
	img = driver.find_elements_by_xpath('//picture/img')
	count = 1
	if not os.path.isdir(f"D:/manga-boku-no-hero/{k}"):
		os.mkdir(f"D:/manga-boku-no-hero/{k}")

	for i in img:
		count = count+1
		src = i.get_attribute('src')
		opener = urllib.request.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		urllib.request.install_opener(opener)
		a = urlparse(src)
		urllib.request.urlretrieve(src, f"D:/manga-boku-no-hero/{k}/{os.path.basename(a.path)}")

driver.close()