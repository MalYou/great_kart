from .models import Cart, CartItem
from .views import _cart_id

def menu_cart_items(request):
    total_cart_items = 0

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart)

            if cart_items:
                for item in cart_items:
                    total_cart_items += item.quantity
        except Cart.DoesNotExist:
            total_cart_items = 0

    return dict(total_cart_items=total_cart_items)
