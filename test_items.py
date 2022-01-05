import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_search_button_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements_by_css_selector('button.btn.btn-add-to-basket')
    assert button , '!!!FATAL - btn-add-to-basket NOT FOUND!!!'  
    time.sleep(5) 