from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        product = Product(name='Apple',
                          description='Orange very goods, he from in Indonesia',
                          price=1.2,
                          quantity=300
                          )
        ...
        product.save()
        self.stdout.write(f'{product}')
