from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import render ,get_object_or_404
from .models import Product

class IndexView(generic.ListView):
    template_name = 'product/index.html'
    def get_queryset(self):
        return Product.objects.all()


class ProductPageView(generic.DetailView):
    model=Product
    template_name='product/productpage.html'

def purchase(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    try:
        selected_version=product.versions_set.get(pk=request.POST['version'])
    except (KeyError,selected_version.DoesNotExist):
        return render(request,'product/productpage.html',{'product':product,'error_message':"select a valid version of the product", })
    else :
        selected_version.is_purchased=True
        selected_version.save()
        return render(request, 'product/productpage.html', {'product': product, })


class ProductCreate(CreateView):
    model = Product
    fields=['productName','productLogo']