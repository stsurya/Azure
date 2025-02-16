## VPN Gateway

VPNs typically are deployed to connect two or more trusted private networks to one another over an untrusted network such as the internet. Traffic is encrypted while traveling over the untrusted network to prevent a third-party from eavesdropping on the network communication.

When you're planning a VPN gateway, there are three architectures to consider:

- Point to site over the internet.
- Site to site over the internet.
- Site to site over a dedicated network, such as Azure ExpressRoute.

## Gateway Subnet in Azure

A Gateway Subnet is required for VPN Gateways in Azure. It contains the IP addresses that the Virtual Network Gateway VMs and services use.

**Key Points:**

- The subnet must be named GatewaySubnet.
- This subnet is only for the Virtual Network Gateway—no other resources should be deployed here.
- When creating a VPN Gateway, Azure automatically deploys gateway VMs in this subnet.
- The subnet size determines how many IP addresses are available for the gateway.
  - Minimum size: /29
  - Recommended size: /27 (to allow future scaling or ExpressRoute coexistence).
