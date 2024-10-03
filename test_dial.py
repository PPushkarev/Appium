import time

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
    appPackage='com.google.android.dialer',
    appActivity='com.android.dialer.main.impl.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield android_driver
    android_driver.quit()


def test_dial_number(driver) -> None:
    driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='key pad').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="5"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="4"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="4"]').click()
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="1"]').click()
    driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/dialpad_voice_call_button').click()
    stop_phone = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="End call"]'))
    )
    assert stop_phone.is_displayed(), 'Dial is not successful'
    stop_phone.click()
