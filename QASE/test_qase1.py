import pytest
from selenium import webdriver

def test_title():
    driver = webdriver.Firefox()
    driver.get('https://qase.io/')
    assert driver.title == 'Qase | Test management software for QA teams'
    driver.quit()