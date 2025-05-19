from django.core.management.base import BaseCommand
from blogapp.models import Category, Tag, Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Create sample categories all
        categories = Category.objects.all()
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(type(item))

        print('End of the script')

# select one category
        category = Category.objects.get(name='Health')
        print(category)
        print(type(category))

#    some categories
        categories = Category.objects.filter(name__in=['Health', 'Travel'])
        print(categories)
        print(type(categories))
        for item in categories:
            print(item)
            print(type(item))

# связанные поля
        post = Post.objects.first()
        print(post)
        print(type(post))
        print(post.category.name)
        print(post.tags.first().name)

# Create sample categories
    Category.objects.create(name='Sport', description='Sport category')

# Changes
    cat = Category.objects.get(name='Sport')
    cat.name = 'Sport category description'
    cat.save()

# Delete
    cat = Category.objects.get(name='Sport category description')
    cat.delete()
