# -*- coding: utf-8 -*-
import os
import urllib.request

from clint.textui import puts, colored


class FileManager:
    def get_file_content(self, file, **kwargs):
        data = None
        if 'verbose' in kwargs and kwargs['verbose']:
            puts(colored.yellow("Opening file: {}".format(file)))

        with open(file, 'r') as fo:
            data = fo.read()
            puts(colored.green("Success"))

        if data is None:
            puts(colored.red("Fail"))

        return data

    def get_url_content(self, url, **kwargs):
        data = None

        if 'verbose' in kwargs and kwargs['verbose']:
            puts(colored.yellow("Opening url: {}".format(url)))

        with urllib.request.urlopen(url) as u:
            data = u.read().decode('utf-8')
            puts(colored.green("Success"))

        if data is None:
            puts(colored.red("Fail"))

        return data

    def save_in_file(self, content, path=None, filename='kelkoo_autogen.xml', **kwargs):
        if path is None:
            os.chdir(os.path.dirname(__file__))
            path = os.getcwd() + '/../'

        file = path + filename
        return_flag = False

        try:
            fo = open(file, 'wb+', )
            fo.write(content)
            return_flag = file
        except:
            puts(colored.red("Can't open file: {}".format(file)))
            raise FileNotFoundError()
        finally:
            fo.close()

        return return_flag
