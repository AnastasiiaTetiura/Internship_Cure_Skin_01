import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

from support.logger import logger, MyListener

#Allure command:
#behave -f allure_behave.formatter:AllureFormatter -o test_report/ features/tests/SPF_search_result.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    #service = Service('/Users/anastasiiatetiura/MyInternshipCure/chromedriver')
    #service = Service('/Users/anastasiiatetiura/MyInternshipCure/geckodriver')  #------FIREFOX
    #context.driver = webdriver.Chrome(service=service)
    #context.driver = webdriver.Firefox(service=service)                         #-----FIREFOX

    ## -----CHROMe-----HEADLESS MODE ##
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('window-size=1366x768')
    #context.driver = webdriver.Chrome(
         #chrome_options=options,
         #service=service
    #)


    ## -----FIREFOX----HEADLESS MODE ##
    #options = FirefoxOptions()
    #options.add_argument('--headless')
    #context.driver = webdriver.Firefox(
        #options=options,
        #service=service
    #)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    #context.driver = EventFiringWebDriver(
         #webdriver.Chrome(service=service),
        # MyListener()
    #)
    # for headless mode ###
    #context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # BrowserStack
    bs_user = 'anastasiiatetiur_oSxFA0'
    bs_key = '2spffrK83i1Ne9zWpqT2'
    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_name
        }
    }
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.app = Application(driver=context.driver)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    #print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    #print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        #context.driver.execute_script(
            #'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
