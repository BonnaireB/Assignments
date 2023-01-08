from selenium import webdriver
# -*- coding: UTF-8 -*-
from selenium.common import exceptions as exceptions





class DriverFactory():
    """
    This driver factory class contains the used selenium methods for the purpose of this exercise

    """
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        
    
    def get_all_elements_by_xpath(self,xpath):
        """
        Function to retreive all the elements corresponding to an xpath

        Args:
            xpath (String): HTML relative or Absolute path to all the requested elements

        Returns:
            List <WebElements>: The list of all webElements found
        """
        elements = self.driver.find_elements("xpath",xpath)
        return elements

    def open_url(self,url):
        """
        Function to go to specified URL

        Args:
            url (String): Destination URL
        """
        self.driver.get(url)

    def close(self):
        """
        Function to close Browser

        """
        self.driver.close()