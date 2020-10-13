from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver=webdriver.Chrome(options=chrome_options)
driver=webdriver.Chrome()
stock='آپ'
driver.get('http://www.tsetmc.com/Loader.aspx?ParTree=111C1417')
name=driver.find_elements_by_css_selector('td:nth-child(7)')
code=driver.find_elements_by_css_selector('td:nth-child(1)')
for i in range(len(name)):
    if name[i].text==stock:
        stockcode=code[i].text
        break
driver.close()
driver=webdriver.Chrome()
driver.get(f'https://www.nahayatnegar.com/tv/{stockcode}')
driver.save_screenshot(f"{stock}.png")

maximize=driver.find_element_by_css_selector('iframe')
size=maximize.size
location=maximize.location
x = location['x']
y = location['y']
width = location['x']+size['width']
height = location['y']+size['height']
im = Image.open(f'{stock}.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save(f'{stock}.png')

driver.quit()

