---
title: Using Content Addressable aRchives to store decentralized data
layout: post
date: 25, January 2024
author: Seth Docherty
sub_heading: ''
tags:
- IPFS
- CARs
- Large Data
- Landsat
- Geospatial
- DAGs
related_posts: []
---
# Introduction

When dealing with large geospatial datasets, such as Landsat 9 imagery, effective management, storage, and seamless transfer of massive data are key challenges for both data stewards and users seeking to access the content. One common solution for bundling and compressing these datasets is using `.tar` files (a type of [File archiver](https://en.wikipedia.org/wiki/File_archiver)), aiding data stewards in organization and simplifying data transfer for users. Transitioning into the realm of decentralized systems, [Content Addressable Archives](https://ipld.io/specs/transport/car/carv1/) (CAR) present a solution akin to `.tar` files. CAR files, like their traditional counterparts, play a role in maintaining data organization and accessibility in decentralized setups. In this blog post, we'll look into the technical details of CAR files and explore some practical advantages inherent to [IPFS](https://docs.ipfs.tech/concepts/what-is-ipfs/) (InterPlanetary File System) and Web3.

## What is **content** in IPFS?

When content is imported into IPFS, a unique [CID](https://docs.ipfs.tech/concepts/content-addressing/#what-is-a-cid) (content identifier) hash is generated representing the content itself in the form of a [graph tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)). This representation can be further decomposed into smaller chunks known as blocks, where each block generates a unique CID hash node linked to the parent hash node. This hierarchial list of linked CIDs is known as a [Merkle DAG](https://docs.ipfs.tech/concepts/merkle-dag/) (Directed Acyclic Graphs). So in IPFS, when we want to identify a specific data object i.e. file or directory, we're specifying the hash value from a Merkle DAG root node, known as the content identifier, or CID. By referring to content by it's CID is known as **content addressing**. Since the CID is unique, we can use it as a link, replacing location-based identifiers, like URLs, with ones based on the content of the data itself.

Let's take a look at what this would look like visually using a directory of files:

<center><img src="https://proto.school/tutorial-assets/T0008L03-directory-graph.png"alt="CARv2 Format"width="40%"></center>

And as a Merkle DAG, we'll simplify the representation of the content with two attributes: the name of the file, and the data corresponding to the file's contents. These attributes, bundled together, make up the data of our node, represented below in the orange box.

<center><img src="https://proto.school/tutorial-assets/T0008L04-complete-dag.svg"alt="CARv2 Format"width="70%"></center>

The root directory **pics** is the **root node** of the DAG with the CID **baf8**. If we wanted to see all the content in the sub-directory, **cats**, we would reference the CID **baf7** which would return:

<center><img src="https://proto.school/tutorial-assets/T0008L04-partial-dag.svg"alt="CARv2 Format"width="40%"></center>

You may have also noticed that the **root** CID label for the **pics** directory has a higher integer value compared to the **children** CIDs for each of the files at the bottom of the graph tree.  That's because the representations of DAGs are derived from the bottom up. Each node's CID depends on it's descendants. Any alterations to the images and or additions/deletions to each folder would change the CID value of the parent node. This is because parent nodes cannot be created until CIDs of their children can be determined.

> The CID labels are purely for explanation. For an in-depth look at the formatting of a CID, see this interactive tutorial on the [Anatomy of a CID](https://proto.school/anatomy-of-a-cid).

So how does this relate to maintaining and organizing large datasets? At the heart of any dataset is it's data structure! From wikipedia, a [data structure](https://en.wikipedia.org/wiki/Data_structure) is defined as:

> In computer science, a data structure is a data organization, management and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.

The choices we make when structuring how our data is organized has significant implications for the types of interactions that can be performed. Therefore, the larger a dataset is the more important it is to tailor the structure the way we intend to use or access it. Structure gives data meaning and organization and in the case of generating DAGs, a unique identifier.

## Organizing **DAGs** into collections

Just as we structure individual data elements, we must also consider how we assemble these elements together. Collections of content introduce an extra layer of abstraction in data structuring that impacts downstream usability for dissemination and sharing.

For example, [Landsat 9 collects upwards of 750 scenes a day](https://www.usgs.gov/landsat-missions/landsat-9#:~:text=Landsat%209%20collects%20as%20many%20as%20750%20scenes%20per%20day) which equates to a total of 15,750 files! Having scenes organized into a collection of `.tar` files has several advantages for dissemination purposes:

1. **Efficiency**: Downloading a single file is often faster than downloading many smaller files due to reduced overhead. Each file download requires a separate request, which can add significant overhead when dealing with many files.
2. **Reliability**: If the download process is interrupted, it's easier to resume or restart a single file download than multiple individual file downloads.
3. **Ease of Management**: A single file is easier to manage, transfer, and keep track of than many individual files.
4. **Preservation of Structure**: Archive files like can preserve the directory structure and metadata of the original files, which can be important for certain types of data.

In the context of decentralized systems, these advantages apply as well. Just like `.tar` files, CAR files are used to organize CID's into collections.

### **But wait**... don't forget that we're in the web3 realm!

The key differentiator here is **content-based addressing** which enables the capability for CAR files to perform partial extractions. Traditional archive formats like `.tar` files treat the entire file as a single stream of data, which means to access a specific piece of data, you need to download the entire file. This can be inefficient, especially for very large datasets where bandwidth is the limiting factor. The CAR format is a serialized representation of data, where each piece of data in the collection is individually accessible, without the need to read through the entire file.

> Note: This is made possible by the inclusion of an [index in the CARv2 format](https://ipld.io/specs/transport/car/carv2/#summary), which provides a way to look up the offset of a specific block within the file.

So how do CAR files store DAGs? Let's take a look.

<center><img src="https://ipld.io/specs/transport/car/content-addressable-archives.png"alt="CARv2 Format"width="70%"></center>

The diagram above depicts a header block containing details about the DAG followed by the data payload, which is a serialized representation of the DAG. Additional technical specifications include:

1. **Header**: Begins with a header that includes the version of the CAR format and a list of the root CIDs of the data stored in the file.
2. **Data Payload**: Contains a sequence of data blocks, each prefixed with the length of the block in bytes, followed by the serialized block data.
3. **Index**: Provides a way to look up the offset of a specific block within the data payload, allowing for random access to blocks. This means you can access a specific block without having to read through the entire file.
4. **Characteristics**: Self-describing and self-contained. Includes all the blocks and the links between them, so you don't need to fetch any additional data from the network to access the data in the file.
5. **Pragmatic**: Designed to be easy to produce and consume, with a focus on practicality and efficiency. It supports both sequential access (like CARv1) and random access (thanks to the index), making it a versatile format for a wide range of use cases.

## Conclusion

Organizing and managing large geospatial datasets are challenging as it requires a data steward to tailor the data structure in a way users intend to access and use the content.  Knowing the intricacies of your data is really important but don't forget your audience and their expectations for using data are crucial in developing an underlying data structure. Though, the transition into Web3 unlocks new capabilities that provides data stewards **AND** users with flexibility of choice.  By replacing location-based identifiers with *content addressing*, files and directories are represented as DAGs where the root node is known as a *content identifier*, or CID. The CAR file format extends this capability of *content addressing* further by providing efficiency and flexible management for users and data stewards.
