#!/usr/bin/env python
"""
    vp21.py -- Definition of Epson VP21 Protocol.

    This file is a part of pyVP21, a Python interface to the Epson VP21
    command protocol.

    This file defines a projector class 

    Copyright (C) 2012
    Vehicle Systems & Control Laboratory
    Texas A&M University
"""
import datetime
import logging
import serial
import sys
import time
import vp21


# Set up logging.
logging.basicConfig(
    filename = '.projector-%s.log' % (datetime.date.today().isoformat()),
    format = '%(levelname)-10s %(asctime)s %(message)s',
    level = logging.DEBUG
)
log = logging.getLogger(__name__)

# Define constants for serial communication.
BUF = 1024 # Buffer for receiving data from serial.
CMD_FAILURE = 1 # Indicates a command failed communication or was rejected.
CMD_SUCCESS = 0 # Indicates successfule issuing of command.

# Define default parameters for serial connection.
BAUD_RATE = 9600 # VP21 uses a 9600 bps serial connection.
HEARTBEAT_PERIOD = 20 # Period between heartbeat checks.
TIMEOUT = 10 # Timeout for serial communication.


class Projector(object):
    """Projector -- Python interface to Epson projector.
        Interfaces with an Epson projector over a serial connection.
    """
    def __init__(self,
                 port=None, 
                 baud=BAUD_RATE,
                 timeout=TIMEOUT,
                 heartbeatPeriod=HEARTBEAT_PERIOD):
        """Constructor for the Projector class.
            Creates a projector object 
        """
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.heartbeatPeriod = heartbeatPeriod
        # Create the serial object.
        self.ser = serial.Serial()
        self.ser.baudrate = self.baud
        self.ser.port = port
        self.ser.timeout = self.timeout
        if self.port is not None:
            try:
                self.ser.open()
            except serial.SerialException:
                log.error('Could not open serial port %s.' % self.port)

    def send(self, message):
        """Sends the specified message to the projector object."""
        if self.ser.isOpen():
            self.ser.write(serial.to_bytes(message) + vp21.NULL)
            bytes = self.ser.read(BUF)
            if bytes == vp21.NULL:
                return CMD_SUCCESS
            else:
                return CMD_FAILURE
                log.warning('Command \"%s\" rejected.')
        else:
            return CMD_FAILURE

    def sendHeartbeat(self):
        """Sends null command to projector to see if alive."""
        if self.ser.isOpen():
            self.ser.write(vp21.NULL)
            bytes = self.ser.read(BUF)
            if bytes == vp21.NULL:
                return CMD_SUCCESS
            else:
                return CMD_FAILURE
                log.warning('Hearbeat failed.')

