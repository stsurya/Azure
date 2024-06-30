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
- ASGs are used within a NSG to apply a network security rule to a specific workload or group of VMs — defined by ASG worked as being the “network object” & explicit IP addresses are added to this object.
- Another great use of this is for scalability, creating the virtual machine and assigning the newly created virtual machine to its ASG will provide it with all the NSG rules in place for that specific ASG — zero distribution to your service!

## What is an NIC ?

- It's a component which will connect the VM or any other service to the Virtual Network. It'll enable the communication b/w the VM and other azure resources.
- A network interface (NIC) enables an Azure virtual machine (VM) to communicate with internet, Azure, and on-premises resources.
