## What is cloud technology ?

A cloud is a virtual space where users can store their software, applications including services like network, storage, databases and can share thorugh the internet without the restriciton of physical location and also cloud comes with lot of advantages like location independence, scalabilty, reliabiltiy and Better storage.

## Main features of cloud computing

- **Agility:** Huge amounts of computing resources can be provisioned within minutes.
- **Scalability:** Cloud allows to sclae up and down the resource based on demand and requirement.
- **Better storage:** There are no limitations on cloud for storage.
- **Reliability:** Data backup and disaster recovery becomes easier and less expensive.
- **Locatio independence:** Resources can be accessed anywhere from internet.

## Cloud delivery models

- **Infrastructure as a Service(IAAS):** It's also known as Hardware as service. It delivers the services like network, storage, operating system over the internet without a need of buying the physical servers and maintaining them.
  Eg: Virtual machine, Load Balancer, Virtual Network

- **Platform as a Service(PAAS):** It combines IAAS with an abstracted collection of middleware services, software development, deployment tools. PaaS helps developers quickly to create web or mobile apps.
  Eg: Function apps, web apps

- **Software as a Service(SAAS):** It is software on-demand. It is a software in which the applications are hosted by a cloud service provider.

## Different versions of cloud

- **Public Cloud:** The set of services like network, storage, hardware e.t.c are maintained and operated by third party like azure. They build highly scalable physical data centers that hides the underlying infrastructure from the consumer. They're successfull because they offer many options for computing, storage, and a rich set of other services.

- **Private Cloud:** The set of service network, storage, hardware e.t.c are owned and maintained by a organization fo9r it's employees, customers. They're not publicly available, these are highly secured as they sit behind the firewall.

- **Hybrid Cloud:** Combination of public and private cloud.

- **Multi Cloud:** Some companies use variety of public clouds to suuprt their business.

## Who are direct consumers ?

Direct customers are those who use your applications which is developed in an cloud environment. Tehy don't whether you're susing private cloud or public cloud.

## Who are cloud consumers ?

Cloud consumers are the individuals or groups within a business unit that use the various cloud services provided to get a task done.

## Serverless component in Cloud Computing

Serverless componets allow the building of applications wihtout much worrying about the infrastructure.One can write code without having provision to a server.

## Define microservices

Microservices is the process of creating applications that include code which is independent of each other.

## importance of microservices

- microservice is desgined to serve a specific purpose, so applciation developement is easy.
- It's easier and faster to make code changes using microservices.
- They're scalable, hence easy to deploy additional instances.

## What is hypervisor ?

A hypervisor is a software that is used to create multiple virtual machines on single machine. Every virtual machine has its own operating system and applications. The hypervisior allocates the underlying physical machine resources such as CPU, memory to the virtual machines as required.

There are two type of hypervisiors:

i) The type-1 or 'bare-metal server' will sit on the physical machine and has direct access to hardware reosurces. This is more secure.

ii) the type-2, here the hypervisor is installed on the host operating system, hosted hypervisor do not have complete access on hardware resources. Here the system administrator allocates the resources for the hosted hypervisor, which it distributes to the virtual machines.

## What is CDN ?

When a user visits a website, data from that website's server has to travel across the internet to reach the user's computer. If the user is located far from that server, it will take a long time to load a large file, such as a video or website image. Instead, the website content is stored on CDN servers geographically closer to the users and reaches their computers much faster.

Caching
Caching is the process of storing multiple copies of the same data for faster data access. In computing, the principle of caching applies to all types of memory and storage management. In CDN technology, the term refers to the process of storing static website content on multiple servers in the network. Caching in CDN works as follows:

A geographically remote website visitor makes the first request for static web content from your site.
The request reaches your web application server or origin server. The origin server sends the response to the remote visitor. At the same time, it also sends a copy of the response to the CDN POP geographically closest to that visitor.
The CDN POP server stores the copy as a cached file.
The next time this visitor, or any other visitor in that location, makes the same request, the caching server, not the origin server, sends the response.
