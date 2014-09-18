#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.

import SetParameter as sp
import Henon


def clicked():
    henon.assignment(module=window)
    window.quit()
    henon.plot_x_and_y(henon.calc()[0], henon.calc()[1], color='black')

if __name__ == '__main__':
    parameters = [{'x0': 0.0}, {'y0': 0.0}, {'a': 1.4}, {'b': 0.3}]
    window = sp.SetParameter()
    henon = Henon.Henon()
    window.show_setting_window(parameters, {'OK': clicked})
