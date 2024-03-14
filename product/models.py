from django.db import models
from users.models import User,BaseModel
from django.core.validators import FileExtensionValidator

class Category(BaseModel):
    name=models.CharField(max_length=100)
    

    def __str__(self):
        return self.name


class Product(BaseModel):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products')
    description=models.TextField(default='',null=True, blank=True)
    image=models.ImageField(upload_to='product_images/',null=True,validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png','jpeg'])])


    def __str__(self):
        return self.name

