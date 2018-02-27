from django.conf.urls import url
from . import views

app_name='contact'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.ProductPageView.as_view(),name='productpage'),
    url(r'^(?P<pk>[0-9]+)/purchase$', views.purchase, name='purchase'),
    url(r'^add/$',views.ProductCreate.as_view(),name='product-add'),
]