from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # inputs = browser.find_elements_by_css_selector("input[required]")
    # for input in inputs:
    #     input.send_keys("some information")

    input1 = browser.find_element_by_css_selector("input.first[required]")
    input1.send_keys("first name")
    input2 = browser.find_element_by_css_selector("input.second[required]")
    input2.send_keys("last name")
    input3 = browser.find_element_by_css_selector("input.third[required]")
    input3.send_keys("email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(3)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
