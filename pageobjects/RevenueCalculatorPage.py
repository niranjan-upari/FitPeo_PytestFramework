from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RevenueCalculatorPage:

    def __init__(self, driver):
        self.driver = driver

    ele = (By.XPATH, "//h4[text()='Medicare Eligible Patients']")
    slider = (By.XPATH, "//span[contains(@class,'MuiSlider-thumb')]")
    number1 = (By.XPATH, "//input[@type='number']")
    reimbursement = (By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body2 inter css-1xroguk'][4]/p")

    # javascript to scroll to MedicalEligiblePatients keyword location,(slider section)
    def MedicalEligiblePatients(self):
        re = self.driver.find_element(*RevenueCalculatorPage.ele)
        return self.driver.execute_script('arguments[0].scrollIntoView(true)', re)

    # To drag slider
    def adjustSlider(self):
        adjust = self.driver.find_element(*RevenueCalculatorPage.slider)
        action = ActionChains(self.driver)
        return action.drag_and_drop_by_offset(adjust, 94, 0)
        # action.move_to_element(adjust).pause(1).click_and_hold(adjust).move_by_offset(94,0).release())
        # action.click_and_hold(adjust).pause(1).move_by_offset(94, 0).release())
        # return action.click_and_hold(adjust).pause(1).drag_and_drop_by_offset(adjust, 94, 0)

    # Location of sliders input box
    def numberBoxBeforeTyping(self):
        return self.driver.find_element(*RevenueCalculatorPage.number1)

    # Location of sliders input textbox and clearing the field
    def enter_num(self):
        number3 = self.driver.find_element(By.XPATH, "//input[@type='number']")
        actions = ActionChains(self.driver)
        return actions.move_to_element(number3).double_click().click().send_keys(Keys.BACK_SPACE)

    # To select given CPT codes
    def cpt_Codes(self):
        codes = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1p19z09']/div")
        print(len(codes))
        cpt_lists = ["CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"]

        for code in codes:
            code_text = code.text  # Directly get the text content of the element
            for cpt_code in cpt_lists:
                if cpt_code in code_text:
                    code.find_element(By.XPATH, "label/span[1]").click()

    # Reimbursement amount web element location
    def reimbursement_amount(self):
        return self.driver.find_element(*RevenueCalculatorPage.reimbursement)

    # To scroll to bottom of the page
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
