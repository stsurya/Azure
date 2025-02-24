## Network Virtual Appliance

A Network Virtual Appliance (NVA) is a virtual machine that performs network functions such as firewalling, routing, WAN optimization, or load balancing. NVAs are commonly used to provide advanced network security, traffic inspection, or custom network routing in cloud environments.

- NAV's are always deployed on Vitrual Machines.

**Key Use Cases of NVAs**

- Firewall & Security – Acts as a next-generation firewall (NGFW) to inspect and filter traffic (e.g., Palo Alto, Check Point, FortiGate).
- Intrusion Detection/Prevention (IDS/IPS) – Detects and prevents malicious traffic in real time.
- Traffic Filtering & Routing – Controls and routes traffic between subnets, VNets, or on-premises networks.
- VPN Gateway Replacement – Used for custom VPN solutions instead of Azure VPN Gateway.
- WAN Optimization – Enhances performance of traffic between Azure and on-prem.
- Application Load Balancing – Provides advanced Layer 7 load balancing beyond Azure’s native load balancers.

## Step-by-Step Traffic Flow

1️⃣ User → Web Server (Request)

- The User (10.1.0.5) sends a request to the Web Server (20.1.0.10).
- The request first goes through the NVA (Firewall), which inspects it and allows it.
- The request is then forwarded to the Web Server.

2️⃣ Web Server → NVA (Response)

- The Web Server sends a response back to the User.
- Since the original request passed through the NVA, the response must also go through it.
- The stateful NVA remembers the session and allows the response traffic.

3️⃣ NVA → User (Final Delivery)

- The NVA forwards the response to the original User (10.1.0.5).
