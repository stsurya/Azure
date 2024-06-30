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

## Azure Private link

Azure private link is a set of services designed to establish secure connections to various services in Azure.
It consists of two services

1. Private EndPoint.
2. Private Link Service.

### Private Endpoint

- When you activate a private endpoint on storage account which is not belonging to the Vnet, it receives a NIC, with a complete private IP address from the selected Virtual Network. Consequently, resources already residing within the same VNET or connected to it (by means of VNET peering, VPN, ExpressRoute etc.) gain the capability to securely access the Storage Account solely through this private IP address

- When you create a private endpoint configure DNS zone correctly to resolve the private endpoint IP address to the fully qualified domain name (FQDN) of the connection string

- Existing Microsoft Azure services might already have a DNS configuration for a public endpoint. This configuration must be overridden to connect using your private endpoint.Existing Microsoft Azure services might already have a DNS configuration for a public endpoint. This configuration must be overridden to connect using your private endpoint.

![Image is not accessible](./Images/PrivateEndpoint.webp)

### Private Link Service

This is useful when two different azure services are in two different Vnets and Vnet peering is not possible due to some issues like Ip address conflicts or other securtiy considerations.
Esentially, it enables you to create a private endpoint for a resource in VnetA for a service hosted in VnetB and made accessible thorugh a standard load balancer.
In essence, the Private Link Service helps allocate a private IP (Private Endpoint) within VNET B for a service that is hosted in VNET A. This configuration enables the services within VNET B to securely establish connections with the service hosted in VNET A using a private IP.

![Image is not accessible](./Images/PrivateLink.webp)

### Service endpoints

They enable a resource within an Azure VNET to establish a more secure and direct connection to another Azure resource, such as a Storage Account.
For example, if a Virtual Machine in a VNET needs to connect to a storage account, only the Virtual Machine will have an internal IP within the VNET.
The storage account itself won’t possess an internal IP in the VNET but will instead be mapped to the same VNET, allowing the Virtual Machine to take a more direct route while still utilizing the public IP of the storage account but without leaving the Azure backbone or traversing the public internet.

![Image is not accessible](./Images/ServiceEndPoint.webp)

## difference between ASG and NSG ?

- ASGs are applied to a group of VMs with same tags. ASGs are applied to VMs and are used in conjunction with NSGs.
- ASGs simplify the manner of applying security rules by grouping VMs that belong to same application tier.