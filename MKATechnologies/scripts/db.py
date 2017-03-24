#hello.py
from product.models import Category, Subcategory

def create_category_and_subcategories_from_data():
    f = open("categories.txt")
    Subcategory.objects.all().delete()
    Category.objects.all().delete()
    for line in f:
        print(line)
        category = line.split(":")[0]
        url_name = category.lower()
        category_db = Category(name=category,url_name=url_name)
        category_db.save()
        for word in line.split(":")[1].split(","):
            sub = word.strip(" ")
            sub_db = Subcategory(category_id=category_db, name=sub, subcategory_image="test")
            sub_db.save()
    print("done")

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
    create_category_and_subcategories_from_data
    generate_subcategory_img()


