## Availability sets

- Availability sets are logical groupings of VMs that reduce the chance of correlated failures bringing down related VMs at the same time.
- Availability sets place VMs in different fault domains for better reliability, especially beneficial if a region doesn't support availability zones.

- Each Virtual Machine in Availability Set is assgined an update domain and fault domain by underlying azure platform.
- Each availability set can be configured with up to 3 fault domains and 20 update domains.
- These configurations can't be changed once Availability Set is created.
- Update domains indicate groups of virtual machines and underlying physical hardware that can be rebooted at the same time.
- When more than five virtual machines are configured within a single availability set with five update domains, the sixth virtual machine is placed into the same update domain as the first virtual machine, the seventh in the same update domain as the second virtual machine, and so on.
- The order of update domains being rebooted may not proceed sequentially during planned maintenance, but only one update domain is rebooted at a time.
- A rebooted update domain is given 30 minutes to recover before maintenance is initiated on a different update domain.
- Fault domains define the group of virtual machines that share a common power source and network switch. By default, the virtual machines configured within your availability set are separated across up to three fault domains.
- While placing your virtual machines into an availability set doesn't protect your application from operating system or application-specific failures, it does limit the impact of potential physical hardware failures, network outages, or power interruptions.
