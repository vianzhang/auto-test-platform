#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""

from flask import render_template, flash, redirect, url_for, Blueprint, request


main_bp = Blueprint('main', __name__)


@main_bp.route('/home', methods=['GET'])
def home():
    return render_template('main/index.html')


@main_bp.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.home'))