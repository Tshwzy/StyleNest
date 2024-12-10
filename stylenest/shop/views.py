from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
def product_list(request):
    products = Product.objects.all() 
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_details.html', {'product': product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})
    cart[pk] = cart.get(pk, 0) + 1
    request.session['cart'] = cart
    return redirect('shop:product_list')

def cart(request):
    # Fetch cart data from the session
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    # Create a new cart dictionary to hold only valid product IDs
    valid_cart = {}

    for product_id, quantity in cart.items():
        try:
            # Try to get the product; if not found, it will raise Product.DoesNotExist
            product = Product.objects.get(pk=product_id)
            cart_items.append({'product': product, 'quantity': quantity})
            total_price += product.price * quantity
            
            # If the product is valid, add it to the valid_cart dictionary
            valid_cart[product_id] = quantity
        except Product.DoesNotExist:
            # Product doesn't exist, skip it and don't add it to valid_cart
            continue

    # Update the session with the valid cart
    request.session['cart'] = valid_cart

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, "Your cart is empty. Please add items to cart before checking out.")
            return redirect('shop:cart')

        # Create an order for the current user
        order = Order.objects.create(customer=request.user, status='Pending')

        # Create OrderItems for each item in the cart
        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(pk=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)
            except Product.DoesNotExist:
                continue  # Skip any products that don't exist

        # Clear the cart after placing the order
        request.session['cart'] = {}

        messages.success(request, "Your order has been placed successfully!")
        return redirect('shop:product_list')

    return render(request, 'shop/checkout.html')



@login_required
def staff_order_list(request):
    orders = Order.objects.all()  # Display all orders
    return render(request, 'shop/staff_order_list.html', {'orders': orders})

@login_required
def accept_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    #if not request.user.groups.filter(name='Staff').exists():
        #return redirect('home')  # Redirect if not staff
    
    order.status = 'Accepted'
    order.save()
    return redirect('shop:staff_order_list')

@login_required
def prepare_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    #if not request.user.groups.filter(name='Staff').exists():
        #return redirect('home')  # Redirect if not staff

    order.status = 'Preparing'
    order.save()
    return redirect('shop:staff_order_list')

@login_required
def deliver_order(request, pk):
    #if not request.user.groups.filter(name='Staff').exists():
        #return redirect('home')  # Redirect if not staff

    order = get_object_or_404(Order, pk=pk)
    order.status = 'Delivered'
    order.save()
    
    # Optionally, display a success message
    messages.success(request, "Order has been marked as delivered.")

    # Redirect to the staff order list
    return redirect('shop:staff_order_list')

@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    #if not request.user.groups.filter(name='Staff').exists():
        #return redirect('home')  # Redirect if not staff

    order.status = 'Canceled'
    order.save()
    return redirect('shop:staff_order_list')

@login_required
def client_order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'shop/client_order_list.html', {'orders': orders})