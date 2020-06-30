import pytest
from POM import LoginPage
from Utility import ReadDatafromexcel
obj_login_page=LoginPage.LoginPage
@pytest.mark.usefixtures('android_driver')
def test_login(android_driver):
    expected_result=ReadDatafromexcel.read_data_excel(1,1)
    actual_result=obj_login_page.login(android_driver)
    assert actual_result,expected_result
@pytest.mark.usefixtures('android_driver')
def test_search_tv(android_driver):
    expected_result=ReadDatafromexcel.read_data_excel(2,1)
    actual_result=obj_login_page.search_tv(android_driver,expected_result,22)
    assert actual_result, expected_result
@pytest.mark.usefixtures('android_driver')
def test_search_tv_randomly(android_driver):
    expected_result = ReadDatafromexcel.read_data_excel(3, 1)
    actual_result=obj_login_page.select_one_tv_randomly(android_driver,22)
    assert actual_result,expected_result
def  test_tv_detail_verify(android_driver):
    expected_result = ReadDatafromexcel.read_data_excel(4, 1)
    actual_result = obj_login_page.tv_detail_verify(android_driver, 22)
    assert actual_result, expected_result
def test_proced_till_check_out(android_driver):
    expected_result = ReadDatafromexcel.read_data_excel(5, 1)
    actual_result = obj_login_page.proceed_till_check_out(android_driver)
    assert actual_result, expected_result
def test_check_out_order_detail(android_driver):
    expected_result = ReadDatafromexcel.read_data_excel(6, 1)
    actual_result = obj_login_page.check_out_order_detail(android_driver)
    assert actual_result, expected_result







