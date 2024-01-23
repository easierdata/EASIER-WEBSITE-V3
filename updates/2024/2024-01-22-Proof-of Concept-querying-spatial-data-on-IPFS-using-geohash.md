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

InterPlanetary File System (IPFS) offers an alternative approach to store and distribute spatial data. Size of spatial data grows exponentially so it is imperative to perform efficient partial selection of data to avoid large bulk download over IPFS which can save both transaction time and local storage space. Yet there is a lack of support in spatial query functionality like PostGIS in the traditional database of PostgreSQL. This blog post introduces one type of spatial indexing – *[geohash](https://en.wikipedia.org/wiki/Geohash "geohash")* and walks through a proof of concept to integrate geohash into the IPFS system. The final section depicts preliminary result for the implementation in comparison with solutions using local storage, local database, and vanilla IPFS without any spatial index.

[Explore More with our Notebook](../../notebooks/geohash-ipfs-blog-post.ipynb)
