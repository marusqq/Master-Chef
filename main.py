#!env/bin python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''controller script'''

from BarcodeReader import BarcodeReader

reader = BarcodeReader()
reader.start()