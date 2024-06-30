## What is Virtual Machine ?

- A virtual machine (VM) is a computing environment that functions as an isolated system with its own CPU, memory, network interface, and storage, created from a pool of hardware resources. Software called a hypervisor isolates the necessary computing resources and enables the creation and management of VMs.
- Software called a hypervisor isolates the necessary computing resources and enables the creation and management of VMs.

## What is hypervisor ?

A hypervisor is a software that is used to create multiple virtual machines on single machine. Every virtual machine has its own operating system and applications. The hypervisior allocates the underlying physical machine resources such as CPU, memory to the virtual machines as required.

There are two type of hypervisiors:

i) The type-1 or 'bare-metal server' will sit on the physical machine and has direct access to hardware reosurces. This is more secure.

ii) the type-2, here the hypervisor is installed on the host operating system, hosted hypervisor do not have complete access on hardware resources. Here the system administrator allocates the resources for the hosted hypervisor, which it distributes to the virtual machines.
