## What is Virtual Machine ?

- A virtual machine (VM) is a computing environment that functions as an isolated system with its own CPU, memory, network interface, and storage, created from a pool of hardware resources. Software called a hypervisor isolates the necessary computing resources and enables the creation and management of VMs.
- Software called a hypervisor isolates the necessary computing resources and enables the creation and management of VMs.

## What is hypervisor ?

A hypervisor is a software that is used to create multiple virtual machines on single machine. Every virtual machine has its own operating system and applications. The hypervisior allocates the underlying physical machine resources such as CPU, memory to the virtual machines as required.

There are two type of hypervisiors:

i) The type-1 or 'bare-metal server' will sit on the physical machine and has direct access to hardware reosurces. This is more secure.

ii) the type-2, here the hypervisor is installed on the host operating system, hosted hypervisor do not have complete access on hardware resources. Here the system administrator allocates the resources for the hosted hypervisor, which it distributes to the virtual machines.

## Data Disk Vs OS Disk

- A data disk is a managed disk that's attached to a virtual machine to store application data, or other data you need to keep. Like OS disks, data disks can also use Premium SSD, Standard SSD, or Standard HDD. The choice depends on the required performance and cost considerations.
- Every virtual machine has one attached operating system disk. That OS disk has a pre-installed OS, which was selected when the VM was created. This disk contains the boot volume. The OS disk usually uses Premium SSD, Standard SSD, or Standard HDD, depending on the performance requirements and the selected VM size.

## User data Vs Custom data

- User data is a set of scripts or other metadata that's inserted to an Azure virtual machine at provision time.
- User data is a new version of custom data.
- User data is persistent. It will be available during the lifetime of the VM.
- User data can be updated from outside the VM, without stopping or rebooting the VM.
- If user data isn't added at provision time, you can still add it after provision.
- User data will not be encrypted, and any process on the VM can query this data. You should not store confidential information in user data.

- Custom data is made available to the VM during first startup or setup, which is called provisioning.
- For single VMs, you can't update custom data in the VM model. But for Virtual Machine Scale Sets, you can update custom data.
- Don't store sensitive data in custom data.

## Availability options for Azure Virtual Machines

- Availability Zones.
- Virtual Machine Scale Sets.
- Availibitly Sets.
- Azure Site Recovery.
- Load balancer.

## NIC

- Each VM will be having NIC, when we say a VM is in virtual netowrok, it's not acutally the VM, it's the NIC which is under the Vnet.
- Multiple NIC's can be attached to single VM. Those NIC's can be from different subnets but not from different Vnets.
