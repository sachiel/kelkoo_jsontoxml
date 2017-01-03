# -*- coding: utf-8 -*-


def validate_uuid(content=None):
    return 'magiuuid'


def validate_text(content, max_length=None):
    # TODO: Sanitize content
    return content


def validate_url(content):
    return 'http://www.ejemplo.com'


def validate_number(content):
    #TODO: validate number
    return content


def validate_image_array(obj):
    image_url = 'https://www.placecage.com/c/1024/768'

    if len(obj) > 1:
        image_url = obj[0]['urlimage']

    return image_url


def validate_category_array(obj):
    category = ''

    if 'name' in obj:
        category = obj['name']

    return category


def validate_check_stock(content):
    status_available = 1
    status_request = 4

    number = int(content)

    if number > 1:
        return status_available
    else:
        return status_request


def validate_check_shipping(obj):
    shipping = ''
    if 'text' in obj:
        shipping = obj['text']

    return shipping


def validate_currency(content):
    return 'MXN'

