import numpy as np 
import math
import pandas as pd
from uncertainties import ufloat
from uncertainties import unumpy as unp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

b = 50e-3
l = ufloat(633.52e-9, 1.86e-9 )
z = 24
T = 293.15
T0 = 273.15
p = 1
p0 = 1.0132
p1 = 0.4

dn = z * l / (2 * b)
print(dn)
print(z/(b *2) * l.s)

n = 1 + dn * T/T0 * p0/(p-p1)
print(n)

print(T/T0 * p0/(p- p1) * dn.s)