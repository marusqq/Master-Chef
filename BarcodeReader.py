#!env/bin python3
# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"
'''Barcode reading class'''

import cv2
from pyzbar import pyzbar

class BarcodeReader:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def start(self):
        
        while True:
            ret, frame = self.camera.read()

            #check for barcodes  
            frame = self._read_barcode(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame', gray)
            
            # turn off with q
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    def _read_barcode(self, frame):
        barcodes = pyzbar.decode(frame)
        if barcodes:
            for barcode in barcodes:
                x, y, w, h = barcode.rect
                barcode_info = barcode.data.decode('utf-8')
                print(barcode_info)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)  

                with open("barcode_result.txt", mode ='w') as file:
                    file.write("Recognized Barcode:" + barcode_info)    
            
        return frame


    