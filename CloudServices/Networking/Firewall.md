## Azure Firewall

- To create firewall we need to have Firewall policy and AzureFirewallSubnet.
- Why we need policy is - We'll define all the rules in the policy and we can re-use these policies for different Vnets. We cannot reuse the firewall for different Vnets, but we can re-use policies for different Vnets. Firewall policy can be created in one region and can be used with different firewalls in different regions.
- We can've parent policy and child policies, parent policy is like common organisation policy and child policy is to overide the parent policies and make it flexible for each environamnet like dev,test, prod.
- You'll attach only child policy to the Firewall but the rules of parent policy will automatically be implemented ot the firewall.
- Rule Collections group is the important component of Azure Policy where you'll be creating multiple Rule collection Groups and each group can have multiple rules and each group can have priority from 100 to 65,000. Lower the number, higher the priority.
- Controlling outbound network access is an important part of an overall network security plan, For example, you may want to limit access to web sites.<br>
  Azure firewall can configure:<br>
  a) **DNAT rules** for forwarding the request on particular port of firewall to another IP and port. All the DNAT rules are processed first.<br>
  b) **Network rules** that define source address, protcola, destination (same NSG). Network rules are prccessed after DNAT rules<br>
  c) **Application rules:** that define Full Qualified Domain Name(FQDNs) that can be accessed from a subnet.<br>
- Firewall is a managed, cloud-based network secuirty service that protects your Vnet reosurces.
- It's highly scalabale and unrestricted scalabilty. It can scale up as much as you need to accomadate the network traffic flow, you don't need to budget for your peak traffic. The more it scales, more you'll pay.
- Firewall can've multiple IP addresses.
- Applying FQDN filtering rules. you can limit outbound HTTP and HTTPS, including wildcards.
- you can terminate SSL/TLS in premium tier of firewall.
- integrating with Azure Monitor.
- By default firewall blocks everything.
- We can allocate and de-allocate azure firewall by using azure powershell scripting, this doesn't stop the billing but it'll be helpfull when migrating the azure firewall from one vnet to another vnet.

- Threat intelligence based filtering can be enabled for your firewall to alert and block traffic to/from known malicious IP addresses and domains. The IP addresses and domains are sourced from the Microsoft Threat Intelligence feed. You can choose between three settings:<br>
  ● Off - This feature will not be enabled for your firewall<br>
  ● Alert only - You will receive high confidence alerts for traffic going through your firewall to or from known malicious IP addresses and domains<br>
  ● Alert and deny - Traffic will be blocked and you will receive high confidence alerts when traffic attemting to go through your firewall to or from known malicious IP addresses and domains is detected.<br>
