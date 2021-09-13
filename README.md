# RGB Text Fan Controller
This repository contains scripts to control a RGB text fan attached to a Raspberry Pi.

# Setup

The Raspberry Pi and RGB text fan need to be wired as followed:

IMAGE

The following dependencies need to be installed:

```
sudo apt-get install libusb-1.0-0.dev
sudo pip3 install git+https://github.com/LukePrior/microwave_usb_fan
sudo pip3 install Flask
```

The script can be run with:

```
sudo python3 main.py"
```

The website can then be accessed from the Pi's local IP on port 80.

You can find the complete installation and setup guide in the Diyode Magazine article.

# DIYODE Magazine Article

[COMING SOON](https://diyodemag.com)

# License

This project is licensed under the MIT License. This project contains code from the [Micro Wave USB Fan](https://github.com/fergofrog/microwave_usb_fan) repository.
