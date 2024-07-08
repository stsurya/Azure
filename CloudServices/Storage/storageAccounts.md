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
- Achieve storage tier: It is optimized for data that is rarely accessed. Mostly used for archiving or backup data. It is the least expensive service. If you want to access data in archive tier first you need to move data into cold tier or hot tier.
