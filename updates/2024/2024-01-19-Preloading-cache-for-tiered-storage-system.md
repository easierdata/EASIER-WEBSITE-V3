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

In this blog post, we explore the practical aspects of tiered storage systems, focusing on the nuances of hot and cold storage layers using different cache system strategies. The premise starts with the system's initialization and an empty hot layer or cache and illustrate the impact of prepopulating a cache with randomly selected geospatial data. Specifically centered around landsat scenes within the continental US, the two layers—cold storage and hot storage (set up as a least recently used cache)—play key roles in the experiment. We'll delve into the mechanics of data requests categorized as region, state, or county, and how the system strategically manages landsat scenes in the least recently used cache.

[Explore More with our Notebook](../../notebooks/preloading_a_cache.ipynb)
