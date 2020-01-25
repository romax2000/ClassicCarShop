from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import pre_delete
from django.db.models.signals import post_save
from datetime import datetime
from django.urls import reverse
from transliterate import translit
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models import F

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField()
    imageb = models.BinaryField()
    slug = models.SlugField()

def readImage(filename):
    # Подключение к файлу
    fin = open(filename, "rb")
    img = fin.read()
    return img
    # Закрываем подключение с файлом
    fin.close()

def pre_save_imageb(sender, instance, *args, **kwargs):
    name = 'media' + '/' + str(instance.image)
    data = readImage(name)
    #binary = Binary(data)
    #print(data)
    instance.imageb = data


pre_save.connect(pre_save_imageb, sender = Car)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=10, blank=True, null=True, choices= (('user', 'user'),('admin','admin')))

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
    	return self.login

def pre_save_user_user_type(sender, instance, *args, **kwargs):
	if not instance.user_type:
		instance.user_type = 'user'

pre_save.connect(pre_save_user_user_type, sender = User)

class Cars(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=30)
    model = models.CharField(max_length=60)
    carcass = models.CharField(max_length=100) 
    years_of_productions = models.CharField(max_length=10)
    engines = models.TextField(max_length=1000) 
    transmissions = models.CharField(max_length=50)
    drive_units = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cars'
        ordering = ['mark', 'model']    	

    def __str__(self):
    	return (self.mark + ' ' + self.model)    

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'
        ordering = ['name']    	

    def __str__(self):
    	return (self.name)

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    #login = models.ForeignKey('User', models.DO_NOTHING, unique=True)
    login = models.ForeignKey('User', on_delete=models.CASCADE)
    fio = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    person = models.CharField(max_length=23, blank=True, null=True, choices= (('физическое лицо', 'физическое лицо'),('частный предприниматель','частный предприниматель')))

    class Meta:
        managed = False
        db_table = 'customers'

    def __str__(self):
    	return (self.fio)   

class Deliveries(models.Model):
    id = models.AutoField(primary_key=True)
    shipper = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)
    date_order = models.DateField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'deliveries'  

#Вы можете ссылаться на поля внешнего ключа в столбце STR, но если вы также не установите list_display в ModelAdmin для модели A, я бы не рекомендовал его, если вам нужен гибкий модуль администрирования.
#Вы получите буквально тысячи запросов для каждой загрузки страницы. Любая задача удаления большого объема станет видением яиц.
#попытка решения https://www.youtube.com/watch?v=uT114PqFJgY
    def __str__(self):
    	return (str(self.id) + ' ' + self.shipper.name + ' ' + self.car.mark + ' ' + self.car.model) #опасное место

class MycarManager(models.Manager):
    def all(self, order_by_cost, order_by_cost_distinct, order_by_year, order_by_year_distinct, order_news, first_cost, last_cost, first_year, last_year, filter_mark, filter_model, filter_body, filter_color, filter_engine, filter_KPP, filter_unit, first_mileage, last_mileage, filter_supplier, *args, **kwargs):
        if order_by_cost == 'true':
            return super(MycarManager, self).get_queryset().filter(visible='True').order_by('cost')
        if order_by_cost_distinct == 'true':
            return super(MycarManager, self).get_queryset().filter(visible='True').order_by('cost').reverse()
        if order_by_year == 'true':
            return super(MycarManager, self).get_queryset().filter(visible='True').order_by('car_year')
        if order_by_year_distinct == 'true':
            return super(MycarManager, self).get_queryset().filter(visible='True').order_by('car_year').reverse()
        if order_news == 'true':
            return super(MycarManager, self).get_queryset().filter(visible='True').order_by('date_of_delivery').reverse()
        if order_news == None:
            if first_cost == None and last_cost == None and first_year == None and last_year == None:
                return super(MycarManager, self).get_queryset().filter(visible='True')
            if first_cost == '':
                first_cost = 0
            if last_cost == '':
                last_cost = 10000000
            if first_year == '':
                first_year = "1900"
            if last_year == '':
                last_year = "1990"
            if first_mileage == '':
                first_mileage = 0
            if last_mileage == '':
                last_mileage = 10000000
            return super(MycarManager, self).get_queryset().filter(visible='True').filter(cost__gte = first_cost).filter(cost__lte = last_cost).filter(car_year__gte = first_year).filter(car_year__lte = last_year).filter(car__car__mark__contains = filter_mark).filter(car__car__model__contains = filter_model).filter(car_body__contains = filter_body).filter(color__contains = filter_color).filter(engine__contains = filter_engine).filter(transmission__contains = filter_KPP).filter(drive_unit__contains = filter_unit).filter(mileage__gte = first_mileage).filter(mileage__lte = last_mileage).filter(car__shipper__name__contains = filter_supplier)
        if order_news == "WordOrder":
            if first_cost == None and last_cost == None and first_year == None and last_year == None:
                return super(MycarManager, self).get_queryset().filter(visible='True')
            if first_cost == '':
                first_cost = 0
            if last_cost == '':
                last_cost = 10000000
            if first_year == '':
                first_year = "1900"
            if last_year == '':
                last_year = "1990"
            return super(MycarManager, self).get_queryset().filter(visible='True').filter(cost__gte = first_cost).filter(cost__lte = last_cost).filter(car_year__gte = first_year).filter(car_year__lte = last_year).filter(car__car__mark__contains = filter_mark).filter(car__car__model__contains = filter_model).filter(car__shipper__name__contains = filter_supplier)


