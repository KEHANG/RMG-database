#!/usr/bin/env python
# encoding: utf-8

name = "Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Dummy Root""",
    longDesc = 
u"""

""",
    rank = 10,
)

tree(
"""
L1: Ring
"""
)

