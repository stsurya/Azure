# Azure Blob Storage

- Azure blob storage is a service that enables you to store massive amounts of unstructured data as bianry large objects or blobs in Cloud. Blobs are the efficient way to store the data files and our applicaiton can perform read and write operations by using Azure blob storage API.
- In an Azure storage account you store blobs in containers. Containers provide a convenient way of grouping related blobs.You control who can read and write blobs inside a container at the container level.

Blob storage provides three access tiers, which help to balance access latency and storage cost:

- **Hot Access Tier:** The Hot tier is the default. You use this tier for blobs that are accessed frequently.
- **Cool Access Tier:** The Cool tier has lower performance and incurs reduced storage charges compared to the Hot tier. Use the Cool tier for data that is accessed infrequently.
- **Archive Tier:** The Archive tier is intended for historical data that mustn't be lost, but is required only rarely. Blobs in the Archive tier are effectively stored in an offline state.
  Typical reading latency for the Hot and Cool tiers is a few milliseconds, but for the Archive tier, it can take hours for the data to become available.
  To retrieve a blob from the Archive tier, you must change the access tier to Hot or Cool. The blob will then be rehydrated. You can read the blob only when the rehydration process is complete.

You can create lifecycle management policies for blobs in a storage account to move the tier or to delete the blobs.

---

# Azure File Shares

Azure Files is essentially a way to create cloud-based network shares, such as you typically find in on-premises organizations to make documents and other files available to multiple users.
By hosting file shares in Azure, organizations can eliminate hardware costs and maintenance overhead, and benefit from high availability and scalable cloud storage for files.

# Azure Tables

Azure table storage is a NoSQL storage solution that makes use of tables containning key/value data items. Each item is represented by a row that contains columns for the data fields that need to be stored.

- Azure tables are used to store semi-structured that something like JSON,XML.
- All rows in table will be having a partiion key and row key. Whenever you modified a row a timestamp will be created with data and time.
- When you search for data, you can include the partition key in the search criteria. This helps to narrow down the volume of data to be examined, and improves performance by reducing the amount of I/O needed to locate the data.
