# -*- coding: utf-8 -*-

"""
Actually, i want to design a django model-like with fields and inline validators,
    of course  time is against me, so i wrote this; close enough (not really) xD

If 'f' is None means that validator generate the content of the field
"""

MAIN_FIELDS = [
    {
        'f': None,  # From JSON
        't': 'offer-id',  # To XML
        'type': 'uuid',
        'required': True
    },
    {
        'f': 'name',
        't': 'title',
        'type': 'text',
        'max_length': 80,
        'required': True
    },
    {
        'f': None,
        't': 'product-url',
        'type': 'url',
        'max_length': None,
        'required': True
    },
    {
        'f': 'price',
        't': 'price',
        'type': 'number',
        'required': True
    },
    {
        'f': 'stock',
        't': 'availability',
        'type': 'check_stock',
        'required': True
    },
    {
        'f': 'shipping',
        't': 'deliver-cost',
        'type': 'check_shipping',
        'required': True
    },
    {
        'f': 'brand',
        't': 'brand',
        'type': 'text',
        'max_length': None
    },
    {
        'f': 'description',
        't': 'description',
        'type': 'text',
        'max_length': 300
    },
    {
        'f': 'images',
        't': 'image-url',
        'type': 'image_array'
    },
    {
        'f': 'id_category',
        't': 'merchant-category',
        'type': 'category_array'
    },
    {
        'f': 'sku',
        't': 'sku',
        'type': 'text',
        'max-length': None
    },
    {
        'f': None,
        't': 'currency',
        'type': 'currency'
    }
]


# TODO: create custom validator for custom product
"""
FASHION:
    fashion-type
    fashion-gender
    fashion-size
    color
"""
