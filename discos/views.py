from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,redirect,render

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from discos.forms import CustomerForm, CategoryForm,ArtistForm, ProductForm, PurchaseForm
from .models import Customer, Category,Artist, Product,Purchase, PurchaseProduct
from .forms import PurchaseForm
from django.contrib import messages


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
    purchases = Purchase.objects.all().order_by('-date')
    return render(request, 'purchase_list.html', {'purchases': purchases})


def index(request):
    return render(request, 'index.html')

def customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    template = loader.get_template('customer_list.html')
    context = {
        'customer': customer
    }
    return HttpResponse(template.render(context, request))

def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    template = loader.get_template('category_list.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    template = loader.get_template('artist_list.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    template = loader.get_template('product_list.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))


def purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    purchase_products = PurchaseProduct.objects.filter(purchase=purchase)
    context = {
        'purchase': purchase,
        'purchase_products': purchase_products,
    }
    return render(request, 'display_purchase.html', context)



#CUSTOMER
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discos:customer_list')
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
            return redirect('discos:customer_list')
    else:
        form = CustomerForm(instance=customer)
        
    return render(request, 'customer_form.html', {'form': form})

@login_required
def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)
    customer.delete()
    return redirect("discos:customer_list")

#CATEGORY
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discos:category_list')
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
            return redirect('discos:category_list')
    else:
        form = CategoryForm(instance=category)
        
    return render(request, 'category_form.html', {'form': form})


@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect("discos:category_list")

#ARTIST
@login_required
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:artist_list')
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
            return redirect('discos:artist_list')
    else:
        form = ArtistForm(instance=artist)
        
    return render(request, 'artist_form.html', {'form': form})


@login_required
def delete_artist(request, id):
    artist = get_object_or_404(Artist, pk=id)
    artist.delete()
    return redirect("discos:artist_list")

#PRODUCT
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:product_list')
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
            return redirect('discos:product_list')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'product_form.html', {'form': form})


@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect("discos:product_list")


#PURCHASE
@login_required
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('discos:purchase_list')
    else:
        form = PurchaseForm()
    
    return render(request, 'purchase_form.html', {'form': form})

#AÑADIR AL CARRITO
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'title': product.title,
            'price': str(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('discos:product_list')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            # Crear la compra
            purchase = form.save(commit=False)
            purchase.total_price = total_price
            purchase.save()

            # Crear registros en PurchaseProduct
            for product_id, item in cart.items():
                product = Product.objects.get(id=product_id)
                PurchaseProduct.objects.create(
                    purchase=purchase,
                    product=product,
                    quantity=item['quantity']
                )
                # Actualizar la cantidad del producto
                product.quantity -= item['quantity']
                product.save()

            # Vaciar el carrito después de la compra
            request.session['cart'] = {}
            return redirect('discos:purchase_list')
        else:
            print("Formulario no válido:", form.errors)  # Agregado para depuración
    else:
        form = PurchaseForm()

    return render(request, 'view_cart.html', {'cart': cart, 'total_price': total_price, 'form': form})


@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:  # Asegúrate de que estás comparando el `product_id` como string
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            del cart[str(product_id)]
        
        # Actualizar la sesión con el carrito modificado
        request.session['cart'] = cart
        messages.success(request, "Cantidad del producto actualizada en el carrito.")
    else:
        messages.error(request, "El producto no se encontró en el carrito.")

    return redirect('discos:view_cart')


class CustomLoginView(LoginView):
    template_name = 'login.html'

