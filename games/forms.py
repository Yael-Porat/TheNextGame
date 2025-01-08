from django import forms

class AdvancedSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    min_price = forms.DecimalField(required=False, min_value=0, label='Min Price')
    max_price = forms.DecimalField(required=False, min_value=0, label='Max Price')
    min_rating = forms.DecimalField(required=False, min_value=0, label='Min Rating')
    max_rating = forms.DecimalField(required=False, min_value=0, label='Max Rating')
    category = forms.CharField(required=False, label='Category')
    min_players = forms.IntegerField(required=False, min_value=1, label='Min Players')
    max_players = forms.IntegerField(required=False, min_value=1, label='Max Players')
    min_duration = forms.IntegerField(required=False, min_value=1, label='Min Duration')
    max_duration = forms.IntegerField(required=False, min_value=1, label='Max Duration')

    # Optionally, you can provide choices for some fields like 'category' and 'rating'
    CATEGORY_CHOICES = [
        ('strategy', 'Strategy'),
        ('family', 'Family'),
        ('party', 'Party'),
        # Add other categories as necessary
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label='Category')
