from django import forms
from .models import Customer, Category,Artist, Product,Purchase

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'identity_card': 'Cédula de Identidad',
            'name': 'Nombre',
            'phone': 'Teléfono',
            'email': 'Correo Electrónico',
            'address': 'Dirección',
        }

        widgets = {
            'identity_card': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_name': 'Nombre de la Categoría',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'})
        } 

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'name': 'Nombre del Artista',
            'country': 'País de Origen',
            'category': 'Categoría',
            'picture': 'Foto del Artista',
            'artist_type': 'Tipo de Artista',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'artist_type': forms.Select(attrs={'class': 'form-control'})
        } 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'title': 'Título del Producto',
            'code': 'Código',
            'quantity': 'Cantidad',
            'price': 'Precio',
            'release_year': 'Año de Lanzamiento',
            'artist': 'Artista',
            'category': 'Categoría',
            'picture': 'Imagen del Producto',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        } 

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer', 'date']
        labels = {
            'customer': 'Cliente',
            'date': 'Fecha de Compra',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        