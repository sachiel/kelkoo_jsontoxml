# -*- coding: utf-8 -*-

MAIN_FIELDS = [
    {
        'f': None,  # From JSON
        't': 'offer-id',  # To XML
        'type': 'uuid'
    },
    {
        'f': 'name',
        't': 'title',
        'type': 'text',
        'max_length': 80
    },
    {
        'f': None,
        't': 'product-url',
        'type': 'url',
        'max_length': None
    },
    {
        'f': 'price',
        't': 'price',
        'type': 'number'
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
        'f': 'stock',
        't': 'availability',
        'type': 'check_stock'
    },
    {
        'f': 'shipping',
        't': 'deliver-cost',
        'type': 'check_shipping'
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
