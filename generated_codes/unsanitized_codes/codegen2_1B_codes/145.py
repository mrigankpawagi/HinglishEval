
def order_by_points(nums):
    """
    Ek function likho jo diye gaye integers ki list ko unke digits ka sum ke hisaab se ascending order mein sort kare.
    Dhyan do: agar kuch items ke digits ka sum similar ho, 
    toh unhe original list ke index ke basis par order karo.

    Jaise ki:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums: return []
    else:
        return nums.sort(reverse=True)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
    <|python|>from django import forms
from django.db import models
import re


class AddressForm(forms.ModelForm):
    street_address = forms.CharField(label="Street Address",
                                      help_text="Use these field to enter the street address",
                                      required=False)
    other_line = forms.CharField(label="Other line",
                                    help_text="Use these field to enter the other line to identify the landmark(s)",
                                    required=False)
    unit_number = forms.CharField(label="Unit Number",
                                    help_text="Use these field to enter the unit number",
                                    required=False)
    floor = forms.CharField(label="Floor",
                                  help_text="Use these field to enter the floor number",
                                  required=False)
    apartment_number = forms.CharField(label="Apartment number",
                                           help_text="Use these field to enter the apartment number",
                                           required=False)
    city = forms.CharField(label="City",
                                     help_text="Use these field to enter the city address",
                                     required=False)
    postal_code = forms.CharField(label="Postal Code",