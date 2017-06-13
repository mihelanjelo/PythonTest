import time

import pytest

from pageobjects.cryptocomparepage import CryptoComparePage
from utils.base import Base


# Test of correct proportionality
class TestProp(Base):
    page = CryptoComparePage(Base.driver)

    def setup_class(self):
        self.visit(self, url="https://www.cryptocompare.com/mining/calculator/btc")

    @pytest.mark.parametrize("hp, pc, c1, c2,  m", [
        (10000, 5, 20, 50, "GH/s"),
    ])
    def test_cost_increase(self, hp, pc, c1, c2,  m):
        self.page.input_hashing_power(input_number=hp, measure=m)
        self.page.input_power_consumption(input_number=pc)
        self.page.input_cost(input_number=c1)
        time.sleep(1)
        profit1 = self.page.get_profit_value()
        self.page.input_cost(input_number=c2)
        time.sleep(1)
        profit2 = self.page.get_profit_value()
        assert profit1 > profit2

    @pytest.mark.parametrize("hp1, pc, c, hp2,  m", [
    (10000, 5, 20, 100000, "GH/s"),
    ])
    def test_hashing_power_increase(self, hp1, pc, c, hp2, m):
        self.page.input_hashing_power(input_number=hp1, measure=m)
        self.page.input_power_consumption(input_number=pc)
        self.page.input_cost(input_number=c)
        time.sleep(1)
        profit1 = self.page.get_profit_value()
        self.page.input_hashing_power(input_number=hp2, measure=m)
        time.sleep(1)
        profit2 = self.page.get_profit_value()
        assert profit1 < profit2

    @pytest.mark.parametrize("hp, pc1, c, pc2,  m", [
        (10000, 5, 20, 7, "GH/s"),
    ])
    def test_power_consumption_increase(self, hp, pc1, c, pc2, m):
        self.page.input_hashing_power(input_number=hp, measure=m)
        self.page.input_power_consumption(input_number=pc1)
        self.page.input_cost(input_number=c)
        time.sleep(1)
        profit1 = self.page.get_profit_value()
        self.page.input_power_consumption(input_number=pc2)
        time.sleep(1)
        profit2 = self.page.get_profit_value()
        assert profit1 > profit2

    def teardown_class(self):
        self.close(self)