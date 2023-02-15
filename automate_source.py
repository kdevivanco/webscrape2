import os
import shutil
from selenium import webdriver

translated_dir = '/Users/macbookpro/Desktop/Programacion/AllStars2/www.classcentral.com'
copy_dir = '/Users/macbookpro/Desktop/final_translated'

driver = webdriver.Chrome()

html_files = [f for f in os.listdir(translated_dir) if f.endswith('.html')]

for file in html_files:
    file_path = os.path.join(translated_dir, file)
    driver.get("file:///" + file_path)
    
    driver.execute_script("return document.readyState") == "complete"
    
    html = driver.page_source
    
    copy_path = os.path.join(copy_dir, file)
    with open(copy_path, "w", encoding="utf-8") as f:
        f.write(html)

driver.quit()