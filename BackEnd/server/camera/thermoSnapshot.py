import numpy as np
import cv2
from pylepton import Lepton
from datetime import datetime, date
from time import sleep
import copy

from . models import Thermo


def thermo(path, file_name, format):

    with Lepton() as l:
        a, _ = l.capture()

    cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)  # extend contrast
    np.right_shift(a, 8, a)  # fit data into 8 bits

    # scale_percent = 200  # percent of original size
    # width = int(a.shape[1] * scale_percent / 100)
    # height = int(a.shape[0] * scale_percent / 100)
    # dim = (width, height)
    # resized = cv2.resize(a, dim, interpolation=cv2.INTER_AREA)
    # a = copy.copy(resized)

    cv2.imwrite(path + file_name + format, np.uint8(a))  # write it!
    thermo = Thermo()
    thermo.name = file_name
    thermo.image = file_name + format
    thermo.save()
    print(thermo)

    print('Thermo taken at' + thermo.date_taken)
