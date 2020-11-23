from webdriver.support.ui import WebDriverWait
from webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from webdriver.common.keys import Keys


class CreateDashboardPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.pageLogo_xpath = "//div[@id='logo']"
        self.createDashboard_button_id = "createNewDashboard"
        self.dashboard_textbox_id = "enterName"
        self.next_button_id = "modalNext"

        self.subBlock_button_cssSelector = "#addNewBlock-0"
        self.checkbox1_subBock_xpath = "//div/label[@id='rule-label-title-0']"
        self.checkbox2_subBock_xpath = "//div/label[@id='rule-label-title-1']"
        self.confirm_button_subBlock_ID = "modalConfirm"

        self.addRule_button_id = "addBlock"
        self.ruleName_textbox_id = "blockName"
        self.ruleDescription_textbox_id = "blockDescription"
        self.createRule_button_id = "modificationButton"
        self.add_subBlock_inRule_cssSelector = "#addNewBlock-1"
        self.checkbox_inRule_cssSelector = "#rule-label-title-0"
        self.confirm_subBlock_inRule = "modalConfirm"

        self.first_clone_button_cssSelector = "#cloneRueBlock-0"

        self.save_button_cssSelector = "#modifyDashboard"
        self.classToBeInvisible_classname = "np-content np-cReports np-rulesDash np-nops-loading"

        self.share_button_id = "share"
        self.email_textbox_id = "email"
        self.email_textbox_xpath = "//*[@id='email']/div/div[1]"
        self.send_button_id = "modalShareReport"

    def verify_visibility_of_elements(self):
        self.wait.until(expected.presence_of_element_located((By.XPATH, self.pageLogo_xpath)))
        self.wait.until(expected.element_to_be_clickable((By.ID, self.createDashboard_button_id)))
        self.wait.until(expected.invisibility_of_element((By.CLASS_NAME, self.classToBeInvisible_classname)))

    def create_dashboard(self, dashboardname):
        self.driver.find_element_by_id(self.createDashboard_button_id).click()
        self.driver.find_element_by_id(self.dashboard_textbox_id).send_keys(dashboardname)
        self.driver.find_element_by_id(self.next_button_id).click()

    def add_subBlock_items(self):
        # Add sub block and few items in it
        self.driver.find_element_by_css_selector(self.subBlock_button_cssSelector).click()  # sub_block_tab
        self.driver.find_element_by_xpath(self.checkbox1_subBock_xpath).click()  # checkbox_1
        self.driver.find_element_by_xpath(self.checkbox2_subBock_xpath).click()  # checkbox_1
        self.driver.find_element_by_id(self.confirm_button_subBlock_ID).click()  # confirm checkbox for rule block

    def add_rules_subBlocks(self):
        # Add rules and block in it
        self.driver.find_element_by_id(self.addRule_button_id).click()  # rule_block_tab
        self.driver.find_element_by_id(self.ruleName_textbox_id).send_keys("New Rules")
        self.driver.find_element_by_id(self.ruleDescription_textbox_id).send_keys("Rule Description")
        self.driver.find_element_by_id(self.createRule_button_id).click()
        self.driver.find_element_by_css_selector(self.add_subBlock_inRule_cssSelector).click()
        self.driver.find_element_by_css_selector(self.checkbox_inRule_cssSelector).click()
        self.driver.find_element_by_id(self.confirm_subBlock_inRule).click()

    def cloneBlock(self):
        # clone block
        self.driver.find_element_by_css_selector("#cloneRueBlock-0").click()

    def save_created_dashboard(self):
        # Save dashboard
        self.driver.find_element_by_css_selector(self.save_button_cssSelector).click()
        self.wait.until(expected.element_to_be_clickable((By.CSS_SELECTOR, self.save_button_cssSelector)))

    def share_dashboard(self):
        # Share with someone
        self.driver.find_element_by_id(self.send_button_id).click()  # Will open share dialog box
        self.driver.implicitly_wait(10)
        flag = self.driver.find_element_by_id(self.email_textbox_id).is_displayed()  # Will check email textbox
        print(flag)
        self.driver.find_element_by_xpath(self.email_textbox_xpath).click()  # User will able to input
        # self.action.send_keys_to_element(self.driver.find_element_by_xpath(self.email_textbox_xpath),
        # "richa" ).perform()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys("richa")
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(Keys.ENTER)  # will select the value from the
        # dropdown
        self.driver.find_element_by_id(self.email_textbox_id).click()  # Close dropdown
        self.driver.find_element_by_id(self.send_button_id).click()
