#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.

import matplotlib.pylab as plt
import array


class Henon(object):

    def __init__(self):
        global ntransient, nplot
        ntransient = 1000
        nplot = 10000

    def assignment(self, module):
        self.x0 = float(module.entry[0].get())
        self.y0 = float(module.entry[1].get())
        self.a = float(module.entry[2].get())
        self.b = float(module.entry[3].get())

    def func(self, x_i, y_i):
        return y_i + 1.0 - self.a * x_i ** 2, self.b * x_i

    def calc(self):
        global x, y
        x = array.array('d')
        y = array.array('d')
        x.append(self.x0)
        y.append(self.y0)
        for n in range(ntransient + nplot):
            x.append(self.func(x[n], y[n])[0])
            y.append(self.func(x[n], y[n])[1])
        return (x[ntransient:ntransient + nplot], y[ntransient:ntransient + nplot])

    def plot_x_and_y(self, x, y, color='blue', showing=True):
        self.margin = 0.1
        plt.scatter(x, y, s=1.0, marker='o', color=color,
                    label=r'$x_{0}=$' + str(self.x0) + ' : '
                    + r'$y_{0}=$' + str(self.y0) + ' : '
                    + r'$a=$' + str(self.a) + ' : '
                    + r'$b=$' + str(self.b)
                    )
        plt.gca().set_xlim(min(x) - self.margin, max(x) + self.margin)
        plt.gca().set_ylim(min(y) - self.margin, max(y) + self.margin)
        plt.xlabel(r'$x$', fontsize=16)
        plt.ylabel(r'$y$', fontsize=16)
        plt.title(r"$\mathrm{H\'{e}non\ map}$")
        plt.legend(loc="best")
        if showing:
            plt.show()
        else:
            pass
