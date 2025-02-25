## Azure DNS Zone

- A DNS Zone is a logical grouping of DNS records that belong to a specific domain.

1. Hosting DNS records: Azure DNS Zone allows you to host your DNS records in the cloud, making it easy to manage and maintain your domain's DNS settings.
2. High availability: Azure DNS Zone provides high availability and redundancy, ensuring that your DNS records are always accessible and resolving correctly.
3. Support for various record types: Azure DNS Zone supports various DNS record types, including A, AAAA, CNAME, MX, NS, PTR, SOA, and TXT records.

## How DNS Zone works ?

For example let's say there is a domain surya.com.

There are lot of servers where the code is sitting and before the servers there is a load balancer which will distibute the traffic among all the servers. This load balancer will be having an IP address let's say 10.34.20.3

- So whenever a user hits surya.com it need to re-direct to the IP 10.34.20.3.
- These two surya.com and 10.34.20.3 need to link some where....that is called DNS Zone.

- DNS Zones and Private DNS zones are Global in Azure.
