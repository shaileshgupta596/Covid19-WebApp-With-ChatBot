
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import schedule

#options = Options()
#options.add_argument("--headless")
#options=options
def selenium_work():
	link="https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen"
	driver = webdriver.Chrome()
	driver.get(link)
	time.sleep(2)
	statewise_info=driver.find_element_by_css_selector('table.pH8O4c')
	rows=statewise_info.find_elements_by_css_selector('tr.sgXwHf.wdLSAe.YvL7re')
	for row in rows:
		print(row.find_element_by_tag_name('th').text)
	driver.close()
#selenium_work()


	

