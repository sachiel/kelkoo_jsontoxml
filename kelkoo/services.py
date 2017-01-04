# -*- coding: utf-8 -*-
import json
from dicttoxml import dicttoxml

from .file import FileManager
from .parsefields import MAIN_FIELDS
from .validators import *

from clint.textui import colored, puts
from clint.textui import progress

from time import sleep


class ParseJSON(FileManager):
    master_json = None
    master_dict = None

    def __init__(self, **kwargs):
        if 'file' in kwargs and kwargs['file'] != '':
            self.json = self.get_file_content(**kwargs)

            if not self.json or '' == self.json :
                raise ValueError("File content is blank")

            self.master_dict = json.loads(self.json)
        elif 'url' in kwargs and kwargs['url'] != '':
            self.json = self.get_url_content(**kwargs)

            if not self.json or '' == self.json :
                raise ValueError("URL content is blank")

            self.master_dict = json.loads(self.json)
        else:
            raise AttributeError("Must set a file or url in param")

        # trigger parse process
        self.parse(**kwargs)

    def parse(self, **kwargs):
        num_items = len(self.master_dict)
        verbose = False
        products_str = ''

        if 'verbose' in kwargs and kwargs['verbose']:
            verbose = True

        if verbose:
            puts(colored.red("Parsing {} Products".format(num_items)))

        if verbose:
            with progress.Bar(label="Parsing", expected_size=num_items) as bar:
                bar_counter = 1
                for obj in self.master_dict:
                    product = self.process_item(obj)

                    if product:
                        products_str += product.decode('utf-8')

                    bar.show(bar_counter)
                    bar_counter += 1
        else:
            for obj in self.master_dict:
                product = self.process_item(obj)
                if product:
                    products_str += product.decode('utf-8')

        # not the best way to do this but YOLO
        xml_gen = '<?xml version="1.0" encoding="UTF-8" ?><products>{}</products>'.format(products_str)
        xml_gen = xml_gen.encode('utf-8')

        save_xml = self.save_in_file(xml_gen, **kwargs)
        if save_xml:
            puts(colored.green("Success XML Saving in: {}".format(save_xml)))
        else:
            puts(colored.red("Script Miserably Fails. Shame!, shame!, shame!"))

    def process_item(self, obj):
        if not self.validate(obj):
            return False

        # Assemble XML Object
        return_obj = {}

        for field in MAIN_FIELDS:
            validate_function = globals()["validate_" + field['type']]
            validate_result = None

            if field['f'] is None:
                validate_result = validate_function(None, **field)
                if validate_result:
                    return_obj.update(validate_result)
                else:
                    continue  # avoid next condition

            if field['f'] in obj:
                validate_result = validate_function(obj[field['f']], **field)
                if validate_result:
                    return_obj.update(validate_result)

        return_obj = {
            'product': return_obj
        }

        return dicttoxml(return_obj, root=False, attr_type=False, cdata=True)

    def validate(self, obj):
        """
        Verify if obj has required fields defined in kelkoo.parsefields.MAIN_FIELDS
        """
        is_valid = True

        # Only check if obj has the required fields
        for field in MAIN_FIELDS:
            if 'required' in field and field['required']:
                if field['f'] is None:
                    continue

                if field['f'] not in obj:
                    is_valid = False

        return is_valid
