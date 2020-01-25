from django.shortcuts import render
from ecomapp.models import Mycar
from ecomapp.models import Request
from ecomapp.models import Order
from ecomapp.models import User
from ecomapp.models import Customer
from ecomapp.models import Cars
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.urls import reverse
from django.http import JsonResponse
from ecomapp.forms import RegistrationForm
from ecomapp.forms import LoginForm
from ecomapp.forms import CustomerForm
import hashlib
import time
from django.contrib.auth.models import User as MainUser

# Create your views here.

def base_view(request):
	requests = Request.objects.all()
	order_by_cost = request.GET.get('order_by_cost')
	order_by_cost_distinct= request.GET.get('order_by_cost_distinct')
	order_by_year=request.GET.get('order_by_year')
	order_by_year_distinct=request.GET.get('order_by_year_distinct')
	news_order = request.GET.get('news_order')
	print("order_by_cost ",  order_by_cost)
	print("order_by_cost_distinct ",  order_by_cost_distinct)
	print("order_by_year ",  order_by_year)
	print("order_by_year_distinct ",  order_by_year_distinct)
	print("news_order ",  news_order)
	first_cost = request.GET.get('first_cost')
	last_cost = request.GET.get('last_cost')
	first_year = request.GET.get('first_year')
	last_year = request.GET.get('last_year')
	filter_mark = request.GET.get('filter_mark')
	filter_model = request.GET.get('filter_model')
	filter_body = request.GET.get('filter_body')
	filter_color = request.GET.get('filter_color')
	filter_engine = request.GET.get('filter_engine')
	filter_KPP1 = request.GET.get('filter_KPP1')
	filter_KPP2 = request.GET.get('filter_KPP2')
	filter_KPP = ''
	if filter_KPP1 == None and filter_KPP2 == None:
		filter_KPP = ''
	if filter_KPP1 == 'МКПП' and filter_KPP2 == None:
		filter_KPP = 'МКПП'
	if filter_KPP1 == None and filter_KPP2 == 'АКПП':
		filter_KPP = 'АКПП'
	if filter_KPP1 == 'МКПП' and filter_KPP2 == 'АКПП':
		filter_KPP = ''
	filter_unit = request.GET.get('filter_unit')
	first_mileage = request.GET.get('first_mileage')
	last_mileage = request.GET.get('last_mileage')
	filter_supplier = request.GET.get('filter_supplier')
	mycars = Mycar.objects.all(order_by_cost, order_by_cost_distinct, order_by_year, order_by_year_distinct, news_order, first_cost, last_cost, first_year, last_year, filter_mark, filter_model, filter_body, filter_color, filter_engine, filter_KPP, filter_unit, first_mileage, last_mileage, filter_supplier)
	filterset = Mycar.objects.all(None, None, None, None, "WordOrder", first_cost, last_cost, first_year, last_year, filter_mark, filter_model, filter_body, filter_color, filter_engine, filter_KPP, filter_unit, first_mileage, last_mileage, filter_supplier)
	markset = ''
	modelset = ''
	colorset = ''
	engineset = ''
	supplierset = ''
	for mark in filterset:
		markset = markset + mark.car.car.mark + '^'
	markset = markset.rstrip('^')
	massmarks = markset.split('^')
	massmarks = list(set(massmarks))
	massmarks = sorted(massmarks)

	for model in filterset:
		modelset = modelset + model.car.car.model + '^'
	modelset = modelset.rstrip('^')
	massmodels = modelset.split('^')
	massmodels = list(set(massmodels))
	massmodels = sorted(massmodels)

	for color in filterset:
		colorset = colorset + color.color + '^'
	colorset = colorset.rstrip('^')
	masscolors = colorset.split('^')
	masscolors = list(set(masscolors))
	masscolors = sorted(masscolors)

	for engine in filterset:
		engineset = engineset + engine.engine + '^'
	engineset = engineset.rstrip('^')
	massengines = engineset.split('^')
	massengines = list(set(massengines))
	massengines = sorted(massengines)

	for supplier in filterset:
		supplierset = supplierset + supplier.car.shipper.name + '^'
	supplierset = supplierset.rstrip('^')
	masssuppliers = supplierset.split('^')
	masssuppliers = list(set(masssuppliers))
	masssuppliers = sorted(masssuppliers)
	

	context = {
		'mycars': mycars,
		'massmarks': massmarks,
		'massmodels': massmodels,
		'masscolors': masscolors,
		'massengines': massengines,
		'masssuppliers': masssuppliers,
		'requests': requests
	}
	return render(request, 'base.html', context)
"""
	for i in range(1, 100000):
		testcar = Cars.objects.get(mark = ('Mark' + str(i)) )
		testcar.delete()

	for i in range(1, 100000):
		testcar = Cars()
		testcar.mark = 'Mark' + str(i)
		testcar.model = 'Model' + str(i)
		testcar.carcass = 'Body' + str(i)
		testcar.years_of_productions = '1900-2000'
		testcar.engines = 'Engine' + str(i)
		testcar.transmissions = 'Transmission' + str(i)
		testcar.drive_units = str(i)
		testcar.save()
"""

