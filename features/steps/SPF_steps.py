from behave import when, given, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('From page header, click "Search"')
def click_search_button(context):
    context.app.header.click_search_button()


@when('Search for the {item_text}')
def input_search_item(context, item_text):
    context.app.header.input_search_text(item_text)
    sleep(4)


@then('Verify the results have SPF')
def verify_spf_result(context):
    context.app.header.verify_spf_result()


