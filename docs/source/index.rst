.. CHAM9000 documentation master file, created by
   sphinx-quickstart on Sun Jan 13 19:35:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
====================================

The CHAM9000 is a self contained open source home monitoring and automation 
system.  The core feature of the CHAM9000 is its ability to monitor a garage 
door and not only display the status of that door on a web page, but can send 
the owner an email if the door is left open for a predefined time period.

The CHAM9000 has the ability to monitor and control nearly anything.  Currently,
there is support for sensing the "Presence" of things, log/report temperatures, 
communicate with a Radiothermostat_.

The CHAM9000 is currently limited to monitoring a few different types of
sensors.  However, the current state is only a jumping stone for what it is 
really capable of.  Future revisions will have documented APIs that will allow
third party developers to develop there own modules to plug in any type of
sensor.  There will also be support for the CHAM9000 to initiate calls to remote
nodes.  Currently the CHAM9000 only accepts connections, and this severly limits
its ability to operate in a full fledged home automation system.

Getting Started
========================
The following links will provide some help in setting up your system as well 
as describe the CHAM9000 as a whole.

* :doc:`initial_setup`
* :doc:`architecture`
* :doc:`cham_protocol`





Hardware Requirements
============================
Basic hardware requirements to wirelessly monitor a garage door:

* Two nRF24L01P_ radios.  Something like `these 
<https://www.amazon.com/dp/B004U984UK/?tag=cham9000-20>`_ should work fine.
* A RaspberryPi_
* An `Arduino <https://www.amazon.com/dp/B006H06TVG/?tag=cham9000-20>`_
* A `magnetic door switch <https://www.amazon.com/dp/B0009SUF08/?tag=cham9000-20>`_
* Two strands of wire long enough to reach from your RaspberryPi_ to the
    garage door.
* Power supplies and power cables for the RaspberryPi and Arduino.


        


Index
==========
.. toctree::
   :maxdepth: 2
   
   initial_setup
   architecture
   cham_protocol

.. _Radiothermostat: http://www.radiothermostat.com/
.. _RaspberryPi: http://www.raspberrypi.org/
.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P

