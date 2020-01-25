from django.conf.urls import url
from ecomapp.views import base_view
from ecomapp.views import mycar_view
from ecomapp.views import request_view
from ecomapp.views import order_view
from ecomapp.views import add_to_request_view
from ecomapp.views import remove_from_request_view
from ecomapp.views import change_request_delivery
from ecomapp.views import account_view
from ecomapp.views import registration_view
from ecomapp.views import login_view
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from ecomapp.views import order_by_view
from ecomapp.views import filter_view

urlpatterns = [
   url(r'^mycar/(?P<mycar_slug>[-\w]+)/$', mycar_view, name='mycar_detail'),
   url(r'^requests/$' , request_view, name = 'requests'),
   url(r'^add_to_request/(?P<mycar_slug>[-\w]+)/$', add_to_request_view, name='add_to_request'),
   url(r'^remove_from_request/(?P<mycar_slug>[-\w]+)/$', remove_from_request_view, name='remove_from_request'),
   url(r'^change_request_delivery/$' , change_request_delivery, name = 'change_request_delivery'),
   url(r'^order/$', order_view, name='order'),
   url(r'^account/$', account_view, name='account'),
   url(r'^registration/$', registration_view, name='registration'),
   url(r'^login/$', login_view, name='login'),
   url(r'^logout/$', LogoutView.as_view(next_page = reverse_lazy('base')), name='logout'),
   url(r'^order_by_view/$' , order_by_view, name = 'order_by_view'),
   url(r'^filter_view/$' ,filter_view, name = 'filter_view'),
   url(r'^$', base_view, name='base'),
]