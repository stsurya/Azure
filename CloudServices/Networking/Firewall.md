## Azure Firewall

- To create firewall we need to have Firewall policy and AzureFirewallSubnet.
- Why we need policy is - We'll define all the rules in the policy and we can re-use these policies for different Vnets. We cannot reuse the firewall for different Vnets, but we can re-use policies for different Vnets. Firewall policy can be created in one region and can be used with different firewalls in different regions.
- Controlling outbound network access is an important part of an overall network security plan, For example, you may want to limit access to web sites.
  Azure firewall can configure:
  a) **Application rules:** that define Full Qualified Domain Name(FQDNs) that can be accessed from a subnet.
  b) **Network rules** that define source address, protcola, destination (same NSG).
  c) **NAT rules** for forwarding the request on particular port of firewall to another IP and port.
- Firewall is a managed, cloud-based network secuirty service that protects your Vnet reosurces.
- It's highly scalabale and unrestricted scalabilty. It can scale up as much as you need to accomadate the network traffic flow, you don't need to budget for your peak traffic. The more it scales, more you'll pay.
- Firewall can've multiple IP addresses.
- Applying FQDN filtering rules. you can limit outbound HTTP and HTTPS, including wildcards.
- you can terminate SSL/TLS in premium tier of firewall.
- integrating with Azure Monitor.
- By default firewall blocks everything.
