## What is Azure Virtual Network ?

- Azure Virtual Network is a service that provides the fundamental block for creating your private network on azure.
- It enables the azure resources to securely communicate with each other, to internet and to on-premises.
- It's similar to you own private network on data center.

## why virtual network ?

- Communication b/w azure resources.
- Communication to internet, on-prem.
- Filtering of network traffic.
- Routing of network traffic.

_Note_

_To move a virtual machine from one virtual network to another, you must delete and recreate the virtual machine in the new virtual network. The virtual machine's disks can be retained for use in the new virtual machine._

## Availabilty Zone of Virtual Network

- Azure Vnets and subnets span across all availability zones.
- This means when you're creating a Vnet you no need to divide it into multiple zones.
- When deploying zonal resources like VMs, you select the desired zone during configuration, and the VNet/subnet will seamlessly support it.
- Azure Vnets can span across the zones but not regions.

## Costing

Virtual Network in Azure is free of charge. Every subscription can create up to 50 Virtual Networks across all regions. VNET Peering links two virtual networks – either in the same region, or in different regions - and enables you to route traffic between them using private IP addresses (carry a nominal charge). Inbound and outbound traffic is charged at both ends of the peered networks. Network appliances such as VPN Gateway and Application Gateway that are run inside a virtual network are also charged.

## Communication with on-prem resources

### Point-to-site VPN:

Established between your azure network and single computer in client network. Each computer that wants to connect with virtual network must configure this connection. This is usefull if you're just getting started with azure or for developers because it come's with less changes or no changes.

### Site-to-Site VPN:

- This can be used for cross-premises or hybrid configurations.
- This connection requires a VPN device located on-premises with public IP attacjed to it.
- Virtual Network Gateway can be configured by using active-standby mode with single public IP or with active-active mode by two public IPs.
- In active-standby mode one tunnel is always active and another is standby. The traffic will flow through the active tunnel and if there is any issue in this tunnel, the traffic switches over to the standby tunnel.
- Setting up VPN Gateway in active-active mode is recommended in which both the IPsec tunnels are simultaneously active, with data flowing through both tunnels at the same time.
- Each Virtual Network can have only on VPN gateway, but we can make multiple connections to on-premises env's.
- This type of connection is sometimes referred to as a "multi-site" connection.

### Express Route

Established between your network and Azure, through an ExpressRoute partner. This connection is private. Traffic doesn't go over the internet.

## What is a subnet ?

A subnet is a range of IP addresses in a Virtual Network. You can divide a Vnet into multiple subnets for security and organisation.
