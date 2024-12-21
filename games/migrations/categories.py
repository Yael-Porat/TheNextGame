from django.db import migrations


def add_categories(apps, schema_editor):
    # Get the Category model
    Category = apps.get_model('games', 'Category')

    # List of categories to add
    categories = [
        {"name": "Strategy", "description": "Games focused on careful planning and tactics."},
        {"name": "Party", "description": "Games designed for social gatherings and fun."},
        {"name": "Family", "description": "Games suitable for players of all ages."},
        {"name": "Card", "description": "Games that primarily use cards as the main component."},
        {"name": "Cooperative", "description": "Games where players work together to achieve a goal."},
    ]

    # Add each category
    for category in categories:
        Category.objects.create(**category)


def remove_categories(apps, schema_editor):
    # Get the Category model
    Category = apps.get_model('games', 'Category')

    # Names of categories to remove
    category_names = ["Strategy", "Party", "Family", "Card", "Cooperative"]

    # Delete categories by name
    Category.objects.filter(name__in=category_names).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_categories, remove_categories),
    ]
