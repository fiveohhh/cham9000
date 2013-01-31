.. architecture::
Architecture
================
Because the CHAM9000 has the ability to span multiple platforms, careful
consideration was given to determine an efficient and uniform way to send
messages between the central server and any other sensor nodes.


At the core of the CHAM900sits a RaspberryPi_ Model B.  This acts as both the
wireless gateway as well as the webserver.

The wireless portion of the system uses the Nordic nRF24L01P_ radio.

.. _Radiothermostat: http://www.radiothermostat.com/
.. _RaspberryPi: http://www.raspberrypi.org/

.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P