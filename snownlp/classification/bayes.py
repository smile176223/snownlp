# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from math import log, exp

from ..utils.frequency import AddOneProb


class Bayes(object):

    def __init__(self):
        self.d = {}
        self.total = 0

    def train(self, data):
        for d in data:
            c = d[1]
            if c not in self.d:
                self.d[c] = AddOneProb()
                for word in d[0]:
                    self.d[c].add(word, 1)
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))

    def classify(self, x):
        tmp = {}
        for k in self.d:
            tmp[k] = 0
            for word in x:
                tmp[k] += log(self.d[k].getsum()) - log(self.total)\
                    + log(self.d[k].freq(word))
        ret, prob = 0, 0
        for k in self.d:
            now = 0
            for otherk in self.d:
                now += exp(tmp[otherk]-tmp[k])
            now = 1/now
            if now > prob:
                ret, prob = k, now
        return (ret, prob)
