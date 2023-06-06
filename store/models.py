from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    """
    model for type of estate(product)
    """
    name = models.CharField(max_length=200,
                            help_text='Enter type of estate')

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[str(self.name)])

    def __str__(self):
        return self.name


class Producer(models.Model):
    """
    model for owner
    """
    name = models.CharField(max_length=200,
                            help_text='Enter owner name')
    country = models.CharField(max_length=200,
                               help_text='Enter where you are going to have estate')

    def get_absolute_url(self):
        return reverse('producer-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    module for estate(product estate)
    """
    name = models.CharField(max_length=200)
    producer = models.ForeignKey('Producer',
                                 on_delete=models.SET_NULL,
                                 null=True)
    cost = models.IntegerField()
    type = models.ForeignKey('ProductType',
                             on_delete=models.SET_NULL,
                             null=True)
    quantity = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    purchase_count = models.PositiveIntegerField(default=0)
    UNITS = (
        ('$', 'dollars'),
        ('€', 'euro'),
        ('D', 'dirhams')
    )

    units = models.CharField(max_length=2,
                             choices=UNITS,
                             help_text="units of estate")

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    module for client
    """
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
