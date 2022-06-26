from selenium import webdriver
import unittest

from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	#def tearDown(self):
		#self.browser.quit()
	
	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Cent Art', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		CustomerFullName = self.browser.find_element_by_id('customerName')
		self.assertEqual(CustomerFullName.get_attribute('placeholder'),'Please enter your name here.')
		CustomerFullName.send_keys('Joselle Sacriz')
		time.sleep(1)

		CustomerEmail = self.browser.find_element_by_id('customerEmail')
		self.assertEqual(CustomerEmail.get_attribute('placeholder'),'PLease enter your active e-mail here.')
		CustomerEmail.send_keys('josellesacriz@gmail.com') 
		time.sleep(1)


		CustomerReview = self.browser.find_element_by_id('customerReview')
		self.assertEqual(CustomerReview.get_attribute('placeholder'),'PLease enter your message here.')
		CustomerReview.send_keys('Good artworks')
		time.sleep(1)
      		
		btnOK = self.browser.find_element_by_id('btnOK')
		btnOK.click()
		time.sleep(0.5)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_element_by_tag_name('td')
		self.assertIn('Joselle Sacriz, josellesacriz@gmail.com, Good artworks', row_data.text)


	def test_start_list_and_retrieve_2(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Cent Art', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		CustomerFullName = self.browser.find_element_by_id('customerName')
		self.assertEqual(CustomerFullName.get_attribute('placeholder'),'Please enter your name here.')
		CustomerFullName.send_keys('Joselle Sacriz')
		time.sleep(1)

		CustomerEmail = self.browser.find_element_by_id('customerEmail')
		self.assertEqual(CustomerEmail.get_attribute('placeholder'),'PLease enter your active e-mail here.')
		CustomerEmail.send_keys('josellesacriz@gmail.com') 
		time.sleep(1)


		CustomerReview = self.browser.find_element_by_id('customerReview')
		self.assertEqual(CustomerReview.get_attribute('placeholder'),'PLease enter your message here.')
		CustomerReview.send_keys('Good artworks')
		time.sleep(1)
      		
		btnOK = self.browser.find_element_by_id('btnOK')
		btnOK.click()
		time.sleep(0.5)
		

		self.browser.get(self.live_server_url)
		self.assertIn('Cent Art', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		CustomerFullName = self.browser.find_element_by_id('customerName')
		self.assertEqual(CustomerFullName.get_attribute('placeholder'),'Please enter your name here.')
		CustomerFullName.send_keys('Kenny jean')
		time.sleep(1)

		CustomerEmail = self.browser.find_element_by_id('customerEmail')
		self.assertEqual(CustomerEmail.get_attribute('placeholder'),'PLease enter your active e-mail here.')
		CustomerEmail.send_keys('kenny@gmail.com') 
		time.sleep(1)


		CustomerReview = self.browser.find_element_by_id('customerReview')
		self.assertEqual(CustomerReview.get_attribute('placeholder'),'PLease enter your message here.')
		CustomerReview.send_keys('Nice Work')
		time.sleep(1)
      		
		btnOK = self.browser.find_element_by_id('btnOK')
		btnOK.click()
		time.sleep(0.5)


		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('Summary: Joselle Sacriz, josellesacriz@gmail.com, Good artworks', [row.text for row in row_data])
		self.assertIn('Summary: Kenny jean, kenny@gmail.com, Nice Work', [row.text for row in row_data])
# if __name__ == '__main__' :
# 	unittest.main(warnings='ignore')