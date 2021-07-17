# Grow Lab

## Setup
1. Install the [Raspberry Pi Imager](https://www.raspberrypi.org/software/).
    Windows
    ```
    scoop install raspberry-pi-imager
    ```
2. Plug in MicroSD card.
3. Click 'CHOOSE OS' and select the Raspberry Pi OS Desktop.
4. Click 'CHOOSE STORAGE' and select the MicroSD drive that was plugged in.
5. Click 'WRITE'.
6. Open the MicroSD drive in Explorer and create a empty directory called `ssh` in the `boot` drive.
7. Eject the MicroSD.
8. Insert the MicroSD into the Raspberry Pi and turn the power on.
9. After a minute or so, try to connect to the Raspberry Pi using SSH.
    ```
    ssh pi@raspberrypi
    ```
    > The default password is `raspberry`.
10. Update the system packages.
    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```
11. Install `smbus` module used for I2C sensors.
    ```
    sudo apt-get install python3-smbus

    ```
12. Configure the Raspberry Pi.
    ```
    sudo raspi-config
    ```
    1. Set a new password under _System Options > Password_.
    2. Enable the I2C interface under _Interface Options > I2C_.
13. Reboot the Raspberry Pi.
    ```
    sudo reboot
    ```
14. Install VS Code.
    Windows
    ```
    scoop install vscode
    ```
15. Install the Remote - SSH extension.
16. Connect to the Raspberry Pi using SSH extension.

## Resources
- [RPi.GPIO API](https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api)
