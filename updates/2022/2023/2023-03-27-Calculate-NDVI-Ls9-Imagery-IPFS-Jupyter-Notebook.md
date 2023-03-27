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