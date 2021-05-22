from django.core.management.base import BaseCommand

from wbparser.models import Product
from wbparser.parser import get_products


class Command(BaseCommand):
    help = 'Run wb category parser'

    def add_arguments(self, parser):
        parser.add_argument(
            dest='category_url',
            default=True,
            type=str,
            help="parse products of category")

    def handle(self, *args, **options):
        products = get_products(options['category_url'])
        if products:
            Product.objects.all().delete()
            product_instances = []
            for p in products:
                strip_product_data = {k: v.strip() for k, v in p.items() if v}
                product_instances.append(
                    Product(**strip_product_data)
                )
            Product.objects.bulk_create(product_instances)
        self.stdout.write("Complete", ending='')
