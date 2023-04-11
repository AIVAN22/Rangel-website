from django.db import models

# Create your models here.
def generate_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"static/images/{filename}"

class Product(models.Model):
    CATEGORY = [
        ('category1','category1'),
        ('category2','category2'),
        ('category3','category3'),
        ('category4','category4'),
        ]
    CANVAS_= [
        ('canvas1','canvas1'),
        ('canvas2','canvas2'),
        ('canvas3','canvas3'),
        ]
    canvas = models.CharField(max_length=350, choices=CANVAS_, default=1) 
    categories = models.CharField(max_length=350, choices=CATEGORY, default=1)   
    name =  models.CharField(max_length=350, null=True)
    title = models.CharField(max_length=350, null=True)
    content = models.TextField(max_length=10000,null=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(upload_to=generate_image_filename, default='static/images/default.jpg')
    
    def __str__(self):
        return self.title
    