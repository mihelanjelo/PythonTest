import time

import pytest

from pageobjects.cryptocomparepage import CryptoComparePage
from utils.base import Base


# Positive test for checking calculator's behavior with different measures of hashing power field
class TestCalc(Base):
    page = CryptoComparePage(Base.driver)

    def setup_class(self):
        self.visit(self, url="https://www.cryptocompare.com/mining/calculator/btc")

    @pytest.mark.parametrize("value1, value2, value3, measure", [
        (122, 122, 10, "H/s"),
        (122, 122, 10, "KH/s"),
        (122, 122, 10, "MH/s"),
        (122, 122, 10, "GH/s"),
        (122, 122, 10, "TH/s"),
    ])
    def test_scenario(self, value1, value2, value3, measure):
        self.page.input_hashing_power(input_number=value1, measure=measure)
        self.page.input_power_consumption(input_number=value2)
        self.page.input_cost(input_number=value3)
        time.sleep(2)
        profit = self.page.get_profit_value()
        print("Profit per month = ", profit)
        if measure == "TH/s":
            assert profit > 0
        else:
            assert profit < 0

    def teardown_class(self):
        self.close(self)


if __name__ == '__main__':
    pytest.main('test_calc.py')
