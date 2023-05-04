---
title: Decentralized and Deconstructed Approach to Code Artifacts
layout: post
date: 03, May 2023
author: Matthew Nanas
sub_heading: ''
tags:
- IPFS
- Filecoin
- Code
- Publications
related_posts: []
---
# Introduction

As it pertains to publications, being able to share artifacts such as code is imperative to prove methodology in practice and support the validity of findings through replicability.

Unfortunately, many publications fail to abide by open nature through broken links, outdated code snippets, and only a fraction of code used (if not any). Additionally, querying a set of publications by code contents is difficult compared to using keywords and phrases as code follows a unique syntax. As the EASIER Data Initiative continues to explore the harmony between geospatial data and web3, the team has explored opportunities to reach fields of science outside of GIS. This post will explore how the interplanetary file system (IPFS) may benefit researchers and developers through code atomization.


# Code Atomization

*Code atomization* refers to breaking down a program into smaller, manageable components. A deconstructed program enables more manageable testing and debugging. This process opens many opportunities for the web3 space. A couple use cases are explored below.


# Use Case 1 (Publications)

Code atomization opens the door for concrete code/function querying over a set of publications. By atomizing programs, authors are able to assign functions, methods, and classes within their code artifacts respective content identifiers (CIDs). And by doing so, the process of querying publications by code is simplified through searching for specific CIDs. Referencing code in-text becomes easier as one is able to cite a CID as opposed to designating a block of text for a segment of code. Moreover, a dictionary of CIDs referenced may be maintained in a glossary like fashion.

Code atomization also enables workflows to be extracted from intricate programs. An example workflow to achieve this goal would be profiling a workflow from a python program and then uploading the functions used (according to the program profile) to IPFS. In doing so, an array of CIDs are then able to be referenced to point to different parts of the program and also share a timeless characteristic such that updates to any code does not affect the snippets stored.


# Use Case 2 (Software Development)

Being able to analyze statistics regarding CID uploads/retrievals creates a powerful opportunity for software developers, namely those who build and maintain libraries. These analytics enable developers to determine what components of their projects are most used and therefore (in a subjective sense) more valuable to their end users. In turn, developers will be more aware of what to change and how to communicate changes in a more organized fashion.


# Conclusion

Considering previous blog posts, we now see how IPFS is powerful technology that benefits communities beyond just GIS and research. The ability to refer to content via CID addresses many problems and hurdles faced by publications and developers.

In our next blog post, we will demonstrate a proof-of-concept that follows atomizing a python workflow and assigning components CIDs on IPFS.
