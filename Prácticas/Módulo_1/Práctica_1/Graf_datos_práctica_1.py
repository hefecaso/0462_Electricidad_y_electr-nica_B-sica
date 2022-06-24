#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Editor de Spyder

@author: Héctor Fernando Carrera Soto
"""

import pandas as pd
from matplotlib import pyplot as plt

#Extrayendo datos

xls = pd.ExcelFile('Datos_práctica_1.xltx')
df1 = xls.parse('carga_del_capacitor')

'''
Tenías que gráficar la carga y descarga del capacito
pero ya alguien lo hizo por accidente, así que ya no lo hiciste

Ánimo!!!! sigue adelante, tu puedes yo del futuro.
'''