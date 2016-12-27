from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Translator:
    def __init__(self):
        self.driver = webdriver.Firefox()
        url = 'https://translate.google.com/'
        self.driver.get(url)

    def text_translate(self, line):
        clear_area = self.driver.find_element_by_xpath("//textarea[@id='source']")
        clear_area.send_keys(Keys.CONTROL,'a')

        new_state = early_state = self.driver.find_element_by_xpath("//span[@id='result_box']").text
        source = self.driver.find_element_by_xpath("//textarea[@id='source']")
        source.send_keys(line)

        count = 0
        while(early_state == new_state or new_state == (early_state + '...') ):
            new_state = self.driver.find_element_by_xpath("//span[@id='result_box']").text
            count += 1
            if count == 30:
                source = self.driver.find_element_by_xpath("//textarea[@id='source']")
                source.send_keys(line)
                count = 0

        return new_state
