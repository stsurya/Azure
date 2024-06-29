## Network Security Group in Azure

- Azure NSG is used to filter out the traffic to and from azure resources in the Vnet.
- NSG will consist of inbound or outbound rules which will allow or deny the traffic.
- You an define the rule by giving 5 tuples Source, source port, Destination, Destination port, protocol.
- You associate a nsg on subnet or NIC(incase of VM), one NSG can be associated with multiple subnets.

## What is Network Virtual Appliance (NVA) ?

- A network virtual appliance is a VM that performs network function, such as a firewall or WAN optimization.

## difference between ASG and NSG ?

- ASGs are applied to a group of VMs with same tags. ASGs are applied to VMs and are used in conjunction with NSGs.
- ASGs simplify the manner of applying security rules by grouping VMs that belong to same application tier.
