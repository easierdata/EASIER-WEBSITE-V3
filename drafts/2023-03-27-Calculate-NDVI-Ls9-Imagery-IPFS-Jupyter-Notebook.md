---
title: Calculate NDVI Ls9 Imagery IPFS Jupyter Notebook
layout: post
date: 27, March 2023
author: John Solly
sub_heading: ''
tags:
- IPFS
- Filecoin
- Landsat
- Geospatial
- GIS
related_posts: []

---

## Introduction

Geospatial professionals often work with large amounts of data, including satellite imagery, to perform various analyses such as vegetation monitoring, land cover classification, and more. One common technique used in such analyses is the Normalized Difference Vegetation Index (NDVI), which is a simple and effective way to quantify the presence and health of vegetation in an area. In this blog post, we will explore how to calculate NDVI on Landsat 9 imagery using IPFS in a Jupyter notebook. We will also highlight the advantages of using IPFS for geospatial workflows, including content-addressing and decentralization.

## What is IPFS?

IPFS, or InterPlanetary File System, is a peer-to-peer network protocol designed to create a decentralized and distributed web. It allows users to store and access content in a content-addressed way, which means that the address of the content is derived from its content itself, rather than a centralized server. This makes it highly resilient to censorship, data loss, and other forms of centralization. In addition, IPFS can be used to store and share large amounts of data, such as satellite imagery, in a highly efficient and decentralized way.

## Advantages of Using IPFS for Geospatial Workflows

Traditionally, geospatial workflows have relied on centralized storage systems such as cloud storage providers or local file systems. However, these systems have limitations in terms of scalability, security, and availability. By contrast, IPFS provides several advantages for geospatial workflows:

### Content-addressing: 
IPFS uses content-addressing, which means that the content itself is used to derive its address. This ensures that the data is tamper-proof and verifiable, and also allows for highly efficient data retrieval.

### Decentralization: 
IPFS is a peer-to-peer network, which means that data is stored and shared across multiple nodes in the network. This ensures that the data is highly available and resilient to data loss or censorship.

### Efficiency:
IPFS uses content-based addressing and data deduplication to ensure that data is stored and shared efficiently. This means that multiple copies of the same data are stored only once, and data is retrieved from the node that is closest to the requester.

How to Calculate NDVI on Landsat 9 Imagery Using IPFS

Now that we understand the advantages of using IPFS for geospatial workflows, let's see how we can calculate NDVI on Landsat 9 imagery using IPFS in a Jupyter notebook. We will be using Python and several libraries such as rasterio, matplotlib, and pystac_client.

## Step-by-Step Guide
First, we need to import the required libraries. I reccomend using a virtual environment to install the libraries. You can use the following command to install the libraries:

```py
which python3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now, we can import the libraries:
```py
import numpy as np
import rasterio
import subprocess
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.colors as mcolors
from pystac_client import Client
from IPython.display import Image
from PIL import Image as pil_image
```
Next, we will connect to the STAC API and search for Landsat 9 imagery from the Washington D.C. area:
```
catalog = Client.open("http://ec2-54-172-212-55.compute-1.amazonaws.com/api/v1/pgstac/")
bbox = [-76.964657, 38.978967, -76.928008, 39.002783]

search = catalog.search(
    collections=["landsat-c2l1"],
    bbox=bbox,
)

items = search.get_all_items()
len(items)
1
```
After connecting to the STAC API and searching for the Landsat 9 imagery, the JSON response for the item will include links to the assets using traditional storage (S3) and IPFS. Here is a snippet of the JSON that includes the S3 and IPFS CID:

In this example, we have manually modified the JSON response from the STAC API to include the IPFS CID for the Landsat 9 imagery. This modification demonstrates how IPFS can be integrated into a geospatial workflow, alongside traditional storage systems like S3. Please note that this alteration is for demonstration purposes only, and the actual STAC API response might not include the IPFS CID by default.
```json
{
  "assets": {
    "red": {
      "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band4.tif",
      "alternate": {
        "IPFS": {
          "href": "ipfs://QmTgttqUf7PvZgdSoe71j3njeEKk1hC3h22n2sQmety3To"
        }
      }
    },
    "nir08": {
      "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band5.tif",
      "alternate": {
        "IPFS": {
          "href": "ipfs://QmZkWaKSuVhFKtAwNbxSogcT6hXHMksXjhgqLu6AXHSUKq"
        }
      }
    }
  }
}
```
In a traditional workflow, you would fetch the data from the S3 bucket using the href value. However, in this tutorial, we are going to fetch the data using IPFS.

We will fetch bands 4 and 5 from the scene (Red and NIR):
```py
item = items[0]
red_band_cid = item.assets["red"].extra_fields["alternate"]["IPFS"]["href"].split("/")[-1]
nir_band_cid = item.assets["nir08"].extra_fields["alternate"]["IPFS"]["href"].split("/")[-1]

print(f"Red band CID: {red_band_cid}")
print(f"NIR band CID: {nir_band_cid}")
```

Now, we will define the helper functions to load the Landsat bands and save the plot to a buffer:


