## Azure Application Gateway

- Azure Application Gateway is the web-traffic (OSI-Layer 7) load balancer which will route the traffic to your web servers based on HTTP request.
- For example URI path or host headers. For example, you can route traffic based on the incoming URL. So if /images is in the incoming URL, you can route traffic to a specific set of servers (known as a pool) configured for images. If /video is in the URL, that traffic is routed to another pool that's optimized for videos.
  ![Image is missing](./Images/AppGateway.png)

- We need to use Application Gateway v2 as this is the latest version of App Gateway.

Feature of Application Gateway:

### AutoScaling

Application Gateway Standard_v2 supports autoscaling and can scale up or down based on changing traffic load patterns. Autoscaling also removes the requirement to choose a deployment size or instance count during provisioning.

### Zone redundancy

A Standard_v2 Application Gateway can span multiple Availability Zones, offering better fault resiliency and removing the need to provision separate Application Gateways in each zone.

### Secure Sockets Layer (SSL/TLS) termination

Application Gateway will support SSL/TLS termination at gateway, after which traffic flow to the servers unencrypted. This feature allows web servers to be unburdened from costly encryption and decryption overhead. But sometimes unencrypted communication to the servers isn't an acceptable option. This can be because of security requirements, compliance requirements, or the application may only accept a secure connection. For these applications, application gateway supports end to end SSL/TLS encryption.
