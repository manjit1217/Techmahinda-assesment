from Base import BasePage
from Utility import ReadPropertiesFile
#all xpath
login_phoneno = '//input[@id="ap_email_login"]'
login_continue_button='//span[contains(text(),"Continue")]'
login_password='//*[@id="ap_password"]'
login_button='//*[@id="signInSubmit"]'
greeting_name_after_login='//*[@id="nav-greeting-name"]'
search_field='//input[@id="nav-search-keywords"]'
get_all_TV_list='//*[@id="search"]/span[3]/div[2]'
select_TV_randomly_with_data_componentid='//*[@data-component-id="no"]'
get_all_the_tv_details_list='//*[@data-component-id="32"]//a[@title="product-detail"]//span'
get_tv_name_only='//*[@data-component-id="32"]//a[@title="product-detail"]/div/h2/span'
get_tv_price_only='//*[@data-component-id="32"]//a[@title="product-detail"]/div/div/span/span'
buy_now_button='//*[@id="buy-now-button"]'
time_slot_continue_button='//*[@id="a-autoid-1"]/span/input'
continue_button_after_selecting_payment='//*[@id="pp-w2XmMz-369"]/span/input'
check_out_order_now='//*[@id="spc-form"]/div/h1'
check_out_tv_name='//*[@id="spc-orders"]/div[1]/div[4]/div/div[1]/div[2]/div[1]/span/text()'
check_out_tv_price='//*[@id="subtotals-marketplace-table"]/tbody/tr[3]/td[2]/span'

obj_base_page=BasePage.BasePage
class LoginPage(BasePage):


    def login(self):
        phoneNo=ReadPropertiesFile.readproperty('LOGINDETAIL','PHONENUMBER')
        password = ReadPropertiesFile.readproperty('LOGINDETAIL', 'password')
        obj_base_page.set_text(self,login_phoneno,value=phoneNo)
        obj_base_page.click_element(self,locator=login_continue_button)
        obj_base_page.set_text(self,locator=password,value=password)
        obj_base_page.click_element(self,login_button)
        greeting_name=obj_base_page.get_text(self,greeting_name_after_login)
        return greeting_name
    def search_tv(self,search_name,tv_component_id):
        obj_base_page.set_text(self,locator=search_field,value=search_name)
        obj_base_page.key_press_from_keyboard(self,locator=search_field)
        tv_list=obj_base_page.get_elements(self,get_all_TV_list)
        return tv_list
    def select_one_tv_randomly(self,tv_component_id):
        tv_component_id=str(2)
        select_TV_randomly_with_data_componentid='//*[@data-component-id="'+tv_component_id+'"]'
        obj_base_page.scroll(self,select_TV_randomly_with_data_componentid,locx=0,locy=50)
        random_tv_name=obj_base_page.get_text(self,select_TV_randomly_with_data_componentid)
        return random_tv_name
    def tv_detail_verify(self,tv_component_id):
        get_all_the_tv_details_list = '//*[@data-component-id="'+tv_component_id+'"]//a[@title="product-detail"]//span/text()'
        get_tv_name_only = '//*[@data-component-id="'+tv_component_id+'"]//a[@title="product-detail"]/div/h2/span/text()'
        get_tv_price_only = '//*[@data-component-id="'+tv_component_id+'"]//a[@title="product-detail"]/div/div/span/span/text()'
        tv_name=obj_base_page.get_text(self,get_tv_name_only)
        tv_price=obj_base_page.get_text(self,get_tv_price_only)
        return tv_name,tv_price
    def proceed_till_check_out(self):
        obj_base_page.click_element(self,select_TV_randomly_with_data_componentid)
        obj_base_page.scroll(self,locy=0,locx=70,locator=search_field)
        obj_base_page.click_element(self,buy_now_button)
        obj_base_page.click_element(self,time_slot_continue_button)
        obj_base_page.click_element(self,continue_button_after_selecting_payment)
        oredr_heading=obj_base_page.get_text(self,check_out_order_now)
        return oredr_heading

    def check_out_order_detail(self):
        check_out_name=obj_base_page.get_text(self,check_out_tv_name)
        check_out_price=obj_base_page.get_text(self,check_out_tv_price)
        return check_out_name,check_out_price













