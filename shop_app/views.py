import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import Product_update_Form
from datetime import date

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'сработало представление index ')
    content = {'dz': [s for s in 'Задание №6 Доработаем задачу про клиентов, '
                                 'заказы и товары из прошлого семинара. '
                                 'Создайте форму для редактирования товаров в базе'
                                 'данных. Измените модель продукта, добавьте поле для'
                                 ' хранения фотографии продукта. Создайте форму, которая'
                                 ' позволит сохранять фото. http://127.0.0.1:8000/shop/productupgrete/'.split('.')]}
    return render(request, 'shop_app/index.html', content)


def product_upgrete(request):
    if request.method == 'POST':
        logger.info('**********start product_upgrete')
        form = Product_update_Form(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            date_registration = form.cleaned_data['date_registration']
            product = Product(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                date_registration=date_registration.__str__(),
            )
            product.save()
            message = 'Продукт сохранен сохранён'
    else:
        form = Product_update_Form()
        message = 'Заполните форму'
    return render(request, 'shop_app/product_create.html', {'form': form, 'message': message,})

