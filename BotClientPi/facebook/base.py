from bot_service.resrc_service import get_facebook_user
from http.cookies import SimpleCookie
from selenium import webdriver
class Facebook:
    def __init__(self,acction_script,driver_path,cookie,driver_type,facebook_id,username):
        self.driver_path = driver_path
        self.cookie = cookie
        self.facebook_id = facebook_id
        self.username = None
        self.driver_type = driver_type
        self.action_script = None
        self.facebook_action_list = []
        self.driver = None
        self.get.driver() 

    def get_driver(self):
        if self.driver_type == 1:
            self.driver = webdriver.Firefox(executable_path=r'/home/quan/Desktop/Python/Django/mmo_system/geckodriver')         

     def set_action_list(self,action_script_list):
            self.facebook_action_list = action_script_list

    def get_action_script(self):
        pass

    def exe_action_script(self):
        pass

    def update_status_to_server(self):
        pass

    def logging_acount(self):
        pass
    
    def login(self):
        self.driver.get("https://www.facebook.com/")
        rawdata = self.cookie
        cookie = SimpleCookie()
        cookie.load(rawdata)

        for key, morsel in cookie.items():
            self.driver.add_cookie({'name':key,'value':morsel.value})
        self.driver.get("https://www.facebook.com/")
    
    def logout(self):
        self.driver.close()

    def get_facebook_user_account(self):
        data_user = get_facebook_user()
        if data_user['is_email']:
            self.username = data_user['email']
        else:
            self.username = data_user['phone']
        # self.username = data_user['']

    def like_facbook_post_by_id(self):
        pass
