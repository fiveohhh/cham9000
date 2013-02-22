.. _architecture:

CHAM9000 Architecture
========================

.. contents::

Because the CHAM9000 has the ability to span multiple platforms, careful
consideration was given to determine an efficient and uniform way to send
messages between the central server and any other sensor nodes.


At the core of the CHAM900sits a RaspberryPi_ Model B.  This acts as both the
wireless gateway as well as the webserver.

The wireless portion of the system uses the Nordic nRF24L01P_ radio.

.. _Radiothermostat: http://www.radiothermostat.com/
.. _RaspberryPi: http://www.raspberrypi.org/

.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P



Architectural Goals
-------------------

Requirements
------------

Functional
""""""""""

 #. Shall allow for the addition of atleast 255 nodes
 #. All nodes shall communicate with the central server over HTTP or through a 
    wireless gateway

Non-functional
""""""""""""""
 #. Shall cost less then $100 for all components required to monitor a garage 
    door
 #. Shall allow a user to add remote nodes without having to flash firmware

Goals
-----

Constraints
-----------

Architectural Priciples
-----------------------

Top-level Components
--------------------
There are two types of logical components in the CHAM9000 system.  

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
    
Security concerns
-----------------

Paw discovery mechanism
-----------------------
    
    
Architecture of the Cham
------------------------

Architecture of the Paws
------------------------

    
    
    
Glossary
-------------

===========     ======================================================
Term            Definition
===========     ======================================================
CHAM9000        A home automation and monitoring system
Cham            The central server component of the CHAM9000 system
Paw             A remote node that reports information to the Cham
===========     ======================================================