#hello.py
from product.models import Category, Subcategory

def create_category_and_subcategories_from_data():
    f = open("data.txt")
    Subcategory.objects.all().delete()
    Category.objects.all().delete()
    for line in f:
        category = line.split(":")[0]
        category_db = Category(category=category)
        category_db.save()

        for word in line.split(":")[1].split(","):
            sub = word.strip(" ")
            sub_db = Subcategory(category_id=category_db, subcategory=sub)
            sub_db.save()

def generate_subcategory_img():
    subs = Subcategory.objects.all()
    for sub in subs:
        name = sub.name
        name = name.replace(" ", "-")
        name = name.lower()
        name += "-icon.png"
        sub.subcategory_image = name
        sub.save()

def run():
    generate_subcategory_img()


