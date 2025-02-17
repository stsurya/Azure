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

## High availability options for VPN connections

To provide better availability for your VPN connections, there are a few options available:

- VPN Gateway redundancy (Active-standby).
- Multiple on-premises VPN devices.
- Active-active Azure VPN gateway.
- Combination of both.

## VPN Gateway redundancy

Azure VPN gateway has two instances (active-standby). During maintenance or failures, the standby takes over automatically.

**Downtime:**

- **Planned:** 10–15 sec
- **Unplanned:** 1–3 min  
  P2S connections are disconnected, and users must reconnect.

![Image Missing](./Images/vpn-active-standby-587ca913.png)

## Multiple on-premises VPN devices

This configuration provides multiple active tunnels from the same Azure VPN gateway to your on-premises devices in the same location. There are some requirements and constraints:

- You need to create multiple S2S VPN connections from your VPN devices to Azure. When you connect multiple VPN devices from the same on-premises network to Azure, you need to create one local network gateway for each VPN device, and one connection from your Azure VPN gateway to each local network gateway.
- The local network gateways corresponding to your VPN devices must have unique public IP addresses in the GatewayIpAddress property.
- BGP is required for this configuration. Each local network gateway representing a VPN device must have a unique BGP peer IP address specified in the BgpPeerIpAddress property.
- You should use BGP to advertise the same prefixes of the same on-premises network prefixes to your Azure VPN gateway, and the traffic is forwarded through these tunnels simultaneously.
- You must use Equal-cost multi-path routing (ECMP).
- Each connection is counted against the maximum number of tunnels for your Azure VPN gateway, 10 for Basic and Standard SKUs, and 30 for HighPerformance SKU.

In this configuration, the Azure VPN gateway is still in active-standby mode, so the same failover behavior and brief interruption occurs. But this setup guards against failures or interruptions on your on-premises network and VPN devices.

![Image Missing](./Images/vpn-multiple-onprem-vpns-61d52189.png)

## Active-active VPN gateways

- Each Azure VPN gateway instance has a **unique public IP** and establishes an **IPsec/IKE S2S VPN tunnel** to the on-premises VPN device.
- **Two tunnels** exist simultaneously, ensuring high availability.
- Traffic from Azure to on-premises is **routed through both tunnels**, though the on-premises VPN may prefer one.
- For **single TCP/UDP flows**, Azure tries to use the same tunnel, but the on-premises network may use different ones.
- During **planned maintenance or failure**, one tunnel disconnects, and the VPN device automatically removes or updates routes to switch traffic to the active tunnel.
- **Failover is automatic** on the Azure side, ensuring minimal disruption.

![Image Missing](./Images/vpn-active-active-89241ba7.png)

## Dual-redundancy: active-active VPN gateways for both Azure and on-premises networks

Here you create and set up the Azure VPN gateway in an active-active configuration and create two local network gateways and two connections for your two on-premises VPN devices. The result is a full mesh connectivity of 4 IPsec tunnels between your Azure virtual network and your on-premises network.

All gateways and tunnels are active from the Azure side, so the traffic is spread among all four tunnels simultaneously. By spreading the traffic, you may see slightly better throughput over the IPsec tunnels, the primary goal of this configuration is for high availability. And due to the statistical nature of the spreading, it's difficult to provide the measurement on how different application traffic conditions affects the aggregate throughput.

This topology requires two local network gateways and two connections to support the pair of on-premises VPN devices, and BGP is required to allow the two connections to the same on-premises network.

![Image Missing](./Images/vpn-dual-redundancy-567620af.png)

## Highly Available VNet-to-VNet

The same active-active configuration can also apply to Azure VNet-to-VNet connections. You can create active-active VPN gateways for both virtual networks, and connect them together to form the same full mesh connectivity of four tunnels between the two VNets.

Even though the same topology for cross-premises connectivity requires two connections, the VNet-to-VNet topology only needs one connection for each gateway. Additionally, BGP is optional unless transit routing over the VNet-to-VNet connection is required.

![Image Missing](./Images/vpn-vnet-vnet-92bddb64.png)
