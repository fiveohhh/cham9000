.. _architecture:

CHAM9000 Architecture
========================

.. contents::







Architectural Goals
-------------------
Because the CHAM9000 has the ability to span multiple platforms, careful
consideration is given to determine an efficient and cohesive way to send
messages between the central server and any other sensor nodes.


Requirements
------------

Functional
""""""""""

 #. Shall allow for the addition of atleast 255 nodes
 #. All nodes shall communicate with the central server over HTTP or through a 
    wireless gateway
 #. The wireless gateway shall use Nordic Semiconductor 2.4GHz radios.

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
    the webserver and the wireless gateway that independent ``Paws`` can connect 
    to.

2. Paws
    Paws are  devices that report data  to the Cham.  Each Paw can implment 
    multiple interfaces.  For example, a Paw can implement a temperature and a 
    door interface.  It can therefore report both temperature and door status 
    information back to the Cham.

.. uml::

    [Cham] -left-> [paw 2] 
    [Cham] -down-> [paw 4]
    [Cham] -up-> [paw 1] 
    [Cham] -right-> [paw 3] 
    
Hardware
--------
At the core of the CHAM9000 sits a RaspberryPi_ Model B.  The Raspberry Pi will
host all services that the Cham requires.  Initially this will be a webserver
and various scripts that help the Cham perform its duties.  

The RaspberryPi_ will also connect to a Nordic nRF24L01P_ radio via SPI.  This
radio will perform the wireless gateway functionality of the Cham.

Individual Paws will have not be tied to any specific hardware.  all that will
be required of a Paw to connect to the Cham will be either an Ethernet
connection or a nRF24L01P_ radio.

.. _RaspberryPi: http://www.raspberrypi.org/
.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P

Security concerns
-----------------

Architecture of the Cham
------------------------
Interface
""""""""""
All communications with the Cham will be over HTTP with what is essentially
a RESTful interface.  However, there will only be a single write-only resource.
This interface will implement the native :ref:`cham_protocol`.
Third party applications will also have the ability to query data from the Cham
using read-only REST interfaces. This data could include temperature or current
status of a door.

Architecture of the Paws
------------------------
Paws are currently one-way devices.  A Paw can either be an embedded device with
a wireless radio, or any type of device with the ability to make HTTP requests.
Each Paw  will be required to implement a 

Interface
"""""""""
All Paws will communicate with the Cham using the native :ref:`cham_protocol`.
They will need to implement all methods in the Paw discovery mechanism as well
as implement the interfaces they declare during Paw discovery.

Paw discovery mechanism
"""""""""""""""""""""""
.. uml::
    title Discovery over wireless gateway\n with unconfigured Paw 
    
    actor User
    participant Paw
    participant Cham
    Paw -> Cham : getChamAddr()
    note right
        look for an available  
        Cham on discovery channel
    end note
    Paw <-- Cham
    note right
        Cham will respond to 
        discover request with its 
        private address
    end note
    Paw -> Cham : reportCluster()
    note right
        The Paw reports its interfaces
        to the Cham.
    end note
    User ->Cham : AuthorizePaw()
    note right
        The user authorizes the device
        through the Chams webinterface
    end note
    Cham -> Paw : sendEncryptionKey()    
    
    
Glossary
-------------

================  ======================================================
Term              Definition
================  ======================================================
CHAM9000          A home automation and monitoring system

Cham              The central server component of the CHAM9000 system

Paw               A remote node that reports information to the Cham

Wireless gateway  The portion of the system that allows wireless devices to 
                  communicate with the central server
================  ======================================================