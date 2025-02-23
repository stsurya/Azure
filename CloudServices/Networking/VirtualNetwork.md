## What is Azure Virtual Network ?

- Azure Virtual Network is a service that provides the fundamental block for creating your private network on azure.
- It enables the azure resources to securely communicate with each other, to internet and to on-premises.
- It's similar to you own private network on data center.
- Virtual Network is a regional service. It spans across the availbilty zones but not across regions or subscriptions.

## why virtual network ?

- Communication b/w azure resources.
- Communication to internet, on-prem.
- Filtering of network traffic.
- Routing of network traffic.

## RFC 1918

When you are creating a VNet, use address ranges enumerated in RFC 1918. These addresses are for private, nonroutable address spaces.

10.0.0.0 - 10.255.255.255 (10/8 prefix)
172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
In addition, you can't add the following address ranges.

224.0.0.0/4 (Multicast)
255.255.255.255/32 (Broadcast)
127.0.0.0/8 (Loopback)
169.254.0.0/16 (Link-local)
168.63.129.16/32 (Internal DNS)
Azure assigns resources in a virtual network a private IP address from the address space that you provision. For example, if you deploy a VM in a VNet with subnet address space 192.168.1.0/24, the VM is assigned a private IP like 192.168.1.4. Azure reserves the first four and last IP address for a total of five IP addresses within each subnet. These addresses are x.x.x.0-x.x.x.3 and the last address of the subnet.

For example, the IP address range of 192.168.1.0/24 has the following reserved addresses:

192.168.1.0
192.168.1.1 (Reserved by Azure for the default gateway.)
192.168.1.2, 192.168.1.3 (Reserved by Azure to map the Azure DNS IPs to the VNet space.)
192.168.1.255 (Network broadcast address.)

## What is RFC 1918?

RFC 1918 (Request for Comments 1918) is a standard defined by the Internet Engineering Task Force (IETF) that specifies private IP address ranges for use in internal networks. These addresses are not routable on the public internet and are meant for private use within organizations, data centers, and cloud environments.

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

- A subnet with '/29' is always the smallest subnet.s
- subnets spana across avaialbilty zones.
