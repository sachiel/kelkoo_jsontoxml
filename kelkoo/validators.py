# -*- coding: utf-8 -*-
import uuid

"""
All validators return a dict
"""


def validate_uuid(content=None, **kwargs):
    """
    This logic is a demo, the uuid must be obtained of the API of madkting
    :param content:
    :param kwargs:
    :return:
    """
    if 't' not in kwargs:
        return {}

    if content is None:
        # generate a UUID
        return {
            kwargs['t']: str(uuid.uuid1())[0:16]
        }
    else:
        return {
            kwargs['t']: content
        }


def validate_text(content, **kwargs):
    if 't' not in kwargs:
        return {}

    if 'max_length' in kwargs and kwargs['max_length']:
        max_length = int(kwargs['max_length'])
        split_content = content[1:max_length]
        return {
            kwargs['t']: split_content
        }
    else:
        return {
            kwargs['t']: content
        }


def validate_url(content, **kwargs):
    """
    Always return same URL, this param must be send in API
    :param content:
    :param kwargs:
    :return:
    """
    if 't' not in kwargs:
        return {}

    return {
        kwargs['t']: 'http://www.ejemplo.com'
    }


def validate_number(content, **kwargs):
    if 't' not in kwargs:
        return {}

    # TODO: validate if content has only numbers

    return {
        kwargs['t']: float(content)
    }


def validate_image_array(obj, **kwargs):
    if 't' not in kwargs:
        return {}

    # Default image
    image_url = 'https://www.placecage.com/c/1024/768'
    images_dict = {}

    if len(obj) > 1:
        counter = 1
        for image in obj:
            if counter > 4:
                continue

            if counter == 1 and 'urlimage' in image and image['urlimage'] != '':
                images_dict['image-url'] = image['urlimage']
            elif 'urlimage' in image and image['urlimage'] != '':
                images_dict['image-url' + str(counter)] = image['urlimage']

            counter += 1
    else:
        images_dict = {
            'image-url': image_url
        }

    return images_dict


def validate_category_array(obj, **kwargs):
    if 't' not in kwargs:
        return {}

    category_dict = {}

    if 'name' in obj:
        category_dict[kwargs['t']] = obj['name']

    return category_dict


def validate_check_stock(content, **kwargs):
    if 't' not in kwargs:
        return {}

    status_available = 1
    status_request = 4
    stock_dict = {}

    number = int(content)

    if number > 1:
        stock_dict[kwargs['t']] = status_available
    else:
        stock_dict[kwargs['t']] = status_request

    return stock_dict


def validate_check_shipping(obj, **kwargs):
    if 't' not in kwargs:
        return {}

    shipping_dict = {}

    value = 0

    if obj['text'] != 'Gratis':
        value = float(obj['text'])

    if 'text' in obj:
        shipping_dict[kwargs['t']] = value

    return shipping_dict


def validate_currency(content, **kwargs):
    if 't' not in kwargs:
        return {}

    currency_dict = {
        kwargs['t']: 'MXN'
    }

    return currency_dict



