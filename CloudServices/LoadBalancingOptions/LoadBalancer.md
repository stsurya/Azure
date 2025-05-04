## Azure Load balancer

Azure Load Balancer operates at layer 4 of the Open Systems Interconnection (OSI) model. It's the single point of contact for clients. Load balancer distributes inbound flows that arrive at the load balancer's front end to backend pool instances.

These flows are according to configured load-balancing rules and health probes. The backend pool instances can be Azure Virtual Machines or instances in a Virtual Machine Scale Set.

- Basic load balancer have no charge and no SLA.
- Standard load balancer tier is Regional or Global.
- The backend pools of Global load balancer should be the standard regional load balancers.

### FrontEnd IP Configuration

- The IP address of your Azure Load Balancer. It's the point of contact for clients. These IP addresses can be either:
  i) Public IP Address.
  ii) Private IP Address.
  The nature of the IP address determines the type of load balancer created. Private IP address selection creates an internal load balancer. Public IP address selection creates a public load balancer.

- Unlike external load balancers that use public IP addresses, internal load balancers use private IP addresses.The private IP must belong to a specific subnet within the VNet.The internal load balancer will route traffic within the network using this IP address.
- You can choose between a static or dynamic IP address. Static IP addresses are recommended for scenarios where consistent IP addresses are needed, like for DNS resolution or application configurations.

### Health Probes

A health probe is used to determine the health status of the instances in the backend pool. During load balancer creation, configure a health probe for the load balancer to use. This health probe determines if an instance is healthy and can receive traffic.

### Load Balancer rules

A load balancer rule is used to define how incoming traffic is distributed to all the instances within the backend pool. A load-balancing rule maps a given frontend IP configuration and port to multiple backend IP addresses and ports. Load Balancer rules are for inbound traffic only.

### Inbound NAT rules

An inbound NAT rule forwards incoming traffic sent to frontend IP address and port combination. The traffic is sent to a specific virtual machine or instance in the backend pool. Port forwarding is done by the same hash-based distribution as load balancing.

### Limitations

- Load balancer provides load balancing and port forwarding for specific TCP or UDP protocols.
- Load-balancing rules and inbound NAT rules support TCP and UDP, but not other IP protocols including ICMP.
- Load Balancer backend pool can't consist of a Private Endpoint.
- Outbound flow from a backend VM to a frontend of an internal Load Balancer will fail.
- A load balancer rule can't span two virtual networks. All load balancer frontends and their backend instances must be in a single virtual network.
- Forwarding IP fragments isn't supported on load-balancing rules. IP fragmentation of UDP and TCP packets isn't supported on load-balancing rules.
- You can only have one Public Load Balancer (NIC based) and one internal Load Balancer (NIC based) per availability set. However, this constraint doesn't apply to IP-based load balancers.
- LoadBalancers cannot distribute traffic among the backend pools which are in different regions until and unless your tier is gloabl instead of region.
