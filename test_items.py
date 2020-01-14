import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_exist(browser):
    browser.get(link)
    time.sleep(10)
    result = browser.find_element_by_css_selector("#add_to_basket_form")
    assert len(result.text) > 0, "The button is not exist!"
