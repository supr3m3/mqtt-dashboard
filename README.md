---
title: 'MQTT-Dashboard: Solar Energy Acquisition'
---

MQTT Dashboard: Solar Energy Acquisition
===
###### tags: `MQTT`, `Node.js`, `Socket.io` 

This project uses MQTT protocol to stream live energy data. The objective of this project is to present the real-time with a Dashboard developed with Node.js, Socket.io, and MQTT.

The client publishing the data is located in a remote area and communicates via Modbus RTU. A Modbus gateway ([MGate 3170](https://www.moxa.com/en/products/industrial-edge-connectivity/protocol-gateways/modbus-tcp-gateways/mgate-mb3170-mb3270-series)) is being used to convert the serial data to TCP data so that the data is accessible thorugh the internet.

[UC-8112](https://www.moxa.com/en/products/industrial-computing/arm-based-computers/uc-8100-series/uc-8112-lx) is set up to acquire the Modbus data. This gateway is responsible of converting the Modbus data into JSON data. Once converted, the JSON data is published to the MQTT broker for clients to subscribe. For more details, click [here](https://guide.iiot.party/).

## Table of Contents

[TOC]

What is MQTT?
---
MQTT is a protocol that you will run across if you are working in IoT and it is basically a featherweight pubisher-subcriber messaging protocol specifically design for the Internet of Things.

Publisher-subscriber messaging is a way for clients to talk to each other without having to know each other’s addresses and port numbers. To subscribe to a specific data, all you need to know is the IP address of the MQTT broker and topic of the data.

To acquire the MQTT data from the broker for Node.js, `mqtt` npm library is needed. There are many options for a MQTT broker, such as `broker.hivemq.com` and `iot.eclipse.org`. 

![](https://i.imgur.com/PROXLVg.png)


Modbus Data
---
The data we are going to publish to the MQTT broker will be coming from a power meter. This meter communicates through Modbus RTU, a serial level protocol. Modbus is communication protocol that commonly used to establish client/server communication in industrial and energy-management application. More details on Modbus can be found [here](http://www.modbus.org/).

Dashboard
---
To present real-time data on a dashboard, Socket.io is used to maintain an open connection between the server (Node.js) and the browser. This enables the server to push updates to the browsers. Without Socket.io, data will not change on the brwoser unless you refresh the page. 

To display the proper data, JSON data to HTML is made possible with jQuery.

Requirements
---
> Debian
```
$ sudo apt-get install nodejs
```
> macOS
```
$ brew install nodejs
```

Installation
---

```gherkin=
$ git clone https://github.com/supr3m3/mqtt-dashboard
$ npm install
```

## Network Toplogy
![](https://i.imgur.com/JFWZNxz.png)

## Credits
> Icons made by [Freepik](https://www.freepik.com/) from [flaticon](https://flaticon) is licensed by [CC 3.0 BY](https://creativecommons.org/).
> [Condrint](https://github.com/condrint) for jQuery assistance.



