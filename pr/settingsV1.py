# -*- coding: utf-8 -*-
import numpy as np
# -------------------------------------------------------------------------------------------------
# Globale Einstellungen für die physikalische Simulation für Versuchsstand 1
# -------------------------------------------------------------------------------------------------
Ku = 2.46597e-05            # m**3 / (s V) - Verstärkung der Pumpe
uA0 = 6.4                   # V - Spannung ab welcher die Pumpe Wasser fördert über pywisp bestimmt
uA0Voltmeter = 6.4          # V - Spannung ab welcher die Pumpe Wasser fördert mit multimeter bestimmt

rT1 = 0.060195545420039     # m - effektiver Radius des Tank 1
rT2 = 0.060195545420039     # m - effektiver Radius des Tank 2
g = 9.81                    # m / s^2 - Erdbeschleunigung
hV1 = 0.055                 # m - Höhe zwischen Nullniveau und Ventil
hV2 = 0.055                 # m - Höhe zwischen Nullniveau und Ventil

AT1 = np.pi * rT1 ** 2      # m**2 - Tankquerschnitt 1
AT2 = np.pi * rT2 ** 2      # m**2 - Tankquerschnitt 2
AS1 = 4.639266e-05          # m**2 - Abflussquerschnitt von Tank 1 - Ventil 12 ist 2 geschlossen
AS2 = 3.302590e-05          # m**2 - Abflussquerschnitt von Tank 2 - Ventil 21 ist 2.25 geschlossen

aus = 0.029739776           # m / V - Skalierung Ultraschallsensor
bus = -0.056215613          # m - Offset Ultraschallsensor

hT1 = 0.3                   # m - Höhe Tank 1
hT2 = 0.3                   # m - Höhe Tank 2

scale = 2                   # Skalierung für die Visualisierung

initial_state = [0, 0]

is_analog = 0
