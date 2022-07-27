"""괌 사이판 여행 연관 키워드 찾기"""

import time
import urllib
import requests
import platform
import matplotlib.pyplot as plt

from platform import platform
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud


# 한글 분석을 위한 font path 설정
if platform.system() == 'Windows':
	path = r'c:\Windows\Fonts\malgun.ttf'
elif platform.system() == 'Darwin':
	path = r'/System/Library/Fonts/AppleGothic'
else:
	path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'


session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'\
		   'AppleWebKit 537.36 (KHTML, like Gecko) Chrome',\
		   'Accept': 'text/html, application/xhtml+xml, application/xml;'\
		   'q=0.9, image/webp, */*; q=0.8'}

# url에 있는 한글 encoding
search_keyword = '괌 사이판 여행'
keyword_list = search_keyword.split()
keyword = ''
for k in keyword_list:
	keyword = keyword + urllib.parse.quote(k) + '+'
keyword = keyword.rstrip('+')

# scraping
bs = []
for n in range(1, 6):
	req = requests.get(f'https://search.daum.net/search?p={n}&q={keyword}&w=fusion&DA=PGD&period=6m&sd=20220126215757&ed=20220726215757')
	time.sleep(1)
	bsobj = BeautifulSoup(req.text, 'html.parser')

	# Daum 통합웹 탭에서 해당 키워드 검색 데이터
	bsobj = bsobj.find('ul', class_='list_info ty_doc')  
	bs.append(bsobj)

# html tag를 제외한 text만 추출
text = ''
for page in bs:
	page = page.text
	for k in keyword_list:
		text += page.replace(k, '')
text = text.replace('블로그', '').replace('카페', '').replace('웹문서', '')


# Open Korean Text 객체 생성
okt = Okt()

# 명사와 형용사만 noun_adj_list에 추가
sentences_tag = []
sentences_tag = okt.pos(text)
noun_adj_list = []
for word, tag in sentences_tag:
	if tag in ['Noun' , 'Adjective']:
		noun_adj_list.append(word)

# 가장 많이 나온 단어 40개 저장
counts = Counter(noun_adj_list)
tags = counts.most_common(40)

# WordCloud 생성
wc = WordCloud(font_path=path, background_color="white", max_font_size=50)
cloud = wc.generate_from_frequencies(dict(tags))

# WordCloud 출력
cloud.to_file('guam_sipan.png')
plt.figure(figsize=(10, 10))
plt.axis('off')
plt.imshow(cloud)
plt.show()
