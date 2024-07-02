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

## DeepDive into TLS Termination and End to End TLS

TLS is a standard security technology for establishing encrypted link between a web server and browser. This link ensures that all data passed between the web server and browsers remain private and encrypted. Application gateway supports both TLS termination at the gateway as well as end to end TLS encryption.

### TLS Termination

To configure the TLS/SSL Termination, a certificate must be added to the listener. This allows the Application Gateway to decrypt incoming traffic and encrypt response traffic to the client.

**Advantages of TLS Termination:**

- Improved performance.
- Better utilization of the backend servers.
- Intelligent routing.
- Certificate management

### End-to-end TLS encryption

When configured with end-to-end TLS communication mode, Application Gateway terminates the TLS sessions at the gateway and decrypts user traffic. It then applies the configured rules to select an appropriate backend pool instance to route traffic to. Application Gateway then initiates a new TLS connection to the backend server and re-encrypts data using the backend server's public key certificate before transmitting the request to the backend. Any response from the web server goes through the same process back to the end user. End-to-end TLS is enabled by setting protocol setting in Backend HTTP Setting to HTTPS, which is then applied to a backend pool.

## Web Application Firewall

Web Application Firewall (WAF) is a service that provides centralized protection of your web applications from common exploits and vulnerabilities. WAF is based on rules from the OWASP (Open Web Application Security Project) core rule sets 3.1

Web applications are increasingly targets of malicious attacks that exploit common known vulnerabilities. Common among these exploits are SQL injection attacks, cross site scripting attacks to name a few. Preventing such attacks in application code can be challenging and may require rigorous maintenance, patching and monitoring at many layers of the application topology

Existing application gateways can be converted to a Web Application Firewall enabled application gateway easily.
