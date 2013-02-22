.. _initial_setup:

Initial Install and Setup
=============================

So you have your RaspberryPi in hand and are ready to start building your garage
door monitor.  Following the steps on this page will get your RaspberryPi setup
so that it can talk with the wireless radios.

#.  Download the latest Raspbian image from http://www.raspberrypi.org/downloads.  
    I've used `Win32DiskImager <https://launchpad.net/win32-image-writer>`_ to 
    successfully write the image to an SD card on both Windows 7 and 8.

#.  Once the the Pi is running, we want to expand the root partion, this can be done
    by running the raspi-config tool::

        $sudo raspi-config

    This will present a GUI, select expand_rootfs.  Once this is done, reboot the Pi.  
    The partition will be expanded when the Pi boots up, It took about 3 minutes on my
    16GB SD card.

#.  Next we will want to install and run Hexxeh's rpi-update tool.  Running the tool 
    will take ~5 minutes::
    
        $sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && sudo chmod +x /usr/bin/rpi-update
        $sudo rpi-update

#.  In order for the update to take, we need to reboot once again

#.  Now we install and setup permissions for the SPI device. This involves removing the 
    spi module from the blacklist.  To do this uncomment the following line::
    
        #blacklist spi-bcm2708
        
    from the ``/etc/modprobe.d/raspi-blacklist.conf`` file.   
    
    Then add the following line to the ``/etc/modules`` file::
    
        spidev
    
    The last step for setting up SPI involves changing some permissions, so we can use SPI
    without being root.  To do this run the following lines::
        
        $sudo groupadd -f --system spi
        $sudo adduser pi spi
        
        
    Finally, as root (sudo) create a file called ``90-spi.rules`` in the ``/etc/udev/rules.d/``
    directory with the following contents.::
    
        SUBSYSTEM=="spidev", GROUP="spi"
        
#.  In order for the new permissions to take, we need to reboot.

#.  Install python3 setuptools::
    
        $sudo apt-get install python3-setuptools
        
#.  Install gpio-admin by running the following in the root of the source directory::
    
        $make
        $sudo make install
        
#.  Install quick2wire::

        $git clone https://github.com/quick2wire/quick2wire-python-api.git
        $cd quick2wire-python-api
        $sudo python3 setup.py install
        
