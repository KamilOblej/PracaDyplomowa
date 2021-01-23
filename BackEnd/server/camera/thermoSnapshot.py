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

    cv2.imwrite(path + file_name + format, np.uint8(a)) 
    thermo = Thermo()
    thermo.name = file_name
    thermo.image = file_name + format
    thermo.save()
