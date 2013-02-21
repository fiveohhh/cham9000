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


Components
-------------
There are two types of logical componenets in the CHAM9000 system.  

1. The Cham
    Each system will have one and only one server component known as the Cham.  
    This component is hosted on the raspberryPi.  It's main sub-components are
    the webserver and the wireless gateway that external ``Paws`` can connect 
    to.

2. Paws
    Paws are remote devices that report data back to the Cham.  Each Paw can
    implment multiple interfaces.  For example, a Paw can implement a
    temperature and a door interface.  It can therefore report both temperature 
    and door status information back to the Cham.

.. uml::

    [Cham] -left-> [paw 2] 
    [Cham] -down-> [paw 4]
    [Cham] -up-> [paw 1] 
    [Cham] -right-> [paw 3] 
    