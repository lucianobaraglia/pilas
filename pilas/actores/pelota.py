# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor
import pilas
import pymunk

class Pelota(Actor):
    "Representa una pelota de Volley."

    def __init__(self, x=0, y=0):
        imagen = pilas.imagenes.cargar('pelota.png')
        Actor.__init__(self, imagen)
        self.rotacion = 0
        self.x = x
        self.y = y
        self.radio_de_colision = 25
        self.figura = pilas.fisica.fisica.crear_figura_circulo(x, y, self.radio_de_colision)

    def actualizar(self):
        self.definir_posicion(self.figura.body.position.x, self.figura.body.position.y)
        self.rotacion = self.figura.body.angle * 500
