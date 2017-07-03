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
        (20000, 4, 58, "GH/s")
    ])
    def test_calc_result(self, hp, pc, c, m):
        time_in_sec = 24 * 60 * 60 * 30
        block_in_money = 12.5 * self.page.get_bitcoin_price(3)
        hashrate = self.page.get_hashrate(3)
        hash_power = hp
        kwatts = pc/1000
        time_in_hours = 24 * 30
        block_time = 600
        cost_per_hour = c

        self.page.input_hashing_power(input_number=hp, measure=m, time_wait_element=3)
        self.page.input_power_consumption(input_number=pc, time_wait_element=3)
        self.page.input_cost(input_number=c, time_wait_element=3)
        time.sleep(1)
        profit_per_month = (time_in_sec * block_in_money * hash_power)/(hashrate * block_time) - kwatts * time_in_hours * cost_per_hour
        print(round(profit_per_month, 2))
        print(self.page.get_profit_per_month_value(3))
        assert round(profit_per_month, 2) == self.page.get_profit_per_month_value(3)

    def teardown_class(self):
        self.close(self)
