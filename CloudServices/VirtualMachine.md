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

- User data allows you to pass a script or configuration to a VM when it is launched. This script can be used to perform initial setup tasks such as installing software, configuring services, or running custom initialization routines.
- Custom data is a broader term used to refer to any data that you want to pass to a VM during provisioning. This can include scripts, configuration files, or any other initialization data.
