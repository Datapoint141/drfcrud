import faker
from products.models import ProductsInfoModel
import random
fk = faker.Faker()
def statFaking(count):
    for x in range(count):
        productName = fk.country()
        price = random.randint(10000,40000)
        productVendor = fk.url()
        addeddate = fk.date()
        record = ProductsInfoModel.objects.get_or_create(productName=productName, price=price, productVendor=productVendor, addeddate=addeddate)
statFaking(100)