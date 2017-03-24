from product.models import Category
def template_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}