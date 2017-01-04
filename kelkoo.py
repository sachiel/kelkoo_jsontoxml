#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from clint.textui import colored, puts
from clint.arguments import Args

from validators.url import url as isvalid_url

from kelkoo.services import ParseJSON


def main():
    all_args = Args().grouped

    path = None

    if '-path' in all_args:
        path = all_args['-path'].all[0]

    if '-url' in all_args and '-file' in all_args:
        puts(colored.red("Use -url or -file params, not both"))

    if '-url' in all_args:
        if len(all_args['-url'].all) < 1:
            puts(colored.red("-url param can't be blank"))
        else:
            url_raw = all_args['-url'].all[0]

            if isvalid_url(url_raw):
                # init process
                ParseJSON(url=url_raw, verbose=True, path=path)
            else:
                puts(colored.red("-url must be a valid url. Ex: http://www.madkting.com"))

    elif '-file' in all_args:
        if len(all_args['-file'].all) < 1:
            puts(colored.red("-file param can't be blank"))
        else:
            file_raw = all_args['-file'].all[0]
            # TODO: validate if file exist
            # init process
            ParseJSON(file=file_raw, verbose=True, path=path)
    else:
        puts(colored.yellow("Using default json"))
        file = os.getcwd() + '/assets/products_kelkoo.json'
        # pj.get_file_content(file)
        ParseJSON(file=file, verbose=True, path=path)

main()

