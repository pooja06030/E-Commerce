from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)        # on delete models.cashcade ka mtlab catergory delete ki mene to usse related sare product delete ho jayenge
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')     # import liabrery pillow using image
    
   

    
    
  