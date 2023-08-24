In this post, we will explore a theoretical retrieval workflow for a file stored on various storage platforms including IPFS, Filecoin, and S3.

## What is Filecoin?
Filecoin is a decentralized storage network that turns cloud storage into an algorithmic market. The market runs on a blockchain with a native protocol token (also called “Filecoin”), which miners earn by providing storage to clients. Conversely, clients spend Filecoin hiring miners to store or distribute data. As with Bitcoin, Filecoin miners compete to mine blocks with sizable rewards[1].

## What is IPFS?
IPFS is a peer-to-peer hypermedia protocol designed to make the web faster, safer, and more open. IPFS is a distributed system for storing and accessing files, websites, applications, and data. It is a peer-to-peer system that allows users to store and share files in a distributed file system. IPFS uses content-addressing to uniquely identify each file in a global namespace connecting all computing devices[2].

## What is S3?
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9’s) of durability, and stores data for millions of applications for companies all around the world[3].

Each of these systems has pros and cons and can be used in different ways. In this post, we will explore a theoretical retrieval workflow for a file stored on one or all of these platforms.

## Retrieval Workflow
The following diagram shows a theoretical retrieval workflow for a file stored on various storage platforms including IPFS, Filecoin, and S3.
[Insert Diagram]

The workflow is as follows:
1. The user requests a file from the application.
2. The application checks the local cache for the file.
3. If the file is not in the local cache, the application checks the local IPFS node for the file.
4. If the file is not in the local IPFS node, the application checks the IPFS network for the file.
5. If the file is not in the IPFS network, the application checks S3 for the file.
6. If the file is not in S3, the application checks CID.contact to see if there are any miners storing the file in an unsealed state.
7. If a miner is found with an unsealed copy of the file, the application requests the file from the miner via HTTP.
8. If a miner is not found with an unsealed copy of the file, the application then checks CID.contact to see if there are any miners storing the file in a sealed state.
9. If a miner is found with a sealed copy of the file, the application connects to MetaMask and pays the miner to unseal the file.






