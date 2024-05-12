## OSI Model

OSI model breaks down the communication b/w two computers into seven layers. These layers are helpful for Identifying network issues.

![Image missing](./Images/OSI.png)

Whether it's the one person who can't get his laptop on the internet or website down for thousands of users. This model can help us to narrow down where the problem is and if we're able to figure it out then lot of unnecsaary work can be avoided.

7. Application Layer

This is the only layer that directly interacts with data from the user. Software applications like web browsers and email clients rely on the application layer to intiate communicaitons. This layer includes protocols like HTTPS and SMTP which enables the email communications.

6. Presentation layer

- Presentation layer is primarily responsible for preparing the data so that it can be used by the application layer and also responsible for Encryption and compressing the data.
- This layer is responsible for adding encryption on the sender's end as well as decoding the encryption on receivers end.
- Finally it is also responsible for compressing the data before sending it to layer 5 to increase the speed and efficiency by minimizing the amount of data will be transfered.

5. Session layer

- This layer is responsible for opening and closing of communication between the two devices. The time b/w opening and closing of a session is called session.
- The session layer ensures that the session stays open long enough to transfer all the data being exchanged, then promptly closes the session in order to avoid wasting resources.

- The session layer also synchronizes data transfer with checkpoints. For example, if a 100 megabyte file is being transferred, the session layer could set a checkpoint every 5 megabytes. In the case of a disconnect or a crash after 52 megabytes have been transferred, the session could be resumed from the last checkpoint, meaning only 50 more megabytes of data need to be transferred. Without the checkpoints, the entire transfer would have to begin again from scratch

4. The transport layer

- Layer 4 is responsible for end-to-end communication between the two devices.
- This includes taking data from the session layer and breaking it up into chunks called segments before sending it to layer 3. The transport layer on the receiving device is responsible for reassembling the segments into data the session layer can consume.
- Transport layer protocols include the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).

3. Network layer

- The network layer breaks up segments from the transport layer into smaller units, called packets, on the sender’s device, and reassembling these packets on the receiving device.
- Network layer protocols include IP, the Internet Control Message Protocol (ICMP), the Internet Group Message Protocol (IGMP), and the IPsec suite.

2. Data link layer

- The data link layer is very similar to the network layer, except the data link layer facilitates data transfer b/w two devices on the same network.
- The data link layer takes packets from the network layer and breaks them into smaller pieces called frames. Like the network layer, the data link layer is also responsible for flow control and error control in intra-network communication.

1. Physical layer

- This layer includes the physical equipment involved in the data transfer, such as the cables and switches.
- This is also the layer where the data gets converted into a bit stream, which is a string of 1s and 0s.
