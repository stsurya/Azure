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

### Type of blobs:

**1. Block Blobs:** - Composed of blocks (up to 100 MB each) - Ideal for storing large files, such as videos, images, and documents - Each block is independently uploaded and stored, allowing for efficient uploading and downloading - Can be used for data lakes, data archiving, and big data analytics
**2. Page Blobs:** - Designed for frequent read/write operations - Organized into 512-byte pages - Suitable for virtual machine (VM) disks, databases, and files that require random access - Supports incremental updates, reducing storage costs
**3. Append Blobs:** - Optimized for append-only operations (e.g., logging, auditing) - New data is added to the end of the blob, without modifying existing data - Useful for storing log files, audit trails, and sensor data - Supports adding new blocks, but not updating or deleting existing ones.

### Blob encryption and security

**Encryption:**

- Server-Side Encryption (SSE): Azure encrypts your blobs automatically when they're uploaded, using 256-bit AES encryption.
- Client-Side Encryption (CSE): You can encrypt blobs before uploading them to Azure, using libraries like Azure Storage Client Library.

**Key Management:**

- Storage Account Keys: Azure manages storage account keys, used for SSE.
- Customer-Provided Keys (CPK): You can manage your own encryption keys, used for SSE.
- Azure Key Vault (AKV): Integrates with Azure Storage for centralized key management.

**B) Azure Table Storage:**
Microsoft Azure Table Storage was made to store structured NoSQL data something like JSON,XML. The storage is very scalable and, at the same time, very cheap to keep data in. However, it set off more expensive when you access files frequently.

- It is used for storing non-relational structured data (also known as structured NoSQL data) in the cloud.
- It is a key attribute store
- It is a cost-effective option for the storage of table-like data for applications
- Instead of using SQL database to store data, you can use Azure table storage in a more cost-effective manner.

**C) Azure File Storage:**
File Storage is a service in Azure Storage that allows you to store and share files in a hierarchical structure, similar to a file system on a computer. It's designed to support legacy applications that rely on file shares, as well as new applications that need to store and share files in a cloud-based storage solution.

Here are some key features of File Storage:

- File shares: Create file shares, similar to network file shares, that can be accessed by multiple users and applications.
- Directory hierarchy: Organize files in a hierarchical structure, with directories and subdirectories.
- File access: Access files using standard SMB (Server Message Block) protocol, NFS (Network File System) protocol, or REST API.
- Security: Control access to files and directories using Azure Active Directory (AAD) authentication and authorization.
- Data replication: Store data in multiple locations for high availability and redundancy.
- Scalability: Scale up or down to meet changing storage needs.

Use cases for File Storage include:

- Lift and shift: Migrate on-premises applications to Azure without changing code.
- File sharing: Share files between users, applications, or organizations.
- Data archiving: Store infrequently accessed files in a cost-effective manner.

**D) Azure Queue Storage:**
Queue Storage is a type of storage that is built to connect components of your application. It allows you to build flexible applications with decoupled and independent components that rely on asynchronous message queuing.

- This service used for the storage and retrieval of messages
- This service is good when you want to decouple components of an application
- A single message in the queue can be up to 64kb in size
- You can store millions of messages in the queue
