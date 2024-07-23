from django.db import models
from auth_app.models import Customuser
from products.models import Product

# Create your models here.


class Wishlist(models.Model):
    user=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    product=models.ForeignKey( Product,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    @property
    def selling_price(self):
        Totel=0
        offer = None
        if self.product.catagory.main_category.category_offer:
            offer = self.product.catagory.main_category.category_offer
            Totel = self.product.orginal_price-(offer*self.product.orginal_price //100)
            if self.product.product_offer:
                if offer < self.product.product_offer:
                    offer = self.product.product_offer
                    Totel = self.product.orginal_price-(offer*pro.orginal_price //100)
                else:
                    Totel = self.product.orginal_price-(offer*self.product.orginal_price //100)
        elif self.product.product_offer:
            offer = self.product.product_offer
            Totel=self.product.orginal_price-(offer*self.product.orginal_price //100)
        else:
            Totel=self.product.orginal_price
        return Totel 