# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 04:21:30 2017

@author: Wordsmith
"""

import os

def load_data(path):
    """
    Load dataset
    """
    input_file = os.path.join(path)
    with open(input_file, "r", encoding='utf-8') as f:
        data = f.read()

    return data.split('\n')
