from lecture2.pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class ContactUsLocators:
	LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]')
	LOCATOR_CONTACT_NAME =(By.XPATH, '//*[@id="contact"]/div[1]/label/input')
	LOCATOR_CONTACT_EMAIL = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
	LOCATOR_CONTACT_CONTENT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
	LOCATOR_CONTACT_SEND_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button')

	
	
class OperationContactUs(BasePage):
	def contact_click(self):
		logging.info('search and click button "Contact"')
		return self.find_element(ContactUsLocators.LOCATOR_CONTACT_BTN).click()
	
	def fill_content_contact(self, name=None, email=None, content=None):
		name_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_NAME)
		name_field.clear()
		if name:
			logging.info('add name')
			name_field.send_keys(name)
		email_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_EMAIL)
		email_field.clear()
		if email:
			logging.info('add email')
			email_field.send_keys(email)
		content_field = self.find_element(ContactUsLocators.LOCATOR_CONTACT_CONTENT)
		content_field.clear()
		if content:
			logging.info('add content')
			content_field.send_keys(content)
		
	def send_contact_info(self):
		logging.info('Send info to contact us')
		return self.find_element(ContactUsLocators.LOCATOR_CONTACT_SEND_BTN).click()
	