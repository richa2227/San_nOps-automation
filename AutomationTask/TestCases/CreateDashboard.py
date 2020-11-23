import time
import unittest

from selenium import webdriver
from webdriver.common.action_chains import ActionChains
from webdriver.common.keys import Keys
from webdriver.support.ui import WebDriverWait

from AutomationTask.Pages.dashboarPage import CreateDashboardPage
from AutomationTask.Pages.deleteDashboard import DeleteCreatedDashboard
from AutomationTask.Pages.loginPage import LoginPage

DashboardName = "Automation Demo Dashboard123789"


class CreateDashboards(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:/San QA/AutomationTask/Drivers/chromedriver_87.exe")
        cls.wait = WebDriverWait(cls.driver, 2000)
        cls.action = ActionChains(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.dashboard = CreateDashboardPage(cls.driver, cls.wait)
        cls.delete = DeleteCreatedDashboard(cls.driver, cls.wait)  # Create Page objects

        cls.driver.get("https://uat.nops.io/v3/dashboard/list")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_Step1_login(self):
        # Login
        self.login.enter_username("san+richatest@nclouds.com")
        self.login.enter_password("richa@123")
        self.login.click_loginbtn()
        time.sleep(20)
        self.dashboard.verify_visibility_of_elements()

    def test_Step2_createNewDashboard(self):
        # Create Dashboard
        self.dashboard.create_dashboard(DashboardName)
        self.driver.implicitly_wait(10)

    def test_Step3_addSubBlock(self):
        # Add blocks and items
        self.dashboard.add_subBlock_items()
        self.driver.implicitly_wait(5)

    def test_Step4_addRules(self):
        # Add Rule and sub blocks in it
        self.dashboard.add_rules_subBlocks()
        self.driver.implicitly_wait(5)
        self.action.send_keys(Keys.HOME).perform()

    def test_Step5_cloneBlock(self):
        # Clone the block
        self.dashboard.cloneBlock()
        self.action.send_keys(Keys.HOME).perform()

    def test_Step6_saveDashboard(self):
        # Save create dashboard
        self.dashboard.save_created_dashboard()
        time.sleep(2)

    def test_step7_share_dashboard_with_email_ID(self):
        # share dashboard
        self.dashboard.share_dashboard()

    def test_Step8_navigateBackToListPage(self):
        # Navigation to listpage
        self.delete.navigation_homepage()
        time.sleep(4)

    def test_Step9_verifyCreatedDashboardInList(self):
        # Verify created Dashboard in list and then delete it
        self.delete.verify_created_dashboard_delete_it(DashboardName)

    @classmethod
    def tearDownClass(cls) -> None:
        # Close the browser
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

