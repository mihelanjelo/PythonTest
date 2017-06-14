import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class CryptoComparePage:

    def __init__(self, driver):
        self.driver = driver

    def input_hashing_power(self, input_number, measure):
        locator = (By.XPATH, "//input[@name='HashingPower']")
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        self.wait_to_be_clickable(locator)
        element.clear()
        if measure in ["H/s", "KH/s", "MH/s", "GH/s", "TH/s"]:
            measure_select = Select(WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//select[@name='currentHashingUnit']"))))
            measure_select.select_by_value(measure)
        else:
            raise Exception('Wrong measure!')
        element.click()
        element.send_keys(input_number)

    def input_power_consumption(self, input_number):
        locator = (By.XPATH, "//input[@name='PowerConsumption']")
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        self.wait_to_be_clickable(locator)
        element.clear()
        element.click()
        element.send_keys(input_number)

    def input_cost(self, input_number):
        locator = (By.XPATH, "//input[@name='CostPerkWh']")
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
        self.wait_to_be_clickable(locator)
        element.clear()
        element.click()
        element.send_keys(input_number)

    def get_profit_value(self):
        locator = (By.XPATH, "//div[@class='circle-content ng-binding']")
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(locator))
        value = float(element.text.replace("$", "").replace(",", ""))
        return value

    def get_bitcoin_price(self):
        locator = (By.XPATH, "//div[@class='contract-disclosure ng-binding']/b[2]")
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
        value = float(element.text.replace("1 BTC = $", ""))
        return value

    def get_hashrate(self):
        locator = (By.XPATH, "//div[@class='contract-disclosure ng-binding']/b[1]")
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator))
        print(element.text.replace(",", "").replace("GH/s", ""))
        value = float(element.text.replace(",", "").replace("GH/s", ""))
        return value

    def wait_to_be_clickable(self, locator):
        for i in range(1, 4):
            if not WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable(locator)):
                time.sleep(0.5)
                if i == 4:
                    raise Exception("Element isn't clickable for 5+ seconds!")
            else:
                break
