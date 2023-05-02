from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    #service = Service('/Users/anastasiiatetiura/MyInternshipCure/chromedriver')
    service = Service('/Users/anastasiiatetiura/MyInternshipCure/geckodriver')  #------FIREFOX
    #context.driver = webdriver.Chrome(service=service)
    #context.driver = webdriver.Firefox(service=service)                         #-----FIREFOX

    ## HEADLESS MODE ####

    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('window-size=1366x768')
    #context.driver = webdriver.Chrome(
         #chrome_options=options,
         #service=service
    #)


    ## -----FIREFOX----HEADLESS MODE ####
    options = FirefoxOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Firefox(
        options=options,
        service=service
    )





    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