MYCAR_BODY_CHOICES = (
    ('купе', 'купе'),
    ('унивесал', 'унивесал'),
    ('хетчбэк', 'хетчбэк'),
    ('кабриолет', 'кабриолет'),
    ('родстер', 'родстер'),
    ('пикап', 'пикап'),
    ('лимузин', 'лимузин'),
    ('тарга', 'тарга'),
    ('внедорожник', 'внедорожник'),
    ('кроссовер', 'кроссовер'),
    ('фурнон', 'фургон'),
    ('автобус', 'автобус'),
    ('микроавтобус', 'микроавтобус'),
    ('гузовик', 'грузовик'),
    ('минивэн', 'минивэн')
)

Years = [('1900', '1900'), ('1901','1901')]
for i in range(1902,2000):
    adder = (str(i),str(i))
    Years.append(adder)

class Mycar(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey('Deliveries', on_delete=models.CASCADE)
    car_body = models.CharField(max_length=20, choices=MYCAR_BODY_CHOICES)
    car_year = models.CharField(max_length=4, choices=Years)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=20)
    drive_unit = models.CharField(max_length=5, choices=(('RWD','RWD'),('AWD','AWD'),('FWD','FWD')))
    color = models.CharField(max_length=25)
    mileage = models.BigIntegerField(blank=True, null=True, default = 0)
    identification_number = models.CharField(max_length=20)
    cost = models.FloatField(blank=True)
    photos = models.ImageField()
    date_of_delivery = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    options = models.CharField(max_length=200, blank=True, null=True)
    visible = models.CharField(max_length=10, default = 'True' , choices=(('True','True'),('False','False')))
    slug = models.SlugField(blank = True)
    imageb = models.BinaryField()
    objects = MycarManager()

    class Meta:
        managed = False
        db_table = 'mycars'

    def __str__(self):
    	return(self.car.car.mark + ' ' + self.car.car.model + ' ' + self.options + ' ' + self.car_year + ' ' + self.identification_number)

    def get_absolute_url(self):
    	return reverse('mycar_detail', kwargs={'mycar_slug': self.slug})


def pre_save_imageb(sender, instance, *args, **kwargs):
    if instance.slug:
        name = 'media' + '/' + str(instance.photos)
        data = readImage(name)
        instance.imageb = data

pre_save.connect(pre_save_imageb, sender = Mycar)

def pre_save_mycar_slug(sender, instance, *args, **kwargs):
        if not instance.slug:
            slug = slugify(str(instance.car.car.mark+instance.car.car.model+instance.car_year+instance.identification_number))
            instance.slug = slug

pre_save.connect(pre_save_mycar_slug, sender = Mycar)



class Request(models.Model):
    id = models.AutoField(primary_key=True)
    car = models.ForeignKey('Mycar', on_delete=models.CASCADE)
    date_request = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    request_status = models.CharField(max_length=20, choices=(('на рассмотрении','на рассмотрении'), ('принята', 'принята'), ('отклонена', 'отклонена')))
    delivery = models.CharField(max_length=10, choices=(('Нет','Нет'), ('Да', 'Да')))
    delivery_address = models.CharField(max_length=200, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requests'

    def __str__(self):
    	return(str(self.id) + ' ' + self.car.car.car.mark + ' ' + self.car.car.car.model + ' ' 
    		+ self.car.car_year + ' ' + self.car.identification_number + ' ' + str(self.date_request) + ' ' + self.request_status)

def pre_save_request_delivery_address(sender, instance, *args, **kwargs):
    if instance.delivery == 'Да' and not instance.delivery_address:
        instance.delivery_address = instance.customer.address
    if instance.delivery == 'Да' and not (instance.cost and instance.cost != instance.car.cost):
        instance.cost = instance.car.cost * 1.03
    if instance.delivery == 'Нет' and not(instance.cost and instance.cost != instance.car.cost * 1.03):
        instance.cost = instance.car.cost
    if instance.delivery == 'Нет':
        instance.delivery_address = ''
    mycar = Mycar.objects.get(slug = instance.car.slug)
    mycar.visible = 'False'
    mycar.save()
    if instance.request_status == 'отклонена':
        mycar.visible = 'True'
        mycar.save()
    if instance.request_status == 'принята':
        new_order = Order(request=instance, order_status='выполняется', start_date = datetime.today())
        new_order.save()

pre_save.connect(pre_save_request_delivery_address, sender = Request)

@receiver(pre_delete, sender=Request, dispatch_uid='request_delete_signal')
def log_deleted_question(sender, instance, using, **kwargs):
    mycar = Mycar.objects.get(slug = instance.car.slug)
    mycar.visible = 'True'
    mycar.save()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey('Request', on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, choices=(('выполняется','выполняется'),('готов','готов')))
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
    	return(str(self.id) + ' ' + self.request.customer.fio + ' ' + self.request.car.car.car.mark + ' ' + 
    		self.request.car.car.car.model + ' ' + self.request.car.car_year
    		+' '+ self.order_status)

def pre_save_order_start_date(sender, instance, *args, **kwargs):
    if instance.order_status == 'выполняется' and not instance.start_date:
        instance.start_date = datetime.today()
    if instance.order_status == 'готов' and not instance.end_date:
        instance.end_date = datetime.today()

pre_save.connect(pre_save_order_start_date, sender = Order)