def order_by_view(request):
	requests = Request.objects.all()
	order_by_cost = request.GET.get('order_by_cost')
	order_by_cost_distinct= request.GET.get('order_by_cost_distinct')
	order_by_year=request.GET.get('order_by_year')
	order_by_year_distinct=request.GET.get('order_by_year_distinct')
	news_order = request.GET.get('news_order')
	mycars = Mycar.objects.all(order_by_cost, order_by_cost_distinct, order_by_year, order_by_year_distinct, news_order)
	return JsonResponse({'order_by_cost': order_by_cost, 'order_by_cost_distinct': order_by_cost_distinct, 'order_by_year': order_by_year, 'order_by_cost_distinct': order_by_cost_distinct, 'news_order': news_order})

def filter_view(request):
	requests = Request.objects.all()
	order_by_cost = request.GET.get('order_by_cost')
	order_by_cost_distinct= request.GET.get('order_by_cost_distinct')
	order_by_year=request.GET.get('order_by_year')
	order_by_year_distinct=request.GET.get('order_by_year_distinct')
	news_order = request.GET.get('news_order')
	first_cost = request.GET.get('first_cost')
	last_cost = request.GET.get('last_cost')
	first_year = request.GET.get('first_year')
	last_year = request.GET.get('last_year')
	filter_mark = request.GET.get('filter_mark')
	filter_model = request.GET.get('filter_model')
	filter_body = request.GET.get('filter_body')
	filter_color = request.GET.get('filter_color')
	filter_engine = request.GET.get('filter_engine')
	filter_KPP1 = request.GET.get('filter_KPP1')
	filter_KPP2 = request.GET.get('filter_KPP2')
	filter_KPP = ''
	if filter_KPP1 == None and filter_KPP2 == None:
		filter_KPP = ''
	if filter_KPP1 == 'МКПП' and filter_KPP2 == None:
		filter_KPP = 'МКПП'
	if filter_KPP1 == None and filter_KPP2 == 'АКПП':
		filter_KPP = 'АКПП'
	if filter_KPP1 == 'МКПП' and filter_KPP2 == 'АКПП':
		filter_KPP = ''
	filter_unit = request.GET.get('filter_unit')
	first_mileage = request.GET.get('first_mileage')
	last_mileage = request.GET.get('last_mileage')
	filter_supplier = request.GET.get('filter_supplier')
	mycars = Mycar.objects.all(order_by_cost, order_by_cost_distinct, order_by_year, order_by_year_distinct, news_order, first_cost, last_cost, first_year, last_year, filter_mark, filter_model, filter_body, filter_color, filter_engine, filter_KPP, filter_unit, first_mileage, last_mileage, filter_supplier)
	filterset = Mycar.objects.all(None, None, None, None, "WordOrder", first_cost, last_cost, first_year, last_year, filter_mark, filter_model, filter_body, filter_color, filter_engine, filter_KPP, filter_unit, first_mileage, last_mileage, filter_supplier)
	return JsonResponse({'first_cost': first_cost, 'last_cost': last_cost, 'first_year': first_year, 'last_year': last_year, 'filter_mark': filter_mark, 'filter_model': filter_model, 'filter_body': filter_body, 'filter_color': filter_color, 'filter_engine': filter_engine, 'filter_KPP1': filter_KPP1, 'filter_KPP2': filter_KPP2, 'filter_unit': filter_unit, 'first_mileage': first_mileage, 'last_mileage': last_mileage, 'filter_supplier': filter_supplier })

def mycar_view(request, mycar_slug):
	requests = Request.objects.all()
	mycar = Mycar.objects.get(slug = mycar_slug)
	#bdata = mycar.imageb
	context = {
		'mycar': mycar,
		'requests': requests
	}
	return render(request, 'mycar.html', context)

def request_view(request):
	#requests = Request.objects.all()
	requests = Request.objects.filter(customer = Customer.objects.get(login = User.objects.get(login = request.user.username)))
	"""
	try:
		requests_id = request.session['requests_id']
		requests = Request.objects.get(id =  requests_id)
	except:
		requests = Request()
		#requests.save()
		requests_id= requests.id
		request.session['requests_id']=requests_id
		requests = Request.objects.get(id = requests_id)
		"""
	context = {
	'requests': requests
	}
	return render(request, 'request.html', context)

