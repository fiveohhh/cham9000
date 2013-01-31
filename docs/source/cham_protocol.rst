.. _cham_message_types::

CHAM9000 Message Types
============================
There are multiple messaging types natively supported by the CHAM9000.  However,
you are not limited to these messages types, as adding a new message type is as 
simple as adding a function to the views.py file.

.. warning::
    These are initial protocol versions and will likely be changed as the current
    use of fixed width messages is limiting.  Future versions of the protocol will
    likely use messages with a delimiter to separate fields.

* *DOR* - The DOR message type is used to nreport the status of a door(open or 
    close).  The message contains both the number of the door as well as the 
    status of the door.
    Example::
    
        DOR120
        
    In the above example, door #12 is reportin that it is closed (0).
    
* *PRS* - The PRS message type is used to determine when something enters or 
    leaves a location.
    Example::
    
        PRS99881
        
    This message states that the item 99 arrived(1) at location 88.
    
* *TMP* - The TMP message type is used for reporting temperatures.  The 
    temperatures are transmitted in degrees K*100.  This allow for two decimal
    points of precision while not having to deal with floating point numbers
    Example::
    
        TMP9912345
        
    In this message, sensor 99 is reporting a temperature of 123.45 degrees 
    Kelvin.
    