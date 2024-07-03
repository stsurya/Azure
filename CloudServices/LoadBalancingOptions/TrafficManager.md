## Traffic Manager

- This is a DNS based traffic load balancer.
- This service allows you to distribute traffic to your public facing applications across the global Azure region while still providing high availability and quick responsiveness.
- If you're building a Multi-region application this is the best service for you.

Traffic manager comes with two key benefits:

- It distributes the traffic based on it's several routing methods.
- Continuous health monitoring of endpoint and automatic failover when endpoint fails.

### How it works ?

- Traffic Manager will be having endpoints.
- Endpoint is any internet facing service hosted on Azure or outside of azure.
- Traffic manager will be sending traffic based on two points one it the routing method which you selected at the creation of Traffic manager, Another is the health of endpoint. Traffic manager always checks the health of endpoint and route the traffic based on the health check.
