import time

import pytest

from pageobjects.cryptocomparepage import CryptoComparePage
from utils.base import Base


# Test of correct profit calculation result
class TestFormula(Base):
    page = CryptoComparePage(Base.driver)

    def setup_class(self):
        self.visit(self, "https://www.cryptocompare.com/mining/calculator/btc")

    @pytest.mark.parametrize("hp, pc, c, m", [
        (10000, 5, 50, "GH/s"),
    ])
    def test_calc_result(self, hp, pc, c, m):
        time_in_sec = 2592000
        block_in_money = 12.5 * self.page.get_bitcoin_price()
        hashrate = self.page.get_hashrate()
        hash_power = hp
        kwatts = pc/1000
        time_in_hours = 24 * 30
        cost_per_hour = c

        self.page.input_hashing_power(input_number=hp, measure=m)
        self.page.input_power_consumption(input_number=pc)
        self.page.input_cost(input_number=c)
        time.sleep(1)
        profit = (time_in_sec * block_in_money * hash_power)/(hashrate * 600) - kwatts * time_in_hours * cost_per_hour
        print(round(profit, 2))
        print(self.page.get_profit_value())
        assert round(profit, 2) == self.page.get_profit_value()

    def teardown_class(self):
        self.close(self)
