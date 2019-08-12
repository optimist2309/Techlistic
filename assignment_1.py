"""
Assignment 1: Automate Your First Selenium Webdriver Script using Browser Commands
- July 19, 2019
Automate using Browser Selenium Commands - Launch browser, maximize, validate page title and close browser. It should be your first webdriver script.

Assignment Level - Beginner

Steps to Automate:


1. Open this link - https://www.techlistic.com/

2. Launch Firefox browser. (You can choose browser of your choice).

3. Maximize or set size of browser window.

4. Get Title of page and validate it with expected value.

5. Get URL of current page and validate it with expected value.

6. Get Page source of web page.

7. And Validate that page title is present in page source.

8. Close browser.
"""
from selenium import webdriver

driver = webdriver.Chrome()
url_page = "https://www.techlistic.com/"

driver.get(url_page)
driver.maximize_window()

title_value = "Techlistic"
title_from_broswer =driver.title

if title_value == title_from_broswer:
    print("Title is validated")
else :
    print("Title is not validated")

url_from_broswer = driver.current_url


if url_from_broswer == url_page:
    print("URL is validated")
else :
    print("URL is not validated")
    
source_web_page = driver.page_source
unicode_issue = source_web_page.encode('ascii','ignore')
web_page_str = str(unicode_issue)

if "<title>Techlistic</title>" in web_page_str:
    print("Title is in web page source")
else:
    print("Title is not in web page source source")

driver.close()

    
    

