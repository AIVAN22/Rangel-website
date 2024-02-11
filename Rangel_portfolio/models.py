from django.db import models


# Create your models here.
def generate_image_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{instance.custom_filename}.{ext}"
    return f"images/{filename}"


class Product(models.Model):
    CATEGORIES = [
        ("Oil-Painting", "Oil-Painting"),
        ("Watercolors", "Watercolors"),
        ("Dry-Crayons", "Dry-Crayons"),
        ("Oil-Crayons", "Oil-Crayons"),
    ]
    CANVAS_ = [
        ("Canvas", "Canvas"),
        ("Cardboard", "Cardboard"),
    ]
    canvas = models.CharField(max_length=350, choices=CANVAS_, default=1)
    categories = models.CharField(max_length=350, choices=CATEGORIES, default=1)
    name = models.CharField(max_length=350, null=True)
    title = models.CharField(max_length=350, null=True)
    content = models.TextField(max_length=10000, null=True)
    custom_filename = models.CharField(max_length=250, null=False, default="default")
    img = models.ImageField(
        upload_to=generate_image_filename, default="images/default.jpg"
    )

    def __str__(self):
        return self.title


class PurchaseEmail(models.Model):
    name = models.CharField(max_length=50, null=False, default="default")
    email = models.CharField(max_length=250, null=False, default="default")
    content = models.TextField(max_length=10000, null=True)
    send_at = models.DateTimeField(("Received_At"), auto_now=True, null=True)
