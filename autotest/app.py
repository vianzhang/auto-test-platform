#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    :author: WENHAO ZHANG
"""
from autotest.manager import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)