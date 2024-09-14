## What are ports ?

Whenever any computer send data to another computer or device then it sends by using IP address, but how does our computer know that this data is for a specific application and this data is sent by any specific application? There comes the concept of Port.

- Port is a logical address of a 16-bit unsigned integer that is alloted to every application on the computer that uses the internet to send or receive data.
- Port Number or Port is used to uniquely identify any appication/services running on the same device.

## what are protocols ?

protocols are the rules that define how data is exchanged over a network, ensuring that communication between devices is possible, reliable, and secure.

## 1. ping

Purpose: To test connectivity between your computer and a remote host, and to measure the round-trip time of packets sent from your computer to the remote host.

**How It Works:**

Sends ICMP (Internet Control Message Protocol) Echo Request messages to the target host.
The target host responds with ICMP Echo Reply messages.
Measures the time taken for the round trip and displays statistics like packet loss and response time.

**Usage:**

```
ping <hostname_or_ip>
```

**Example:**

```
ping google.com
```

**Output Example:**

```
PING google.com (172.217.164.206) 56(84) bytes of data.
64 bytes from 172.217.164.206: icmp_seq=1 ttl=56 time=14.7 ms
64 bytes from 172.217.164.206: icmp_seq=2 ttl=56 time=15.1 ms
```

**Explanation:**
icmp_seq: Sequence number of the ICMP packet.
ttl: Time-to-live, which indicates the number of hops the packet can make before being discarded.
time: Round-trip time in milliseconds.

## 2. traceroute

Purpose: To trace the path packets take from your computer to a remote host and identify each hop along the route.

**How It Works:**

Sends packets with gradually increasing TTL (Time-to-Live) values.
Each hop along the route decreases the TTL by 1 and sends back an ICMP Time Exceeded message if the TTL reaches 0.
Displays the route taken and the response time from each hop.
**Usage:**

```
traceroute <hostname_or_ip>
```

**Example:**

```
traceroute google.com
```

**Output Example:**

```
traceroute to google.com (172.217.164.206), 30 hops max, 60 byte packets
1 router.local (192.168.1.1) 1.123 ms 1.345 ms 1.567 ms
2 10.0.0.1 (10.0.0.1) 5.678 ms 5.890 ms 6.123 ms
3 172.217.164.206 (172.217.164.206) 12.345 ms 12.567 ms 12.789 ms
```

**Explanation:**
Each line represents a hop along the route.
The times shown are the response times from each hop.
If a hop is not reachable, it will display \* \* \* for that hop.

## 3. nslookup

Purpose: To query DNS (Domain Name System) servers to obtain domain name or IP address information.

**How It Works:**

Sends a query to a DNS server to resolve a domain name to an IP address or vice versa.
Provides information about the DNS record types like A (Address), MX (Mail Exchange), and more.
**Usage:**

```
nslookup <hostname_or_ip>
```

**Example:**

```
nslookup google.com
```

**Output Example:**

```
Server: UnKnown
Address: 192.168.1.1

Name: google.com
Addresses: 172.217.164.206
```

**Explanation:**

Shows the DNS server being used and the resolved IP address for the given domain.
You can also use nslookup to query different DNS record types or specific DNS servers.

## 4. curl

Purpose: To transfer data to or from a server using various protocols (HTTP, HTTPS, FTP, etc.) and to test endpoints or APIs.

**How It Works:**

Sends a request to a specified URL and retrieves the response.
Supports a wide range of options for customizing the request, handling redirects, and more.
**Usage:**

```
curl <url>
```

**Example:**

```
curl https://www.example.com
```

**Output Example:**

```
<!doctype html>
<html>
<head>
<title>Example Domain</title>
...
```

**Explanation:**

Displays the response body from the server.
curl can be used with various options, such as -I for headers only or -d to send POST data.
**Additional Options:**

-I: Fetch headers only.

```
curl -I https://www.example.com
```

-d: Send data with POST request.,

```
curl -d "param1=value1&param2=value2" -X POST https://www.example.com
```
