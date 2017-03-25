from product.models import Category
def template_processor(request):

    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    basket = request.session['basket']

    quantity = 0
    for key, value in basket.items():
        quantity = quantity + value

    context['basket_amount'] = quantity

    if('account' in request.session):
        context['account'] = request.session['account']

    return context