from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import Product

def index(request):


  allProds = []
  catprods = Product.objects.values('category', 'id')
  cats = {item['category'] for item in catprods}
  for cat in cats:
      prod = Product.objects.filter(category=cat)
      n = len(prod)
      nSlides = n // 4 + ceil((n / 4) - (n // 4))
      allProds.append([prod, range(1, nSlides), nSlides])

  # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
  # allProds = [[products, range(1, nSlides), nSlides],
  #             [products, range(1, nSlides), nSlides]]
  params = {'allProds': allProds}
  return render(request, 'shop/index.html', params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return HttpResponse("we are contact")
def tracker(request):
    return HttpResponse("we are tracker")
def search(request):
    return HttpResponse("we are search")
def productview(request):
    return HttpResponse("we are productview")
def checkout(request):
    return HttpResponse("we are checkout")




