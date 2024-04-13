# Data Formats

You can classify data as structured, semi-structured, or unstructured.

## structured data

- Structured Data is data that adheres to fixed schema, so all the data has the same field or properties. Generally this will be in tabular format.
- Structured data is often stored in a database in which multiple tables can reference one another by using key values in a relational model.

## semi-structured data

- Semi-structured data is information that has some structure, but which allows for some variation between entity instances.
  Eg: JSON, XML.

## un-structured data

- Not all the data is structured or semi-structured. Audio,Video, Binary files all these comed under un-strucutred data.

---

# File Storage

- Files can be stored in local file systems on the hard disk of your personal computer, and on removable media such as USB drives; but in most organizations, important data files are stored centrally in some kind of shared file storage system.

Some common file formats are discussed below:

1. Delimited text files: Delimiter is a characteer which sepreates the data like comma,period or new line character. Eg: CSV, TSV e.t.c

2. JSON, XML

3. blob(Binary Large Object)

---

# Databses

A database is a central system, where data can be stored and queried.

## Relational Database

Relational databases are the type of databases which are used to store and query strucutred data. Here the data is orgnaized in the form of tables i.e., rows and columns. The relationship b/w tables is established using keys such as primary key of one table is linked to foreign key of another table to create the relationship b/w tables. These relationships allow data to be distributed across multiple tables while ensuring consistency and integrity.

## Non-Relational Database

Non-relational database won't apply relational schema to the data.

There are four common types of Non-relational database commonly in use:

**Key-value database:** In which each record consists of a unique key and an associated value, which can be in any format.
![alt text](./Images/Key-value-DB.png)

**Document Database:** Here it is key-value database, when value is JSON Document.
![alt text](./Images/Document-DB.png)

**Column amily Database:** which store tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.
![alt text](./Images/Column-dB.png)

**Graph databases** which store entities as nodes with links to define relationships between them.