def add_to_request_view(request, mycar_slug):
	requests = Request.objects.all()
	mycar = Mycar.objects.get(slug = mycar_slug)
	new_item, _ = Request.objects.get_or_create(car = mycar, cost=mycar.cost,  date_request = datetime.today() , customer= Customer.objects.get(login = User.objects.get(login = request.user.username)) , request_status = "на рассмотрении", delivery="Нет") 
	#requests.add(new_item)
	#if new_item not in requests.all():
	if new_item not in requests:
		mycar.visible = 'False'
		mycar.save()
		requests, _ = Request.objects.get_or_create(car = mycar, cost= mycar.cost, date_request = datetime.today() , customer= Customer.objects.get(login = User.objects.get(login = request.user.username)), request_status = "на рассмотрении", delivery="Нет")
	return HttpResponseRedirect('/requests/')

def remove_from_request_view(request, mycar_slug):
	requests = Request.objects.all()
	mycar = Mycar.objects.get(slug = mycar_slug)
	for requests_mass in requests:
		if requests_mass.car == mycar: 
			del_request = Request.objects.get(car = mycar)
			del_request.delete()
			mycar.visible = 'True'
			mycar.save()
			return HttpResponseRedirect('/requests/')


def change_request_delivery(request):
	requests = Request.objects.all()
	delivery = request.GET.get('delivery')
	request_id = request.GET.get('request_id')
	requests = Request.objects.get(id = int(request_id))
	requests.delivery = delivery
	if delivery == 'Да' :
		requests.delivery_address = requests.customer.address
		requests.cost_with_delivery = requests.car.cost * 1.03
		requests.cost = requests.cost_with_delivery
	if delivery == 'Нет' :
		requests.delivery_address = ''
		requests.cost_with_delivery = requests.car.cost
		requests.cost = requests.cost_with_delivery
	requests.save()
	return JsonResponse({'delivery': requests.delivery, 'delivery_address': requests.delivery_address, 'cost_with_delivery': requests.cost_with_delivery})

def order_view(request):
	requests = Request.objects.all()
	#orders = Order.objects.all()
	current_requests = Request.objects.filter(customer = Customer.objects.get(login = User.objects.get(login = request.user.username)))
	orders = Order.objects.none()
	#if current_requests:
		#orders = Order.objects.filter(request = Request.objects.get(customer = Customer.objects.get(login = User.objects.get(login = request.user.username))))
	for r in current_requests:
		if r.request_status == 'принята':
			orders |= Order.objects.filter(request = r)
	context = {
	'requests': requests,
	'orders': orders
	}
	return render(request, 'order.html', context)

def account_view(request):
	form = CustomerForm(request, request.POST or None)
	if form.is_valid():
		login = form.cleaned_data['login']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		fio = form.cleaned_data['fio']
		address = form.cleaned_data['address']
		person = form.cleaned_data['person']
		password = form.cleaned_data['password_new']
		current_customer = Customer.objects.get(login = User.objects.get(login = request.user.username))
		current_user = User.objects.get(login = request.user.username)
		current_main_user = MainUser.objects.get(username = request.user.username)
		if password:
			hashpass = hashlib.sha1(password.encode('utf-8')).hexdigest()
			current_main_user.set_password(password)
			current_user.password = hashpass
		#current_customer.login = login
		request.user.username = login
		current_main_user.username = login
		current_user.login = login
		current_customer.email = email
		current_customer.phone = phone
		current_customer.fio = fio
		current_customer.address = address
		current_customer.person = person
		current_main_user.save()
		current_customer.save()
		current_user.save()
		if password:
			return HttpResponseRedirect(reverse('base'))
	context = {
		'form': form
	}
	return render(request, 'account.html', context)

def registration_view(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		new_user = form.save(commit = False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		email = form.cleaned_data['email']
		phone = form.cleaned_data['phone']
		fio = form.cleaned_data['fio']
		address = form.cleaned_data['address']
		person = form.cleaned_data['person']
		new_user.username = username
		new_user.set_password(password)
		new_user.email = email
		new_user.save()
		hashpass = hashlib.sha1(password.encode('utf-8')).hexdigest()
		#new_user_alternative, _ = User.objects.get_or_create(login = username, password = hashpass, user_type = 'user')
		new_user_alternative = User()
		new_user_alternative.login = username
		new_user_alternative.password = hashpass
		new_user_alternative.user_type = 'user'
		new_user_alternative.save()
		#new_customer, _ = Customer.objects.get_or_create(login = new_user_alternative, fio = fio, phone = phone, address = address, person = person, email = email)
	if form.is_valid():
		new_customer = Customer()
		new_customer.login = User.objects.get(login = username)
		new_customer.fio = fio
		new_customer.phone = phone
		new_customer.address = address
		new_customer.person = person
		new_customer.email = email
		new_customer.save()
		login_user = authenticate(username=username, password = password)
		if login_user:
			login(request, login_user)
			return HttpResponseRedirect(reverse('base'))
	context = {
		'form': form
	}
	return render(request, 'registration.html', context)

def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		login_user = authenticate(username = username, password = password)
		if login_user: 
			login(request, login_user)
			return HttpResponseRedirect(reverse('base'))
	context = {
		'form': form
	}
	return render(request, 'login.html', context)
