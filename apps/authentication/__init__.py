# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint', #nome do Blueprint, que será usado para identificá-lo dentro do aplicativo Flask.
    __name__, #nome do módulo atual
    url_prefix='' #as rotas definidas neste Blueprint não terão um prefixo adicional na URL.
)
