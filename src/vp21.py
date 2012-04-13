#!/usr/bin/env python
"""
    vp21.py -- Definition of Epson VP21 Protocol.

    This file is a part of pyVP21, a Python interface to the Epson VP21
    command protocol.

    This file defines a VP21 instruction subset for the PowerLite Home Cinema
    8350 projector. For a complete description of the VP21 protocol for use in
    adding support for other projector models, see "ESC/VP21 Command User’s 
    Guide for Home Projectors", available at: 
    http://files.support.epson.com/pdf/pltw1_/pltw1_cm.pdf

    Copyright (C) 2012
    Vehicle Systems & Control Laboratory
    Texas A&M University
"""
import sys

# Null command.
NULL = b'\x0d'

# Power commands.
PWR_ON = 'PWR ON'
PWR_OFF = 'PWR OFF'

# Input 1/A commands.
SRC1_CYCLE = 'SOURCE 10'
SRC1_YCBCR = 'SOURCE 14'
SRC1_YPBPR = 'SOURCE 15'
SRC1_AUTO = 'SOURCE 1F'

# Input 2/B commands.
SRC2_CYCLE = 'SOURCE 20'
SRC2_ANALOG_RGB = 'SOURCE 21'

# Input 3 commands.
SRC3_CYCLE = 'SOURCE 30'

# VIDEO Commands.
HDMI2 = 'SOURCE A0'
VIDEO_CYCLE = 'SOURCE 40'
VIDEO_RCA = 'SOURCE 41'
VIDEO_S = 'SOURCE 42'


if __name__ == '__main__':
    sys.stderr.write('Module <%s> cannot be run as script.\n' % __name__)
    sys.exit()

