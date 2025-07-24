from django.shortcuts import render, redirect, get_object_or_404
from .models import Beverage, Ingredient
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'home.html', {'ingredients': ingredients})

from django.shortcuts import render, get_object_or_404
from .models import Beverage, Ingredient

@csrf_exempt
def customize(request, name):
    beverage = get_object_or_404(Beverage, name=name)

    # Default quantities for UI display
    default_quantities = {
        'tea': beverage.tea_qty,
        'coffee': beverage.coffee_qty,
        'milk': beverage.milk_qty,
        'sugar': beverage.sugar_qty
    }

    # Prices per unit
    prices = {
        'tea': beverage.tea_price,
        'coffee': beverage.coffee_price,
        'milk': beverage.milk_price,
        'sugar': beverage.sugar_price
    }

    # Fetch ingredient stock in one query
    ingredients = Ingredient.objects.in_bulk(field_name='name')
    ingredient_stock = {
        'tea': ingredients['tea'].quantity,
        'coffee': ingredients['coffee'].quantity,
        'milk': ingredients['milk'].quantity,
        'sugar': ingredients['sugar'].quantity
    }

    if request.method == 'POST':
        tea = int(request.POST.get('teaQty', 0))
        coffee = int(request.POST.get('coffeeQty', 0))
        milk = int(request.POST.get('milkQty', 0))
        sugar = int(request.POST.get('sugarQty', 0))

        # Check stock availability
        if (tea > ingredient_stock['tea'] or
            coffee > ingredient_stock['coffee'] or
            milk > ingredient_stock['milk'] or
            sugar > ingredient_stock['sugar']):
            
            return render(request, 'customize.html', {
                'beverage': beverage,
                'default_quantities': default_quantities,
                'prices': prices,
                'ingredient_stock': ingredient_stock,
                'error': 'Not enough stock for requested quantities.'
            })

        # Deduct and save updated ingredient quantities
        ingredients['tea'].quantity -= tea
        ingredients['coffee'].quantity -= coffee
        ingredients['milk'].quantity -= milk
        ingredients['sugar'].quantity -= sugar

        ingredients['tea'].save()
        ingredients['coffee'].save()
        ingredients['milk'].save()
        ingredients['sugar'].save()

        return render(request, 'customize.html', {
            'beverage': beverage,
            'default_quantities': default_quantities,
            'prices': prices,
            'ingredient_stock': ingredient_stock,
            'success': True
        })

    return render(request, 'customize.html', {
        'beverage': beverage,
        'default_quantities': default_quantities,
        'prices': prices,
        'ingredient_stock': ingredient_stock
    })


@csrf_exempt
def admin_panel(request):
    ingredients = Ingredient.objects.all()
    if request.method == "POST":
        for ingredient in ingredients:
            new_qty = request.POST.get(ingredient.name)
            if new_qty:
                ingredient.quantity = int(new_qty)
                ingredient.save()
        return redirect('admin_panel')
    return render(request, 'admin_page.html', {'ingredients': ingredients})
