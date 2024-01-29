---
title: Proof of concept for querying spatial data on IPFS using geohash
layout: post
date: 22, January 2024
author: Zheng Liu
sub_heading: ''
tags:
- IPFS
- Code
- Landsat
- Geospatial
- GIS
- Geohash
related_posts: []
---
## Proof of concept for querying spatial data on IPFS using geohash

In this post we'll be exploring how to store and access geospatial data in a decentralized way using Geohash and InterPlanetary File System (IPFS). Geohash is a spatial indexing system that divides the Earth into a grid of squares and assigns a unique identifier to each square. IPFS is a peer-to-peer network that uses Content Identifiers (CIDs) to store and share data. By joining geohash to CIDs of spatial features , we can create a hierarchical indexing system that organizes geospatial features into a directory system based on the geohash encoding. This allows us to store and query geospatial data on IPFS, without relying on centralized servers or databases.

[Explore More with our Notebook](../../notebooks/geohash-ipfs-blog-post.ipynb)
