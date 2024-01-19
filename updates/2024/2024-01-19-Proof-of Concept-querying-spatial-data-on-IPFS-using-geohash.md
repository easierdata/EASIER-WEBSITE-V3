---
title: Preloading a cache for a tiered storage system
layout: post
date: 19, January 2024
author: Jack Rickey
sub_heading: ''
tags:
- Filecoin
- Landsat
- Geospatial
- GIS
- Cache
related_posts: []
---
## Preloading a cache for a tiered storage system

A tiered storage system will have a hot and cold storage layer. Upon the initialization of the system, the hot layer (or cache) will be empty. This demo will show that prepopulating the cache, with randomly selected geospatial data can improve the long term performance of the system for most applications.

###### How is this storage system set up?

For this experiment, there are two layers where geospatial data in the form of landsat scenes can reside: the cold storage layer and the hot storage layer. The hot storage layer is constructed as a least recently used cache.

###### What data is being used?

The data that is used in this experiment are landsat scenes within the continental US. These data cannot be divided, therefore one landsat scene must reside in either the cold storage layer or the least recently used cache.

###### How is data requested?

Requests for data can be of three forms. A region, a state, or a county. When a request for either of these three sets is placed, the system will determine which landsat scenes encompass the request in its entirety, then move these scenes to the least recently used cache.

###### What is a least recently used cache?

A least recently used or LRU cache is a cache system which is based on a stack. When data are retrieved from the cache, these data are moved to the bottom of the stack. When new data are placed in the cache, these new data take the place of data at the top of the stack, which is popped off.  Effectively, this means that the cache will maintain data which are frequently requested. Data which was requested the least recently is what will be removed first to make room for new data.

[Explore More with our Notebook](../../notebooks/geohash-ipfs-blog-post.ipynb)
