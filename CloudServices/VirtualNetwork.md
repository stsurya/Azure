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

**VNet Limit per Subscription:**

Each Azure subscription can create up to 50 VNets across all regions combined. This means that if you have one subscription, you can create a total of 50 VNets, not 50 per region but 50 in total across all the regions where you deploy resources.
Example:

If you create 20 VNets in the East US region and 15 VNets in the West Europe region, you can only create 15 more VNets in any other regions because your total limit is 50.
