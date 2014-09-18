#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.

import SetParameter as sp
import Henon

delta_x0 = 0.0000001
delta_y0 = -0.00001


def clicked():
    henon.assignment(module=window)
    window.quit()

    # --- 1つ目のエノン写像の描画 ---
    henon.plot_x_and_y(henon.calc()[0], henon.calc()[1],
                       color='red', showing=False
                       )

    # --- 近傍点の設定 ---
    henon.x0 = henon.x0 + delta_x0
    henon.y0 = henon.y0 + delta_y0

    # --- 2つ目のエノン写像の描画 ---
    henon.plot_x_and_y(henon.calc()[0], henon.calc()[1],
                       color='blue', showing=True
                       )

if __name__ == '__main__':

    parameters = [{'x0': 0.0}, {'y0': 0.0}, {'a': 1.4}, {'b': 0.3}]
    window = sp.SetParameter()
    henon = Henon.Henon()
    window.show_setting_window(parameters, {'OK': clicked})  # パラメータの設定
