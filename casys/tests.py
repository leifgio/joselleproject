from django.test import TestCase
from casys.views import MainPage
from .models import Contact_us 
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	# def test_responding_post_request(self):
	# 	resp = self.client.post('/', data={'name' :'cusName',
	# 		'email': 'cusEmail',
	# 		'review': 'cusReview'})
	# 	self.assertIn('cusName', resp.content.decode())
	# 	self.assertTemplateUsed(resp, 'mainpage.html')
	def test_save_POST_request(self):
		response = self.client.post('/', {'name': 'Joselle',
        	'email': 'joselle@gmail.com', "review": 'Very Good'})
		self.assertEqual(Contact_us.objects.count(), 1)
		newData = Contact_us.objects.first()
		self.assertEqual(newData.FullName, 'Joselle')
		self.assertEqual(newData.ActiveEmail, 'joselle@gmail.com')
		self.assertEqual(newData.Messages, 'Very Good')
	def test_POST_redirect(self):
		response = self.client.post('/', {'name': 'Joselle',
			'email': 'joselle@gmail.com', "review": 'Very Good'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response["location"], '/')
	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Contact_us.objects.count(), 0)


class ORMTEST(TestCase):
	def test_saving_retriv(self):
		Client1 = Contact_us()
		Client1.FullName = 'Joselle'
		Client1.ActiveEmail='joselle@gmail.com'
		Client1.Messages='Very Good'
		Client1.save()

		Client_2 = Contact_us()
		Client_2.FullName= 'Sharm'
		Client_2.ActiveEmail= 'sharm@gmail.com'
		Client_2.Messages='Excelent'
		Client_2.save()

		Client = Contact_us.objects.all()
		self.assertEqual(Client.count(), 2)

		C1 = Client[0]
		C2 = Client[1]

		self.assertEqual(C1.FullName, 'Joselle')
		self.assertEqual(C1.ActiveEmail, 'joselle@gmail.com')
		self.assertEqual(C1.Messages, 'Very Good')
		self.assertEqual(C2.FullName, 'Sharm')
		self.assertEqual(C2.ActiveEmail, 'sharm@gmail.com')
		self.assertEqual(C2.Messages, 'Excelent')

	def test_template_display_list(self):
		Contact_us.objects.create(FullName="Sandra", ActiveEmail='sandra@gmail', Messages='Nice')
		Contact_us.objects.create(FullName="Kenny", ActiveEmail='kenny@gmail', Messages='Aesthetics')
		resp = self.client.get('/')
		self.assertIn('Summary: Sandra, sandra@gmail, Nice', resp.content.decode())
		self.assertIn('Summary: Kenny, kenny@gmail, Aesthetics', resp.content.decode())