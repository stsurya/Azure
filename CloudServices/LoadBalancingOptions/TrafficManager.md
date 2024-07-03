## Traffic Manager

- This is a DNS based traffic load balancer.
- This service allows you to distribute traffic to your public facing applications across the global Azure region while still providing high availability and quick responsiveness.
- If you're building a Multi-region application this is the best service for you.
- Naming convention of Traffic manager should be globbally unique.

Traffic manager comes with two key benefits:

- It distributes the traffic based on it's several routing methods.
- Continuous health monitoring of endpoint and automatic failover when endpoint fails.

### How it works ?

- Traffic Manager will be having endpoints.
- Endpoint is any internet facing service hosted on Azure or outside of azure.
- Traffic manager will be sending traffic based on two points one it the routing method which you selected at the creation of Traffic manager, Another is the health of endpoint. Traffic manager always checks the health of endpoint and route the traffic based on the health check.

## Routing methods

i) **Priority:** Select Priority routing when you want to have a primary service endpoint for all traffic. You can provide multiple backup endpoints in case the primary or one of the backup endpoints is unavailable.
ii) **Weighted:** Select Weighted routing when you want to distribute traffic across a set of endpoints based on their weight. Set the weight the same to distribute evenly across all endpoints.

- The weight is an integer from 1 to 1000. This parameter is optional. If omitted, Traffic Managers uses a default weight of '1'. The higher weight, the higher the priority.

iii) **Performance:** Select Performance routing when you have endpoints in different geographic locations and you want end users to use the "closest" endpoint for the lowest network latency.

iv) **Geographic:** Select Geographic routing to direct users to specific endpoints (Azure, External, or Nested) based on where their DNS queries originate from geographically. With this routing method, it enables you to be in compliance with scenarios such as data sovereignty mandates, localization of content & user experience and measuring traffic from different regions.
