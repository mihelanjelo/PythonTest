import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class CryptoComparePage:

    def __init__(self, driver):
        self.driver = driver

    locators = {"hashing_power" : (By.XPATH, "//input[@name='HashingPower']"),
                "power_consumption" : (By.XPATH, "//input[@name='PowerConsumption']"),
                "cost" : (By.XPATH, "//input[@name='CostPerkWh']"),
                "profit_per_month" : (By.XPATH, "//div[@class='circle-content ng-binding']"),
                "bitcoin_price" : (By.XPATH, "//div[@class='contract-disclosure ng-binding']/b[2]"),
                "hashrate" : (By.XPATH, "//div[@class='contract-disclosure ng-binding']/b[1]"),
                "change_measure" : (By.XPATH, "//select[@name='currentHashingUnit']")
                }


    def input_hashing_power(self, input_number, measure):
        element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.get("hashing_power")))
        element.clear()
        if measure in ["H/s", "KH/s", "MH/s", "GH/s", "TH/s"]:
            measure_select = Select(WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(self.locators.get("change_measure"))))
            measure_select.select_by_value(measure)
        else:
            raise Exception('Wrong measure!')
        element.click()
        element.send_keys(input_number)

    def input_power_consumption(self, input_number):
        element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.get("power_consumption")))
        element.clear()
        element.click()
        element.send_keys(input_number)

    def input_cost(self, input_number):
        element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.locators.get("cost")))
        element.clear()
        element.click()
        element.send_keys(input_number)

    def get_profit_per_month_value(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.locators.get("profit_per_month")))
        value = float(element.text.replace("$", "").replace(",", ""))
        return value

    def get_bitcoin_price(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.locators.get("bitcoin_price")))
        value = float(element.text.replace("1 BTC = $", ""))
        return value

    def get_hashrate(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.locators.get("hashrate")))
        value = float(element.text.replace(",", "").replace("GH/s", ""))
        return value

