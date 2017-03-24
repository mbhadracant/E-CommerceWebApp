from product.models import Category
def template_processor(request):
    categories = Category.objects.all()
    basket_amount = len(request.session['basket'])
    return {'categories': categories, 'basket_amount': basket_amount}