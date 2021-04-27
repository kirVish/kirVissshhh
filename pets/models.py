from django.db import models


# Create your models here.
class Pet(models.Model):
    kind = models.CharField(verbose_name='Животное', max_length=50)
    name = models.CharField(verbose_name='Кличка', max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)
    email = models.EmailField(verbose_name='E-mail')
    description = models.TextField(verbose_name='Описание')
    date_posted = models.DateField(verbose_name='Дата подачи объявления')
    photo = models.ImageField(verbose_name='Фото', upload_to='uploads/photos/', null=True)
    def __str__(self):
        return '{},{},{},{},{},{}' .format (self.kind , self.name, self.phone_number, self.email, self.description, self.date_posted)
    class Meta:
        ordering = ['-date_posted']
