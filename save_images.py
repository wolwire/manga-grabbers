import urllib
import urllib.request
from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
from PIL import Image

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
manga = "jojos-bizarre-adventure-part-6-stone-ocean-vol-1"
if not os.path.isdir(f"D:/{manga}"):
		os.mkdir(f"D:/{manga}")
		os.mkdir(f"D:/{manga}/pdf-mangas")

nav_next = "https://read.j-o-j-o.com/manga/jojos-bizarre-adventure-part-6-stone-ocean-vol-1/"
manga_name = "jojos-bizarre-adventure-part-6-stone-ocean-vol-1"
while(nav_next):
	html_page = urllib.request.urlopen(nav_next).read()
	soup = BeautifulSoup(html_page, 'html.parser')
	img = soup.findAll("img", class_="lazyload")
	
	
	if not os.path.isdir(f"D:/{manga}/{manga_name}"):
		os.mkdir(f"D:/{manga}/{manga_name}")
	count = 1
	im_list = []
	for i in img:
		count = count+1
		# image = i.find('img')
		src = i.get('data-src')
		a = urlparse(src)
		urllib.request.urlretrieve(src, f"D:/{manga}/{manga_name}/{os.path.basename(a.path)}")
		cover = Image.open(f"D:/{manga}/{manga_name}/{os.path.basename(a.path)}")
		cover = cover.convert('RGB')
		im_list.append(cover)
	im_list[0].save(f'D:/{manga}/pdf-mangas/{manga_name}.pdf',save_all=True, append_images=im_list[1:])
	next_link = soup.find('div', class_="nav-next").find('a')
	nav_next = next_link.get('href')
	manga_name = next_link.find("span", class_="post-title").get_text()
	print(manga_name, nav_next)
	