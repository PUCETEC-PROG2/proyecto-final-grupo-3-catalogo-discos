from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    picture = models.ImageField(upload_to='artist_images')  
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=False)
    price = models.DecimalField(null=False, default=1,max_digits=4,decimal_places=2)
    release_year = models.IntegerField(null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)   
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  
    picture = models.ImageField(upload_to='album_images') 

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=30, null=False)
    
    def __str__(self) -> str:
        return self.category_name 
    
class Customer(models.Model):
    identity_card = models.CharField(max_length=10,null=False)
    name = models.CharField(max_length=100,null=False)
    phone = models.CharField(max_length=10,null=False)
    email = models.CharField(max_length=50,null=False)
    address = models.CharField(max_length=100,null=False)

    def __str__(self) -> str:
        return self.name
    
class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    total_price = models.DecimalField(null=False, default=1,max_digits=4,decimal_places=2)
    
    def __str__(self) -> str:
        return f'Purchase by {self.customer.name} on {self.date}'

