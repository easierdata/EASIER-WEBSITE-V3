---
title: Changes in ipfs-stac v0.2.0
layout: post
date: 4, November 2024
author: Matthew Nanas
sub_heading: ''
tags:
- IPFS
- Code
- Python
- STAC
related_posts: []
---
## Preface

One of the pivotal projects the EASIER Data Initiative has produced is [ipfs-stac](https://pypi.org/project/ipfs-stac/). The Python library is a testament to the feasibility of onboarding and interfacing geospatial data on IPFS. The library enables developers and researchers to leverage STAC APIs enriched with Filecoin and IPFS metadata to seamlessly fetch, pin, and explore data in a familiar manner. In an ambiguous ecosystem with everchanging advancements, updates, breaking changes, and new features of the infrastructure will emerge. The team has made it a responsibility to adhere to these changes and that has prompted our projects to remain flexible. This notebook will explore the many new features and changes to ipfs-stac in version 0.2. A high level overview of the changes is also found below.

[Explore More with our Notebook](../../notebooks/ipfs-stac-v020-updates.ipynb)

### Changes Summary

1. When fetching content, the file size is now human-readable (progress is now tracked in Megabytes)
2. New search functionality via `searchSTAC` method added to the `web3` client class. Returns a collection of items
   1. A user can now pass in many of the [query parameters options](https://github.com/radiantearth/stac-api-spec/tree/release/v1.0.0/item-search#query-parameters-and-fields) to search a STAC catalog
3. Added parameters for content uploads to ipfs:
   1. By default, [CIDv1](https://docs.ipfs.tech/concepts/glossary/#cid-v1) are created
   2. Added option to select whether to pin content to your IPFS node
   3. Added option to add mutable file system (MFS) reference to the content on upload
   4. Added option to provide a filename to content that's uploaded
      1. If a user uploads a file, the filename is extracted. You can override by passing in a value to this parameter.
4. Optimized functions that start and stop ipfs daemon
5. Assets are no longer fetched by default
6. Added `getAssetNames` function to retrieve the asset names from a collection or item
7. New `Web3` class property that automatically grabs all the collection id from the stac endpoint when instantiated.
8. `pinned_list` returns
