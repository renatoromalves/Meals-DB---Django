from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.common.exceptions import SessionNotCreatedException as SNCE
from selenium.common.exceptions import TimeoutException as TimeExpt

class teste:
    def __init__(self):    
        self.driver = webdriver.Chrome()
        self.driver.get('https://topiproject-renato.herokuapp.com/')

    def test_search(self, keyword):
        self.driver.find_element_by_name('searchfield').send_keys(keyword)
        self.driver.find_element_by_name('searchfield').submit()
        test = []
        elements = self.driver.find_elements_by_id('name')
        for item in elements:
            if keyword.lower() in item.text.lower():
                test.append(item)
        if len(test) == len(elements):
            print('test passed')
            return True
        else:
            print('something went wrong')
            return False
        
    def test_next_pagination(self):
        test = True
        while test:
            try:
                self.driver.find_element_by_link_text('next').click()
                wait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"name")))
            except NSEE:
                test = False
                print('Click Next test passed')
            except TimeExpt:
                print('Something went wrong')
                return False
        return True
    def test_previous_pagination(self):
        test = True
        while test:
            try:
                self.driver.find_element_by_link_text('previous').click()
                wait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"name")))
            except NSEE:
                test = False
                print('Click Previous test passed')
            except TimeExpt:
                print('Something went wrong')
                return False
        return True
    
def do_all_tests():
    testing = teste()
    results = []
    results.append(testing.test_next_pagination())
    results.append(testing.test_previous_pagination())
    results.append(testing.test_search('chicken'))
    results.append(testing.test_next_pagination())
    results.append(testing.test_previous_pagination())
    if False in results:
        print('Some tests failed')
    else:
        print('All tests passed')
    
