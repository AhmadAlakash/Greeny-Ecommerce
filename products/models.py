

from django.db import models
from django.utils.translation import gettext_lazy as _  # to translation
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


flag_type = (
    ('New','New'),
    ('Feature', 'Feature'),
    ('Sale','Sale'),

)

class product(models.Model):
    name = models.CharField(_('Name'), max_length=100,)
    subtitle = models.CharField(_('Subtitle'),max_length=300)
    description= models.TextField(_('Description'),max_length=10000)
    sku=models.IntegerField(_("Sku"))
    price = models.FloatField(_('Price'),)
    video_url = models.URLField(_(' Video_Url'),null=True, blank=True)
    category=models.ForeignKey('category',verbose_name=_('Category'),related_name='product_category',on_delete=models.CASCADE)
    brand = models.ForeignKey(
        'brand',verbose_name=_('Brand'), related_name='product_brand', on_delete=models.CASCADE)
    image= models.ImageField(_('Image'),upload_to='products/')
    flag =models.CharField(_('Flag'),max_length=10)
    tags = TaggableManager()

    def __str__(self):
        return self.name






class product_image(models.Model):
    product = models.ForeignKey(product, verbose_name=_('Product'), on_delete=models.CASCADE)
    image= models.ImageField(_('Image'),upload_to='product_imges')

    def __str__(self):
        return str(self.product)








class category(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    image = models.ImageField(_('Image'), upload_to='category/')

    def __str__(self):
        return self.name








class brand (models.Model):
   name = models.CharField(_('Name'),  max_length=100)
   image = models.ImageField(_('Image'),upload_to='products/')
   category = models.ForeignKey(
       category, verbose_name=_('Category'), related_name='brand_category', on_delete=models.CASCADE)

   def __str__(self):
       return self.name





class product_review(models.Model):
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(
        product, verbose_name=_('Product'), related_name='product_review', on_delete=models.CASCADE)
    review = models.CharField(_('Review'), max_length=400)
    rate = models.IntegerField(_('Rate'))
    created_at=models.DateTimeField(_(' Created_At'),default=timezone.now)  

    def __str__(self):
        return str(self.user)
