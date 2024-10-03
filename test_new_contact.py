import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.contacts',
    appActivity='com.google.android.apps.contacts.activities.PeopleActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield android_driver
    android_driver.quit()
#

def test_get_new_contact(driver) -> None:
    first_name_before = 'Edvard'
    last_name_before = "Norton"
    name_before = (first_name_before + last_name_before)
    start = WebDriverWait(driver, 6).until(
        EC.element_to_be_clickable((AppiumBy.ID, 'com.google.android.contacts:id/floating_action_button')))
    start.click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]').send_keys(first_name_before)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Last name"]').send_keys(last_name_before)
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("09090909")
    driver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/toolbar_button').click()
    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((AppiumBy.ID, 'android:id/closeButton')))
    close_button.click()
    name_after = driver.find_element(by=AppiumBy.ID, value='com.google.android.contacts:id/large_title').text
    assert name_before == name_after.replace(" ", ""), 'We got different names'
