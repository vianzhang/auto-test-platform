#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""

from flask import render_template, flash, redirect, url_for, Blueprint, request


api_bp = Blueprint('api', __name__)


@api_bp.route('/api-list', methods=['GET'])
def api_list():
    return render_template('api/api-list.html')


@api_bp.route('/add-api', methods=['GET'])
def add_api():
    return render_template('api/add-api.html')
