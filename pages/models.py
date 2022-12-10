from django.db import models
from django.utils.text import slugify
import os
from PIL import Image


def get_about_dir(instance, filename):
    name, ext = os.path.splitext(filename)
    return f"about/{slugify(name)}{ext}"


def get_photos_dir(instance, filename):
    name, ext = os.path.splitext(filename)
    return f"photos/{instance.category.name}/{slugify(name)}{ext}"


def resize_image(image_path, image_size):
    img = Image.open(image_path)

    if img.size[0] > image_size or img.size[1] > image_size:
        img.thumbnail((image_size, image_size))
        # img.save(image_path)
        img.save(image_path, format="webp")


class SiteInfo(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    class Meta:
        verbose_name_plural = "Site Info"

    def __str__(self) -> str:
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to=get_about_dir)
    text = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = "About"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        resize_image(self.image.path, 500)

    def __str__(self) -> str:
        return self.text[:10]


class Categories(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_photos_dir)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image(self.image.path, 1000)

    def __str__(self) -> str:
        return self.image.name