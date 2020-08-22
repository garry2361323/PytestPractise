import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    logger = LogGen.loggen()
    def test_homePageTitle(self, setup):
        self.logger.info("*********************************Test_001_Login*************************************")
        self.logger.info("*********************************test_homePageTitle*************************************")
        self.driver = setup
        self.driver.get(ReadConfig.getApplicationURL())
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(ReadConfig.getApplicationURL())
        self.loginObject = LoginPage(self.driver)
        self.loginObject.setusername(ReadConfig.getUsername())
        self.loginObject.setpassword(ReadConfig.getPassword())
        self.loginObject.login()
        act_title = self.driver.title
        self.driver.close()
        print(act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
