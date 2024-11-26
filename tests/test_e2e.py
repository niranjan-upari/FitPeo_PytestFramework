import time

from pageobjects.RevenueCalculatorPage import RevenueCalculatorPage
from utilities.Baseclass import BaseClass
from pageobjects.HomePage import HomePage

# @pytest.mark.usefixtures("setup")
class TestFitPeo(BaseClass):

    def test_e2e(self):

        # Page Objects of HomePage
        # Step1 & 2(FitPeo Homepage & navigate to Revenue Calculator)
        homePage = HomePage(self.driver)
        homePage.revenueCalculator().click()

        # Page Objects of Revenue Calculator Page
        # Step 3(ScrollDown to the slider section)
        revenueCalculatorPage = RevenueCalculatorPage(self.driver)
        revenueCalculatorPage.MedicalEligiblePatients()

        # Step 4(Adjust Slider)
        revenueCalculatorPage.adjustSlider().perform()
        # revenueCalculatorPage.numberBoxBeforeTyping().click()
        number_before = revenueCalculatorPage.numberBoxBeforeTyping().get_attribute("value")
        assert number_before == "823"

        # Step 5 & 6(Update text field with 560 & validate)
        revenueCalculatorPage.enter_num().perform()
        revenueCalculatorPage.enter_num().send_keys("560").perform()

        # Step 7(Select given CPT codes)
        revenueCalculatorPage.cpt_Codes()

        # Step 8 & 9(Validation of Total Recurring Reimbursement for all Patients Per Month)
        # Here the Amount will be $75600, When we update slider value to 560.
        # But in the Assignment document it's given as $110700, which is correct when the slider value is 820.
        # Therefore, the code is written for both conditions.
        # Condition 1: slider=560
        value_560 = revenueCalculatorPage.reimbursement_amount().text
        print("Total Recurring Reimbursement for all Patients Per Month, when Slider=560", value_560)
        assert "$75600" == value_560   # Verification

        # Step 5 & 6(Update text field with 820 & validate)
        # Condition 2: slider=820
        revenueCalculatorPage.enter_num().perform()
        revenueCalculatorPage.enter_num().send_keys("820").perform()
        revenueCalculatorPage.scroll_to_bottom()

        # Step 8 & 9(Validation of Total Recurring Reimbursement for all Patients Per Month)
        value_820 = revenueCalculatorPage.reimbursement_amount().text
        print("Total Recurring Reimbursement for all Patients Per Month, when Slider=820", value_820)
        assert "$110700" == value_820  # Verification
        time.sleep(3)
