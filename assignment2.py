"""
Assignment 2: Automate Menu Links and Validate Page Titles using Selenium with Java
- July 22, 2019
Automate Menu Links and Validate Page Titles to verify that when clicking on menu links then users are landing on correct pages.

Assignment Level - Beginner

Steps to Automate:

1. Open this link  https://www.techlistic.com/

2. Launch Firefox browser. (You can choose browser of your choice).

3. Maximize or set size of browser window.

4. Click on 'Java Tutorial' link and validate page title.

5. Navigate back to Home Page.

6. Click on 'Selenium Tutorial' link and validate page title.

7. Navigate back to Home Page.

8. Click on 'Selenium Blogs' link and validate page title.

9. Navigate back to Home Page.

10. Click on 'TestNG Blogs' link and validate page title.

11. Close the browser.

"""



from selenium import webdriver

driver = webdriver.Chrome()
url_page = "https://www.techlistic.com/"

driver.get(url_page)
driver.maximize_window()
driver.find_element_by_link_text('JAVA').click()
java_page_title = "Java Tutorials Series - Java For Selenium"
title_from_broswer = driver.title

if java_page_title == title_from_broswer:
    print("Java Title is validated")
else :
    print("Java Title is not validated")
driver.back()

driver.find_element_by_link_text('SELENIUM').click()
selenium_page_title = "Selenium Tutorial - Learn Selenium from Comprehensive Series of 40 Coding Tutorials"
title_from_broswer = driver.title

if selenium_page_title == title_from_broswer:
    print("Selenium Title is validated")
else :
    print("Selenium Title is not validated")
driver.back()

driver.find_element_by_link_text('BLOG').click()
selenium_blog_page_title = "Top Selenium Blogs"
title_from_broswer = driver.title

if selenium_blog_page_title == title_from_broswer:
    print("Selenium Blog Title is validated")
else :
    print("Selenium Title is not validated")
driver.back()

driver.find_element_by_link_text('TestNG Tutorial').click()
test_ng_page_title = "Selenium with TestNG Integration - Tutorial Series"
title_from_broswer = driver.title

if test_ng_page_title == title_from_broswer:
    print("TestNG Blog Title is validated")
else :
    print("TestNG Title is not validated")
driver.back()

driver.close()


"""
This Commented Code is for to click on the links using find_elements but not implemented.
I will write this code later.
#from selenium.webdriver.common.by import By
link_locator = (By.TAG_NAME, "a")
all_hyper_link =  driver.find_elements(*link_locator)
for i in range(0 , len(all_hyper_link)):
        if all_hyper_link[i].get_attribute('text') == "TOP 10":
            print(all_hyper_link[i])
"""   




