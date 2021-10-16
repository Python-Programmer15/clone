from django.db import models
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
from catalog.models import Category, Product, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    context = {
        'product':Product.objects.all(),
        'category':Category.objects.all()
    }
    # return HttpResponse("<h1>HELO</h1>")
    return render(request, 'home.html', context)

def products(request):
    context = {
        'product':Product.objects.all()
    }
    return render(request, 'product.html', context)

class HomeView(ListView):
    models = Product
    template_name = "home.html"
    queryset = Product.objects.all()


class orderSumaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:        
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object':order
            }
            return render(self.request, "save.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have any saved post")
            return redirect("/")
        

class productDetailView(DetailView):
    models = Product
    template_name = "product.html"
    queryset = Product.objects.all()

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered = False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This post was already saved")
        else:
            messages.info(request, "This post was saved")
            order.items.add(order_item)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This post was saved")

    return redirect("core:product", slug=slug)


def search(request):
    q=request.GET['q']
    context = {
        'product':Product.objects.filter(meta_keywords__icontains=q).order_by('-id')
    }
    return render(request, 'result.html', context)