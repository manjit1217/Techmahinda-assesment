import pytest
import os
from appium import webdriver
os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4728")
@pytest.fixture(scope='session', autouse=True)
def android_driver(request):
    from appium import webdriver
    app_apk = ('file_apk/Amazon_shopping.apk')
    android_driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4728/wd/hub',
        desired_capabilities={
            'app': app_apk,
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'Oneplus5',
            'appPackage': 'pkgName'
        }
    )
    yield android_driver

    android_driver.close()
