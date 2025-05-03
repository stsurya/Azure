## Azure Application Gateway

- Azure Application Gateway is the web-traffic (OSI-Layer 7) load balancer which will route the traffic to your web servers based on HTTP request.
- For example URI path or host headers. For example, you can route traffic based on the incoming URL. So if /images is in the incoming URL, you can route traffic to a specific set of servers (known as a pool) configured for images. If /video is in the URL, that traffic is routed to another pool that's optimized for videos.
  ![Image is missing](./Images/AppGateway.png)

- App Gateway can have either private IP and Public IP nor Public only, cannot have only private IP.

Scenario that I've implemented for app gateway is:

- For non-production env's application should not be publicly accessible but for prod env application should be publicly accessible.
- So we've two app gateways one for prod env and another for non-prod env.
- For non-prod env's we've the frontend public IP and attached a NSG on the subnet of app gateway and allowed only our office network ip address to our Virtual Network and blocked everything else.

- We need to use Application Gateway v2 as this is the latest version of App Gateway.

Feature of Application Gateway:

### AutoScaling

Application Gateway Standard_v2 supports autoscaling and can scale up or down based on changing traffic load patterns. Autoscaling also removes the requirement to choose a deployment size or instance count during provisioning.

### Zone redundancy

A Standard_v2 Application Gateway can span multiple Availability Zones, offering better fault resiliency and removing the need to provision separate Application Gateways in each zone.

### Secure Sockets Layer (SSL/TLS) termination

Application Gateway will support SSL/TLS termination at gateway, after which traffic flow to the servers unencrypted. This feature allows web servers to be unburdened from costly encryption and decryption overhead. But sometimes unencrypted communication to the servers isn't an acceptable option. This can be because of security requirements, compliance requirements, or the application may only accept a secure connection. For these applications, application gateway supports end to end SSL/TLS encryption.

## 🔍 What Is a Listener in App Gateway ?

A **listener** is a logical entity that defines how the Application Gateway should listen for incoming traffic. It specifies:

- **Frontend IP address**: The IP address (public or private) where the gateway listens for requests.
- **Protocol**: HTTP or HTTPS.
- **Port**: The port number (commonly 80 for HTTP and 443 for HTTPS).
- **Host name**: Used in multi-site configurations to route traffic based on the host header.

When a client sends a request, the listener determines if it matches its configuration and, if so, processes the request accordingly.

---

## 🎯 Types of Listeners

### 1. **Basic Listener**

- **Purpose**: Handles traffic for a single domain.
- **Configuration**: Listens on a specific IP, port, and protocol without host name differentiation.
- **Use Case**: Suitable when hosting a single site or application.
- You can't have two listeners with same port and same frontend IP for basic listeners.

### 2. **Multi-site Listener**

- **Purpose**: Allows hosting multiple domains or subdomains on the same Application Gateway.
- **Configuration**: Differentiates traffic based on the host name in the request.
- **Use Case**: Ideal for hosting multiple websites or services behind a single gateway.

---

## 🔐 HTTPS and SSL Termination

For HTTPS listeners, you need to associate an SSL certificate. This enables the Application Gateway to decrypt incoming traffic before routing it to the backend. You can manage SSL certificates directly or integrate with Azure Key Vault for secure storage and management.

---

## 🔁 Listener and Routing Rules

Each listener is associated with a **request routing rule** that defines how traffic should be directed:

- **Basic Rule**: Routes all traffic from the listener to a specific backend pool.
- **Path-based Rule**: Routes traffic based on URL path patterns, allowing for more granular control.
- One Listener can only link with one Rule and vice-versa.

These rules determine which backend pool the traffic should be sent to and can include additional settings like URL path-based routing.

## 🧠 Best Practices

- **Use Multi-site Listeners**: When hosting multiple domains, use multi-site listeners to efficiently manage traffic.
- **Secure with HTTPS**: Always prefer HTTPS listeners to encrypt traffic between clients and the gateway.
- **Manage SSL Certificates**: Utilize Azure Key Vault for secure and centralized certificate management.
- **Monitor Listener Health**: Regularly check listener configurations and associated routing rules to ensure optimal performance.

---

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
