# Networking Fundamentals

## IP address:

An Internet Protocol(IP) address is the unique indentifying number assigned to every device connected to an internet. An IP address definition is a numeric label assigned devices that use the internet to communicate.

Ip address haves two different versions IPv4 and IPv6. There are different types of IP addresses like static IP, Dynamic IP, Public IP, Private IP. The full range of IP address in 0.0.0.0 to 255.255.255.255.

## CIDR

https://cidr.xyz/

- CIDR stands for Classless Inter-Domain Routing. It is an IP address assigning method that improves the efficiency of ip address distribution.
- By using CIDR IP address many unique IP addresses can be designated. CIDR IP address is same as normal IP address except that it ends with slash followed by a number.

  172.200.0.0/16 --> four block --> each - block 8bits...The block size must be of power 2 and equal to the total number of IP addresses.

## What are ports ?

ports are standardized across all network-connected devices, with each port assigned a number. IP address are used to transfer messages to and from devices, where as port numbers aloow targetting applications on those devices.

Sure! In computer networking, a port is a communication endpoint that processes and exchanges data between different applications or services. Think of it as a door through which data can enter or leave a device. Ports are identified by unique numbers, ranging from 0 to 65535.

**Here's an example to illustrate:**

Let's say you have a computer (Computer A) that hosts a web server, and another computer (Computer B) wants to access a webpage hosted on that server. When Computer B sends a request to Computer A for the webpage, it specifies a destination port number in the request. In this case, the destination port number is typically port 80 for HTTP (Hypertext Transfer Protocol) traffic, which is the standard port for web servers.

Computer A, upon receiving the request, checks the destination port number. Since it's port 80, it knows that the request is for the web server. The web server software running on Computer A listens for incoming requests on port 80. It processes the request, retrieves the requested webpage, and sends it back to Computer B.
