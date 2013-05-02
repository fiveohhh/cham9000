.. _architecture:

CHAM9000 Architecture
========================

.. contents::


.. _glossary: 
   
Glossary
--------

================  ======================================================
Term              Definition
================  ======================================================
CHAM9000          A home automation and monitoring system

Cham              The central server component of the CHAM9000 system

Paw               A remote node that reports information to the Cham

Wireless gateway  The portion of the system that allows wireless devices to 
                  communicate with the central server

Yip               The abilities that a paw can implement.  For example,
                  a paw that is monitoring two temperature sensors and a 
                  door sensor would implement two temperature yips and a 
                  single door yip.
================  ======================================================




Architectural Goals
-------------------
Because the CHAM9000 has the ability to span multiple platforms, careful
consideration is given to determine an efficient and cohesive way to send
messages between the central server and any other sensor nodes.

Careful consideration is also given to extensibility.  The Cham is to be
designed as a home monitoring solution.  There will be some core functionality
that will allow out of the box operations, but most of the functionality
will be provided through the implementation of plugins.  Therefor, a key 
element of the architecture will be the ease of plugin development.

Requirements
------------

Functional
""""""""""

 #. Shall allow for the addition of atleast 255 nodes
 #. All nodes shall communicate with the central server over HTTP or through a 
    wireless gateway
 #. The wireless gateway shall only communicate with the Cham over HTTP
 #. The wireless gateway shall use Nordic Semiconductor 2.4GHz radios.
 #. Shall run on a RaspberryPi Model B

Non-functional
""""""""""""""
 #. Shall cost less then $100 for all components required to monitor a garage 
    door
 #. Shall allow a user to add remote nodes without having to flash firmware


Constraints
-----------
One possible constraint will be the physical limitation of the packet buffer in
the wireless radios.  Each packet can be a maximum of 32 bytes.  Currently
all Cham messages are of a fixed known length and do not require larger packets.
This is a constraint that could be eliminated by packet assembly/segmentation
done in software.

Hardware
--------
At the core of the CHAM9000 sits a RaspberryPi_ Model B.  The Raspberry Pi will
host all services that the Cham requires.  Initially this will be a webserver
and various scripts that help the Cham perform its duties.  

The RaspberryPi_ will also connect to a Nordic nRF24L01P_ radio via SPI.  This
radio will perform the wireless gateway functionality of the Cham.

Individual Paws will have not be tied to any specific hardware.  All that will
be required for a Paw to connect to the Cham will be either an Ethernet
connection or a nRF24L01P_ radio.

.. _RaspberryPi: http://www.raspberrypi.org/
.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P

Architectural Priciples
-----------------------

Top-level Components
--------------------
There are two types of logical components in the CHAM9000 system.  

1. The Cham
    Each system will have one and only one server component known as the Cham.  
    This component is hosted on the raspberryPi.  It's main sub-components are
    the webserver and the wireless gateway that independent ``Paws`` can 
    connect to.

2. Paws
    Paws are devices that report data to the Cham.  Each Paw can implement 
    multiple yips.  For example, a Paw can implement a temperature 
    and a door yip.  It can therefore report both temperature and door status 
    information back to the Cham.
    
Top-level Component view
------------------------
The below diagram shows a high-level view of the two ways that a paw can connect
to the Cham.

.. uml::

    [Cham] -- HTTP
    HTTP - [wireless_gateway]
    [wireless_gateway] -- RF
    
    package "Wireless Paws" {
    Nordic_Radio -- [Paw 1]
    Nordic_Radio - [Paw 2]
    Nordic_Radio -- RF
    }
    package "TCP/IP Paws" {
    network_connection -- [Paw 3]
    network_connection - [Paw 4]
    HTTP - network_connection
    }


Security concerns
-----------------

Architecture of the Cham
------------------------
The core sub-components of the Cham are Django web app and a small suite of
scripts and executables that will assist the Cham in monitoring activities.

Interface
""""""""""
All communications with the Cham will be over HTTP with what is essentially
a RESTful interface.  However, there will only be a single write-only resource.
This interface will implement the native :ref:`cham_protocol`.

Third party applications will also have the ability to query data from the Cham
using read-only REST interfaces. This data could include temperature or current
status of a door.

The REST resources that will be available to third parties will be
implementation dependent.  All REST resources will be controlled through the
TastyPie_ Django Application.

