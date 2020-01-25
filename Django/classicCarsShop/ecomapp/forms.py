from django import forms
from ecomapp.models import Customer
from django.contrib.auth.models import User
from ecomapp.models import User as MyUser

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label='Логин'
		self.fields['password'].label = 'Пароль'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		if not User.objects.filter(username = username).exists():
			raise forms.ValidationError('Пользователя с таким логином не существует!')
		user = User.objects.get(username = username)
		#if user and  user.password != password:
		if user and not user.check_password(password):
			raise forms.ValidationError('Неверный пароль!')


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	password_check = forms.CharField(widget = forms.PasswordInput)
	fio = forms.CharField(max_length = 200)
	address = forms.CharField(max_length = 200)
	phone = forms.CharField(max_length = 20)
	person  = forms.ChoiceField(choices = (('физическое лицо', 'физическое лицо'),('частный предприниматель','частный предприниматель')))
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email'
		]

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label='Логин'
		self.fields['password'].label = 'Пароль'
		self.fields['password'].help_text = 'Придумайте пароль'
		self.fields['password_check'].label = 'Повторите пароль'
		self.fields['fio'].label = 'ФИО'
		self.fields['email'].label = 'Электронная почта'
		self.fields['address'].label = 'Адрес'
		self.fields['phone'].label = 'Номер телефона'
		self.fields['person'].label = 'Лицо'
		'''
		self.fields['phone'].label = 'Номер телефона'
		self.fields['address'].label = 'Адрес'
		self.fields['person'].label = 'Лицо'
		'''
	def clean(self):
		password = self.cleaned_data['password']
		username = self.cleaned_data['username']
		password_check = self.cleaned_data['password_check']
		if password != password_check:
			raise forms.ValidationError('Пароли не совпадают! Попробуйте снова.')
		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('Пользователь с таким логином существует!')
	
class CustomerForm(forms.ModelForm):
	login = forms.CharField()
	fio = forms.CharField(max_length = 200)
	address = forms.CharField(max_length = 200)
	phone = forms.CharField(max_length = 20)
	person  = forms.ChoiceField(choices = (('физическое лицо', 'физическое лицо'),('частный предприниматель','частный предприниматель')))
	password_new = forms.CharField(widget = forms.PasswordInput, required = False)
	password_check = forms.CharField(widget = forms.PasswordInput, required = False)
	class Meta:
		model = Customer
		fields = [
			#'login',
			'fio',
			'email',
			'address',
			'phone',
			'person'
		]


	def __init__(self, request,*args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		current_username = User.objects.get(username = request.user.username)
		current_customer = Customer.objects.get(login = MyUser.objects.get(login = current_username.username))
		self.fields['login'].label='Логин'
		self.fields['login'].initial = current_username.username
		#self.fields['password'].label = 'Пароль'
		self.fields['fio'].label = 'ФИО'
		self.fields['fio'].initial = current_customer.fio
		self.fields['email'].label = 'Электронная почта'
		self.fields['email'].initial = current_customer.email
		self.fields['address'].label = 'Адрес'
		self.fields['address'].initial = current_customer.address
		self.fields['phone'].label = 'Номер телефона'
		self.fields['phone'].initial = current_customer.phone
		self.fields['person'].label = 'Лицо'
		self.fields['person'].initial = current_customer.person
		self.fields['password_new'].label = 'Новый пароль'
		self.fields['password_check'].label = 'Повторите пароль'

	def clean(self):
		password_new = self.cleaned_data['password_new']
		password_check = self.cleaned_data['password_check']
		login = self.cleaned_data['login']
		if password_new != password_check:
			raise forms.ValidationError('Пароли не совпадают! Попробуйте снова.')
		#if User.objects.filter(username = login).exists() and request.user.username != login:
			#raise forms.ValidationError('Пользователь с таким логином существует!')

