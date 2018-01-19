# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, 2017 Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from __future__ import division
from ht import *
import numpy as np
from numpy.testing import assert_allclose
from ht.core import is_heating_temperature, is_heating_property

def test_core():
    dT = LMTD(100., 60., 30., 40.2)
    assert_allclose(dT, 43.200409294131525)
    dT = LMTD(100., 60., 30., 40.2, counterflow=False)
    assert_allclose(dT, 39.75251118049003)


def test_is_heating_temperature():
    assert is_heating_temperature(T=200, T_wall=500)
    
    assert not is_heating_temperature(T=400, T_wall=200)
    
    # not heating when 400 K
    assert not is_heating_temperature(T=400, T_wall=400)
    
    
def test_is_heating_property():
    T1, T2 = 280, 330
#    C1, C2 = Chemical('hexane', T=T1), Chemical('hexane', T=T2)
#    mu1, mu2 = C1.mu, C2.mu
#    Pr1, Pr2 = C1.Pr, C2.Pr
    mu1, mu2 = 0.0003595695325135477, 0.0002210964201834834
    Pr1, Pr2 = 6.2859707150337805, 4.810661011475006
    
    assert is_heating_property(prop=mu1, prop_wall=mu2)
    assert is_heating_property(prop=Pr1, prop_wall=Pr2)
    
    # Equal temperatures - not heating in that case
    T1, T2 = 280, 280
    mu1, mu2 = 0.0003595695325135477, 0.0003595695325135477
    Pr1, Pr2 = 6.2859707150337805, 6.2859707150337805
    assert not is_heating_property(prop=mu1, prop_wall=mu2)
    assert not is_heating_property(prop=Pr1, prop_wall=Pr2)
    
    # Lower wall temperatures - not heating in that case
    T1, T2 = 280, 260
    mu1, mu2 = 0.0003595695325135477, 0.0004531397378208441
    Pr1, Pr2 = 6.2859707150337805, 7.27333944072039
    assert not is_heating_property(prop=mu1, prop_wall=mu2)
    assert not is_heating_property(prop=Pr1, prop_wall=Pr2)
