.. CHAM9000 documentation master file, created by
   sphinx-quickstart on Sun Jan 13 19:35:08 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
====================================

The CHAM9000 was initially designed to monitor and report temperatures.  It has 
since taken on the roll of monitoring garage doors and the "Presence" of things. 
The core system runs on a RaspberryPi_.  Requires an SD card that is atleast 4GB.

The wireless portion of the system uses the Nordic nRF24L01P_ radio.

.. _RaspberryPi: http://www.raspberrypi.org/
.. _nRF24L01P: http://www.nordicsemi.com/eng/Products/2.4GHz-RF/nRF24L01P
 
 

Initial Install and Setup
=============================
Only the RaspberryPi is required for these intitial setup steps

1.  Download the latest Raspbian image from http://www.raspberrypi.org/downloads.  
    I've used `Win32DiskImager <https://launchpad.net/win32-image-writer>`_ to 
    successfully write the image to an SD card on both Windows 7 and 8.

2.  Once the the Pi is running, we want to expand the root partion, this can be done
    by running the raspi-config tool::

        pi@raspberrypi ~ $sudo raspi-config

    This will present a GUI, select expand_rootfs.  Once this is done, reboot the Pi.  
    The partition will be expanded when the Pi boots up, It took about 3 minutes on my
    16GB SD card.

3.  Next we will want to install and run Hexxeh's rpi-update tool.  Running the tool 
    will take ~5 minutes::
    
        pi@raspberrypi ~ $sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update
        pi@raspberrypi ~ $sudo rpi-update

4.  In order for the update to take, we need to reboot once again

5.  Now we install and setup permissions for the SPI device. This involves removing the 
    spi module from the blacklist.  To do this uncomment the ``#blacklist spi-bcm2708`` line
    from the ``/etc/modprobe.d/raspi-blacklist.conf`` file.   Then add ``spidev`` to the 
    ``/etc/modules`` file
    
    The last step for setting up SPI involves changing some permissions, so we can use SPI
    without being root.  To do this run the following lines::
        
        pi@raspberrypi ~ $sudo groupadd -f --systemspi
        pi@raspberrypi ~ $sudo adduser pi spi
        
    Finally, as root (sudo) create a file called ``90-spi.rules`` in the ``/etc/udev/rules.d/``
    directory with the following contents.::
    
        SUBSYSTEM=="spidev", GROUP="spi"
        
4.  In order for the new permissions to take, we need to reboot.

5.  Install python3 setuptools::
    
        pi@raspberrypi ~ $sudo apt-get install python3-setuptools
        
6.  Install gpio-admin::
    
        pi@raspberrypi ~ $git clone https://github.com/quick2wire/quick2wire-gpio-admin
        pi@raspberrypi ~ $cd quick2wire-gpio-admin
        pi@raspberrypi ~ $sudo python3 setup.py install
        
7.  Install quick2wire::

        pi@raspberrypi ~ $git clone https://github.com/quick2wire/quick2wire-python-api.git
        pi@raspberrypi ~ $cd quick2wire-python-api
        pi@raspberrypi ~ $sudo python3 setup.py install
        
        
.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

