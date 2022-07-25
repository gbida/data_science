import os

from bs4 import BeautifulSoup
from selenium import webdriver


os.chdir('C:\\Users\\lh\\Downloads\\chromedriver_win32')  # excutable path will be deprecated
driver = webdriver.Chrome()
driver.get('https://www.coffeebeankorea.com/store/store.asp')
driver.execute_script('storePop2(1)')  # 학동역(DT)점 정보

# html preview 또는 debugging으로 저장한 html 데이터 확인
html = driver.page_source
bsObj = BeautifulSoup(html, 'html.parser')