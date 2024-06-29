## Route Tables

- A route table contains a set of rules, called routes, those routes specify how the packet should be routed in Virtual Network. Route tables are associated with subnets, we define routes by giving destination, it can be a IP address, virtual applicance, virtual network Gateway or internet. If nothing is found the packet can be dropped.

There are two types of route tables
i) System routes.
ii) User-Defined routes.

**i) System routes**

- Whenever you create a VM in Vnet, it can communicate it to internet or other VM's in same Vnet automatically. This is because of System routes.
- System routes control the flow of communication in the following scenarios:
  i) From within the subnet.
  ii) From a subnet to another subnet in same VM.
  iii) From VM's to internet.
  iv) From Vnet to another Vnet with Vnet peering.
  v) from vnet to another vnet through Vnet gateway.

**ii) User-Defined Routes**

- Whenever you create a user-defined route table you can associate it with the subnet. Remember user-defined route tables can only be used while the traffic is leaving the subnet, not when traffic is coming into subnet.
- User-defined routes will override the system routes.
- In most of the cases system routes are sufficient, but in if you want to user virtual appliances like azure firewall, you need to create user-defined routes.
- In the rotue you need to mention the next hop and destination.
