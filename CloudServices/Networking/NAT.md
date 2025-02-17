## Understanding Azure Virtual Network NAT (Network Address Translation) 🚀

In Azure, Virtual Network NAT (Network Address Translation) is used to enable outbound internet access for virtual machines (VMs) and other resources inside a private Virtual Network (VNet) without exposing them directly to the internet.

🔹 Why Use NAT?
IPv4 addresses are limited and expensive.
Instead of assigning a public IP to each VM, NAT allows multiple private IPs to share one or more public IPs.
NAT hides the private IP addresses from external networks.
🔹 How Azure NAT Works?
Internal Resource Makes a Request 🏠 → 🌎

A VM inside a private subnet tries to access an external website (e.g., google.com).
NAT Gateway Translates IP 🔄

The request goes through the NAT Gateway, which replaces the VM’s private IP with a public IP.
This allows the request to reach the internet.
Response Comes Back 🌎 → 🏠

The external server (Google) sees the NAT Gateway’s public IP, not the VM’s private IP.
The response is sent back to the NAT Gateway, which forwards it to the correct VM.
🔹 Key Features of Azure NAT
✅ Outbound-Only Traffic – NAT does not allow inbound connections from the internet. Only responses to outbound requests are allowed.
✅ Uses Public IPs/Public IP Prefixes – You can assign a single public IP, a range (prefix), or a combination.
✅ Scales Automatically – NAT scales based on demand, ensuring high availability.
✅ Better than Load Balancer SNAT – Unlike Azure Load Balancer’s SNAT (Source Network Address Translation), NAT does not have port limitations.
