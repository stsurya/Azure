## What is Azure Route Sever ?

Azure Route Server simplifies dynamic routing between your network virtual appliance (NVA) and your Azure virtual network. It allows you to exchange routing information directly through Border Gateway Protocol (BGP) routing protocol between any NVA that supports the BGP routing protocol and the Azure Software Defined Network (SDN) in the virtual network without the need to manually configure or maintain route tables. Azure Route Server is a fully managed service and is configured with high availability.

## How does it work ?

The following diagram illustrates how Azure Route Server works with an SDWAN NVA and a security NVA in a virtual network. Once you establish the BGP peering, Azure Route Server receives an on-premises route (10.250.0.0/16) from the SDWAN appliance and a default route (0.0.0.0/0) from the firewall. These routes are then automatically configured on the VMs in the virtual network. As a result, all traffic destined to the on-premises network is sent to the SDWAN appliance, while all internet-bound traffic is sent to the firewall. In the opposite direction, Azure Route Server sends the virtual network address (10.1.0.0/16) to both NVAs. The SDWAN appliance can propagate it further to the on-premises network.

![Image Missing](./Images/route-server-overview.png)
