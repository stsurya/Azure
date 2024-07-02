## Azure Application Gateway

- Azure Application Gateway is the web-traffic (OSI-Layer 7) load balancer which will route the traffic to your web servers based on HTTP request.
- For example URI path or host headers. For example, you can route traffic based on the incoming URL. So if /images is in the incoming URL, you can route traffic to a specific set of servers (known as a pool) configured for images. If /video is in the URL, that traffic is routed to another pool that's optimized for videos.
  ![Image is missing](./Images/AppGateway.png)
