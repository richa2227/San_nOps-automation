from selenium import webdriver
from webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By


class DeleteCreatedDashboard():

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.pageTitle_text_xpath = "//h1[contains(text(),'Dashboards')]"
        self.firstDashboard_inList_xpath = "//*[@id='root']/div/div/div[4]/div/div/div/div/div/div/div[" \
                                           "2]/div/div/div[1] "
        self.deleteIcon_id = "Delete-0"
        self.delete_dailogBox_xpath = "//div[@role='dialog']"
        self.confirmDelete_button_id = "modalDelete"

    def navigation_homepage(self):
        self.driver.back()
        # self.driver.get("https://uat.nops.io/v3/dashboard/list")
        self.wait.until(expected.presence_of_element_located((By.XPATH, self.pageTitle_text_xpath)))

    def verify_created_dashboard_delete_it(self, dashboardname):
        # Verify dashboard in list
        first_cell = self.driver.find_element_by_xpath(self.firstDashboard_inList_xpath)
        name_of_first_cell = first_cell.text
        print(name_of_first_cell)

        if name_of_first_cell == dashboardname:
            # Delete created Dashboard4
            delete_icon = self.driver.find_element_by_id(self.deleteIcon_id)
            delete_flag = delete_icon.is_displayed()  # delete_icon
            print(delete_flag)
            self.driver.implicitly_wait(5)
            self.wait.until(expected.element_to_be_clickable((By.ID, self.delete_icon)))
            self.driver.find_element_by_id(self.deleteIcon_id).click()
            # wait.until(expected.presence_of_element_located((By.XPATH, self.delete_dailogBox_xpath)))
            self.driver.find_element_by_id(self.confirmDelete_button_id).click()  # delete_btn
            page_title_text = self.driver.find_element_by_xpath(self.pageTitle_text_xpath)
            self.wait.until(expected.visibility_of(page_title_text), "time out")

        else:
            print('dashboard list has not been updated')
