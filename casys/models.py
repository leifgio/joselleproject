from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Client(models.Model):
	firstname= models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	address = models.TextField()
	contact_number = PhoneNumberField(null=False,blank=False,unique=True)
    
	def __str__(self):
         return '%s-%s' % (self.surname, self.firstname)

class Product(models.Model):
	product_name = models.CharField(max_length=24, unique=True)
	art_medium = models.CharField(max_length=300)
	size = models.CharField(max_length=200)
	price = models.CharField(max_length=24)
	quantity=models.IntegerField()

	def __str__(self):
		 return self.product_name

class Order(models.Model):
    COURIER = (('jt', 'J&T Express'), ('lm', 'lala move'), ('lbc', 'LBC Hari ng Padala'))
    user_information = models.ForeignKey(Client, on_delete = models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete = models.CASCADE)
    reference_picture = models.ImageField(null=True, blank=True, upload_to="images/")
    courier = models.CharField(max_length=300, choices=COURIER)
    gcash_number = PhoneNumberField(null=False,blank=False)
    gcash_name = models.CharField(max_length=300)
    proof_of_payment = models.CharField(max_length=300)

    def __str__(self):
        return '%s-%s' % (self.pk, self.user_information)

class Shipment(models.Model):
	order_name = models.ForeignKey(Order, on_delete = models.CASCADE)
	date_to_ship = models.DateField()
	time_to_ship = models.TimeField(auto_now = False, auto_now_add = False)

	def __str__(self):
		return '%s-%s' % (self.order_name, self.pk)

class Product_Receive(models.Model):
	recipient_name =  models.ForeignKey(Client, on_delete = models.CASCADE)
	order_name = models.ForeignKey(Order, on_delete = models.CASCADE)
	proof_received = models.ImageField(null=True, blank=True, upload_to="images/")
	feedback = models.TextField()

	def __str__(self):
		return self.recipient_name
