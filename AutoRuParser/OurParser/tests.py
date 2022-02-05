from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.utils import timezone
from datetime import datetime
from django.http import *
from .models import *
from .views import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse, resolve

class Request():
    def __init__(self, city, pagenumber, yearfrom, yearto, powerfrom, powerto, kmagefrom, kmageto, accelerationfrom, accelerationto, displacementfrom, displacementto, 
	                 pricefrom, priceto, fuelrateto, clearancefrom):
        self.city = city
        self.pagenumber = pagenumber
        self.yearfrom = yearfrom
        self.yearto = yearto
        self.powerfrom = powerfrom
        self.powerto = powerto
        self.kmagefrom = kmagefrom
        self.kmageto = kmageto
        self.accelerationfrom = accelerationfrom
        self.accelerationto = accelerationto
        self.displacementfrom = displacementfrom
        self.displacementto = displacementto
        self.pricefrom = pricefrom
        self.priceto = priceto
        self.fuelrateto = fuelrateto
        self.clearancefrom = clearancefrom

class TestUrls(SimpleTestCase):

    def test_registration(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, registration)
		
    def test_login_user(self):
        url = reverse('login_user')
        self.assertEquals(resolve(url).func, login_user)

    def test_autoruparser(self):
        url = reverse('autoruparser')
        self.assertEquals(resolve(url).func, autoruparser)
		
    def test_registration2(self):
        url = reverse('create_user')
        self.assertEquals(resolve(url).func, registration)
		
    def test_login_user2(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)

    def test_autoruparser2(self):
        url = reverse('AutoRuParser')
        self.assertEquals(resolve(url).func, autoruparser)
		
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
		
    def test_registration_GET(self):
        response=self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
		
    def test_login_user_GET(self):
        response=self.client.get(reverse('login_user'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
		
    def test_autoruparser_GET(self):
        response=self.client.get(reverse('autoruparser'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'autoruparser.html')
		
    def test_registration_GET2(self):
        response=self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_user.html')
		
    def test_login_user_GET2(self):
        response=self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
		
    def test_autoruparser_GET2(self):
        response=self.client.get(reverse('autoruparser'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'AutoRuParser.html')
		
class TestUserCreate(TestCase):

    def setUp(self):
        self.user=UserU.objects.create(username='dig', email='dig@yandex.ru', password='fffff', Surname='Digov', Name='Serega', Fathername='Digovich')
        self.user2=UserU.objects.create(username='', email='', password='', Surname='', Name='', Fathername='')
        self.user3=UserU.objects.create(username='digov', email='digyandex.ru', password='fffff', Surname='Digov', Name='Serega', Fathername='Digovich')
		
    def test_create_user_notemptyusername(self):	
        self.assertNotEquals(self.user.username, '')
		
    def test_create_user_notemptyemail(self):	
        self.assertNotEquals(self.user.email, '')
		
    def test_create_user_notemptypassword(self):	
        self.assertNotEquals(self.user.password, '')
		
    def test_create_user_notemptysurname(self):	
        self.assertNotEquals(self.user.Surname, '')
		
    def test_create_user_notemptyname(self):	
        self.assertNotEquals(self.user.Name, '')
		
    def test_create_user_notemptyfathername(self):	
        self.assertNotEquals(self.user.Fathername, '')
	
    def test_create_user_correctformatemail(self):	
        self.assertNotEquals(0 if not "@" in self.user.email or not "." in self.user.email or self.user.email.find("@") > self.user.email.rfind(".") else 1, 0)
		
    def test_create_user2_notemptyusername(self):	
        self.assertNotEquals(self.user2.username, '')
		
    def test_create_user2_notemptyemail(self):	
        self.assertNotEquals(self.user2.email, '')
		
    def test_create_user2_notemptypassword(self):	
        self.assertNotEquals(self.user2.password, '')
		
    def test_create_user2_notemptysurname(self):	
        self.assertNotEquals(self.user2.Surname, '')
		
    def test_create_user2_notemptyname(self):	
        self.assertNotEquals(self.user2.Name, '')
		
    def test_create_user3_correctformatemail(self):	
        self.assertNotEquals(0 if not "@" in self.user3.email or not "." in self.user3.email or self.user3.email.find("@") > self.user3.email.rfind(".") else 1, 0)
				
class TestUserLogin(TestCase):

    def setUp(self):
        self.user=UserU.objects.create(username='dig', email='dig@yandex.ru', password='fffff', Surname='Digov', Name='Serega', Fathername='Digovich')
        self.user2=UserU.objects.create(username='', email='', password='', Surname='Digov', Name='Serega', Fathername='Digovich')
		
    def test_create_user_notemptyusername2(self):	
        self.assertNotEquals(self.user.username, '')
		
    def test_create_user_notemptyemail2(self):	
        self.assertNotEquals(self.user.email, '')		
		
    def test_create_user_notemptypassword2(self):	
        self.assertNotEquals(self.user.password, '')
		
    def test_create_user2_notemptyusername2(self):	
        self.assertNotEquals(self.user2.username, '')
		
    def test_create_user2_notemptyemail2(self):	
        self.assertNotEquals(self.user2.email, '')		
		
    def test_create_user2_notemptypassword2(self):	
        self.assertNotEquals(self.user2.password, '')
		
class TestCreateRequest(TestCase):
  
    def setUp(self):
        self.request = Request('fff', 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.request2 = Request('', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.request3 = Request('', '', 'f', 'g', 'a', '3f', 'brfb', 'fef', 'fwef', 'fef', 'efegeg', 'egeg', '/egeg', 'brherh', 'egeheh', 'wwfgeh')
		
    def test_create_request_notemptycity(self):	
        self.assertNotEquals(self.request.city, '')
	
    def test_create_request_notemptypagenumber(self):	
        self.assertNotEquals(str(self.request.pagenumber), '')
		
    def test_create_request_notzeropagenumber(self):	
        self.assertNotEquals(self.request.pagenumber, 0)
		
    def test_create_request_isdigitpagenumber(self):	
        self.assertNotEquals(str(self.request.pagenumber).isdigit(), 0)
		
    def test_create_request_isdigityearfrom(self):	
        self.assertNotEquals(str(self.request.yearfrom).isdigit(), 0)
		
    def test_create_request_isdigityearto(self):	
        self.assertNotEquals(str(self.request.yearto).isdigit(), 0)
		
    def test_create_request_isdigitpowerfrom(self):	
        self.assertNotEquals(str(self.request.powerfrom).isdigit(), 0)
		
    def test_create_request_isdigitpowerto(self):	
        self.assertNotEquals(str(self.request.powerto).isdigit(), 0)
		
    def test_create_request_isdigitkmagefrom(self):	
        self.assertNotEquals(str(self.request.kmagefrom).isdigit(), 0)
		
    def test_create_request_isdigitkmageto(self):	
        self.assertNotEquals(str(self.request.kmageto).isdigit(), 0)
		
    def test_create_request_isdigitaccelerationfrom(self):	
        self.assertNotEquals(str(self.request.accelerationfrom).isdigit(), 0)
		
    def test_create_request_isdigitaccelerationto(self):	
        self.assertNotEquals(str(self.request.accelerationto).isdigit(), 0)
		
    def test_create_request_isdigitdisplacementfrom(self):	
        self.assertNotEquals(str(self.request.displacementfrom).isdigit(), 0)
		
    def test_create_request_isdigitdisplacementto(self):	
        self.assertNotEquals(str(self.request.displacementto).isdigit(), 0)
		
    def test_create_request_isdigitpricefrom(self):	
        self.assertNotEquals(str(self.request.pricefrom).isdigit(), 0)
		
    def test_create_request_isdigitpriceto(self):	
        self.assertNotEquals(str(self.request.priceto).isdigit(), 0)
		
    def test_create_request_isdigitfuelrateto(self):	
        self.assertNotEquals(str(self.request.fuelrateto).isdigit(), 0)
		
    def test_create_request_isdigitclearancefrom(self):	
        self.assertNotEquals(str(self.request.clearancefrom).isdigit(), 0)
		
    def test_create_request2_notemptycity(self):	
        self.assertNotEquals(self.request2.city, '')
	
    def test_create_request2_notemptypagenumber(self):	
        self.assertNotEquals(str(self.request2.pagenumber), '')
		
    def test_create_request3_notzeropagenumber(self):	
        self.assertNotEquals(self.request3.pagenumber, 0)
		
    def test_create_request3_isdigitpagenumber(self):	
        self.assertNotEquals(str(self.request3.pagenumber).isdigit(), 0)
		
    def test_create_request_isdigityearfrom(self):	
        self.assertNotEquals(str(self.request3.yearfrom).isdigit(), 0)
		
    def test_create_request_isdigityearto(self):	
        self.assertNotEquals(str(self.request3.yearto).isdigit(), 0)
		
    def test_create_request3_isdigitpowerfrom(self):	
        self.assertNotEquals(str(self.request3.powerfrom).isdigit(), 0)
		
    def test_create_request3_isdigitpowerto(self):	
        self.assertNotEquals(str(self.request3.powerto).isdigit(), 0)
		
    def test_create_request3_isdigitkmagefrom(self):	
        self.assertNotEquals(str(self.request3.kmagefrom).isdigit(), 0)
		
    def test_create_request3_isdigitkmageto(self):	
        self.assertNotEquals(str(self.request3.kmageto).isdigit(), 0)
		
    def test_create_request3_isdigitaccelerationfrom(self):	
        self.assertNotEquals(str(self.request3.accelerationfrom).isdigit(), 0)
		
    def test_create_request3_isdigitaccelerationto(self):	
        self.assertNotEquals(str(self.request3.accelerationto).isdigit(), 0)
		
    def test_create_request3_isdigitdisplacementfrom(self):	
        self.assertNotEquals(str(self.request3.displacementfrom).isdigit(), 0)
		
    def test_create_request3_isdigitdisplacementto(self):	
        self.assertNotEquals(str(self.request3.displacementto).isdigit(), 0)
		
    def test_create_request3_isdigitpricefrom(self):	
        self.assertNotEquals(str(self.request3.pricefrom).isdigit(), 0)
		
    def test_create_request3_isdigitpriceto(self):	
        self.assertNotEquals(str(self.request3.priceto).isdigit(), 0)
		
    def test_create_request3_isdigitfuelrateto(self):	
        self.assertNotEquals(str(self.request3.fuelrateto).isdigit(), 0)
		
    def test_create_request3_isdigitclearancefrom(self):	
        self.assertNotEquals(str(self.request3.clearancefrom).isdigit(), 0)
		
		

# Create your tests here.
