from selenium import webdriver


class Base(object):
    driver = webdriver.Chrome()

    def visit(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()