from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect,render

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from discos.forms import CustomerForm, CategoryForm,ArtistForm, ProductForm, PurchaseForm
from .models import Customer, Category,Artist, Product,Purchase

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def purchase_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase_list.html', {'purchases': purchases})







def index(request):
    return render(request, 'index.html')

def customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    template = loader.get_template('display_customer.html')
    context = {
        'customer': customer
    }
    return HttpResponse(template.render(context, request))

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    template = loader.get_template('display_category.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    template = loader.get_template('display_purchase.html')
    context = {
        'purchase': purchase
    }
    return HttpResponse(template.render(context, request))

#CUSTOMER
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = CustomerForm()
    
    return render(request, 'customer_form.html', {'form': form})

@login_required
def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = CustomerForm(instance=customer)
        
    return render(request, 'customer_form.html', {'form': form})

@login_required
def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()
    return redirect("discos:index")

#CATEGORY
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = CategoryForm()
    
    return render(request, 'category_form.html', {'form': form})

@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = CategoryForm(instance=category)
        
    return render(request, 'category_form.html', {'form': form})


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect("discos:index")

#ARTIST
@login_required
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ArtistForm()
    
    return render(request, 'artist_form.html', {'form': form})


@login_required
def edit_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ArtistForm(instance=artist)
        
    return render(request, 'artist_form.html', {'form': form})


@login_required
def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    artist.delete()
    return redirect("discos:index")

#PRODUCT
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ProductForm()
    
    return render(request, 'product_form.html', {'form': form})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'product_form.html', {'form': form})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect("discos:index")


#PURCHASE
@login_required
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:index')
    else:
        form = PurchaseForm()
    
    return render(request, 'purchase_form.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