Django Apps
"""""""""""
The Chams web interface will be made up of two Django applications.  One
application will be "head-less" and will provide the REST interfaces into the
Chams database.  Theses interfaces will include the APIs for third party 
applications querying the Cham, as well as accepting valid Cham messages.  The 
second application will be responsible the presentation layer and will be
responsible for presenting information to the user.

Typically machines will be interacting with the Rest Interface and users will
interact with the presentation layer.

Both of these application will operate on the same database.  Below is a diagram
of this type of architecture.

.. uml::
    cloud {
    [Users]
    [Machines]
    }

    package "Django Apps" {
    [Rest Interface]
    [Presentation Layer]
    }
    database "sqlite3" {
    [historical data]
    }
    
    
    [Users] -> [Presentation Layer]
    [Machines] -> [Rest Interface]
    [Rest Interface] -- [historical data]
    [Presentation Layer] -- [historical data]

An alternative option would have been for the Presentation Layer to interact 
with the Rest Interface, rather then directly with the database.  This would 
provide an "eat your own dog food" type of architecture.  A large benefit to
this architecture would be the innate testing of the API's.

.. uml::
    cloud {
    [Users]
    [Machines]
    }

    package "Django Apps" {
    [Rest Interface]
    [Presentation Layer]
    }
    database "sqlite3" {
    [historical data]
    }
    
    
    [Users] -> [Presentation Layer]
    [Machines] -> [Rest Interface]
    [Rest Interface] -- [historical data]
    [Presentation Layer] -- [Rest Interface]

Both models are still on the table and further research needs to done to
determine the model that will be used.

The wireless gateway 
""""""""""""""""""""
The wireless gateway will not do any message translating or routing.  It simply
takes what it hears on the RF side and passes it along on the HTTP side.
Currrently data only flows from the RF to the HTTP side of the gateway, but 
implementing two-way wireless messaging is at the top of the list of 
enhancements.

.. uml::
    [Wireless Paw]
    package "Raspberry Pi" {
    [Rest Interface]
    [Wireless Gateway]
    }
    database "sqlite3" {
    [historical data]
    }
    
    [Wireless Paw] --> [Wireless Gateway]
    [Wireless Gateway] -> [Rest Interface]
    [Rest Interface] -- [historical data]
    


.. _TastyPie: http://tastypieapi.org/

Architecture of the Paws
------------------------
The architecture that the Paws implement is completely up to the author of the
Paw.  Therefore, no assumptions will be made about their actually architecture,
however, they will be required to implement the appropriate interfaces.

Paws are currently one-way devices.  A Paw can either be an embedded device with
a nRF24L01P_ radio, or any type of device with the ability to make HTTP 
requests. Each paw will be required to implement at least one yip. The paw must 
notify the Cham of the yips it implements during the Paw discovery time.

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
    Paw -> Cham : reportYips()
    note right
        The Paw reports its yips
        to the Cham.
    end note
    User ->Cham : AuthorizePaw()
    note right
        The user authorizes the device
        through the Chams webinterface
    end note
    Cham -> Paw : sendEncryptionKey()    
    
Components of The Cham9000
--------------------------
This section will describe the architecture of the components within the 
Cham9000.  This includes the wireless gateway, the helper scripts, as well as 
the web application.

The Wireless Gateway
""""""""""""""""""""
First we discuss the design of the wireless gateway.  This will consist of a 
single process that runs as a daemon on the server. It will be written in 
Python and process incoming data from the radio and pass it to the Cham over
HTTP.  This current design only has the ability to receive messages from the
radio.

The gateway will listen for messages on two different addresses.  The first
address will be a "discovery address" and for all Cham systems will be:
0xCAM030303.  This address will be the one that a Paw will advertise itself on
and allow a Cham the opportunity to associate itself with.  The second address 
will be user defined in the config file and is the private address for an 
individual system.  It's best to choose a random address that utilizes the full
32bits of the address range.

The wireless gateway will utilize the quick2wire library that will allow it to
control the GPIO and SPI hardware blocks on the raspberryPi.  To do this some 
knowledge of the Nordic radio is required.

TODO: summary of nordic IO.

Helper Scripts
""""""""""""""
There are two types of helper scripts, time series scripts, and non-time series
scripts.  These could also be thought of as synchronous and asynchronous sripts.

Time Series Scripts
^^^^^^^^^^^^^^^^^^^
These are operations that run at regular intervals.  This is accomplished using
cron.  One limitation of cron is that nothing can run faster than every minute.
The following is an example a time series helper script:

    The Radio Thermostat CM30 has an http interface, but there is no way to 
    program the thermostat so that it will tell the Cham9000 its current 
    setpoint.  To get around this limitiation, a helper script was written that
    runs every 15 minutes and retrieves the temperature from the thermostat.  
    The helper script then relays this temperature onto the CHAM9000.  

Non-time Series Scripts
^^^^^^^^^^^^^^^^^^^^^^^
These are scripts thar aren't run at regular intervals.  They can either run at
boot or be triggered by an interrupt.  The following is an example of a non-time
series script:

    The wireless gateway utilizes the a radio that notifies data is ready by
    raising a GPIO.  In order to retrieve the data from the radio, a script is 
    triggered whenever the GPIO is raised.  This script retrieves the data from
    the radio and exits..


The Cham
""""""""
The Cham can be considered the heart of the system.  This is where all device
data passes through. 