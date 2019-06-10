from django.shortcuts import render
from django.http import HttpResponse
from.models import product, Contact
from math import ceil

# Create your views here.


def index(request):
    ''' Fetch all the items by using objects.all()
     then declare varriable for length of slides and give the formula
     Create a dictionary by name params iside this set no_of_slides and range and product
     This is using for display all the product in homepage what ever we set product in db in Admin Page

    products = product.objects.all()
    print(products)
    n = len(products)
    slides =  n//4 + ceil((n/4) - (n//4))
'''
    ''' This is for multiple slides .if we want use single slide then direct use on param. but for multiple slides
    first you create a dictionary and pass the .product and product range and nSlides
     params = {'no_of_slides' : slides, 'range': range(1, slides), 'product' : products}
    
    allProduct = [[products, range(1, slides), slides],
                  [products,range(1,slides), slides]]
    params = {'allProduct': allProduct}  '''
    ''' For display every product category wise'''
    myProd = []
    displayProd = product.objects.values('category', 'id')
    valCat = {item['category'] for item in displayProd}
    for cat in valCat:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        # Here is the formmula of slide the screen based on the image.
        slides = n // 4 + ceil((n / 4) - (n // 4))
        myProd.append([prod, range(1, slides), slides])
        params = {'allProduct': myProd}
    return render(request, 'shopping/index.html', params)


def about(request):
    return render(request, 'shopping/about.html')


'''   In this contact methode  fetch the detail from user and store in db   '''


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        '''Inside this contact method first name we put whatever we give in DB same name  and second name is same as here
        on where store the value
        ONE OF THE BEST TUTORIAL #42
        '''
    return render(request, 'shopping/contact.html')


def tracker(request):
    return render(request, 'shopping/tracker.html')


def search(request):
    return render(request,'shopping/search.html')


def checkout(request):
    return render(request, 'shopping/checkOut.html')


'''  fetch the details with id  '''


def productview(request, prid):

    prod = product.objects.filter(id=prid)

    return render(request, 'shopping/productView.html', {'product': prod[0]})


''' Display all the record from Product  '''


def productlist(request):
    context = {
        'product':product.objects.all()
    }
    return render(request,'shopping/product.html',context)


def cart(request):
    return HttpResponse("Hello")

