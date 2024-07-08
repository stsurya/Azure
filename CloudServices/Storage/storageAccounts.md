## Azure Storage Accounts

Storage Accounts is a service provided by azure for storing the data in it. It contains blob, queue, file shares, Tables. It uniquely provides namespace and service access to functions of storage.
It is durable, highly available, and scalable. By using Azure storage account services, we don’t need to worry about space because it will be scaled upon our demand.

**A) Azure Blob Storage:**
Azure Blob Storage is a Microsoft Azure cloud-based object storage solution. It is intended to store and manage unstructured data at scale, such as text or binary data such as photos, videos, documents, and other file formats.

- It is used to store unstructured data.
- This is ideal when you have storage solutions for files, videos, log files, and images
  It has different tier levels:
- Hot storage tier: It is ideal for objects that are accessed frequently
- Cool storage tier: It is optimized for data that are infrequently accessed. This is a less expensive option than the hot storage tier
- Achieve storage tier: It is optimized for data that is rarely accessed. Mostly used for archiving or backup data. It is the least expensive service. If you want to access data in archive tier first you need to move data into cold tier or hot tier. Data in the archive tier can take up to 15 hours to rehydrate, depending on the priority you specify for the rehydration operation.

**B) Azure Table Storage:**
Microsoft Azure Table Storage was made to store structured NoSQL data. The storage is very scalable and, at the same time, very cheap to keep data in. However, it set off more expensive when you access files frequently.

- It is used for storing non-relational structured data (also known as structured NoSQL data) in the cloud.
- It is a key attribute store
- It is a cost-effective option for the storage of table-like data for applications
- Instead of using SQL database to store data, you can use Azure table storage in a more cost-effective manner.

**C) Azure File Storage:**
Microsoft Azure File storage is a type of Azure service that was designed to support the needs of the Azure VM environment. That storage is, in essence, a network share. You can store files there that can be accessed from different Virtual Machines.

- It allows for the retrieval of files via the server message block protocol.
- Using file storage, you can mount file shares on Windows, Linux, and Mac-based machines.
- Here you don’t need to manage file servers.
