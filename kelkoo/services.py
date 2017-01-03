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

            if not self.json  or '' == self.json :
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
                    # TODO: validation for product

                    products_str += product.decode('utf-8')

                    sleep(0.1)
                    bar.show(bar_counter)
                    bar_counter += 1
        else:
            for obj in self.master_dict:
                product = self.process_item(obj)
                # TODO: validation for product
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
        # iterate object and validate fields
        return dicttoxml(obj, root=False, attr_type=False, cdata=True)

    def validate(self, obj):
        pass

    def validate_field(self, field):
        pass


