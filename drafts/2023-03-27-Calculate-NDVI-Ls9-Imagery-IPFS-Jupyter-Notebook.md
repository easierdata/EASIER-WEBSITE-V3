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

Geospatial professionals often work with large amounts of data, such as satellite imagery, for object detection, land cover classification, and more. One common technique used in such analyses is the Normalized Difference Vegetation Index (NDVI), which is a simple and effective way to quantify the presence and health of vegetation in an area. In this blog post, we will explore how to calculate NDVI on Landsat 9 imagery using IPFS in a Jupyter notebook. We will also highlight the advantages of using IPFS for geospatial workflows, including content-addressing and decentralization.

## What is IPFS?

IPFS, or InterPlanetary File System, is a peer-to-peer network protocol designed to create a decentralized and distributed web. It allows users to store and access content in a content-addressed manner, which means that the address of the content is derived from the content itself, rather than relying on a centralized server. This makes IPFS highly resilient to censorship, data loss, and other forms of centralization.

In addition, IPFS is a peer-to-peer network, meaning that data is stored and shared across multiple nodes in the network. When you query the IPFS network for a piece of content, the network returns the content from the node that is closest to you¹, resulting in faster data access and reduced load on any single node. IPFS can be thought of as a decentralized version of BitTorrent that utilizes content-addressing instead of file names, which offers significant benefits in terms of data persistence, efficiency, and security.

## Advantages of Using IPFS for Geospatial Workflows

Traditionally, geospatial workflows have relied on centralized storage systems such as cloud storage providers or local file systems. However, these systems have limitations in terms of scalability, security, and availability. By contrast, IPFS provides several advantages for geospatial workflows:
1. Content-addressing
2. Decentralization
3. Censorship Resistance

### Content-addressing: 
IPFS uses content-addressing, which means that the content itself is used to derive its address. This ensures that the data is tamper-proof and verifiable, and also allows for highly efficient data retrieval.

### Decentralization: 
IPFS is a peer-to-peer network, which means that data is stored and shared across multiple nodes in the network. This ensures that the data is highly available and resilient to data loss or censorship.

### Censorship Resistance:
IPFS is a peer-to-peer network, which means that data is stored and shared across multiple nodes in the network. This ensures that the data is highly available and resilient to data loss or censorship.

## How to Calculate NDVI on Landsat 9 Imagery Using IPFS
Now that we understand the advantages of using IPFS, let's see how we can calculate NDVI on Landsat 9 imagery using IPFS in a Jupyter notebook. We will be using several libraries such as rasterio, matplotlib, and pystac_client.

## Step-by-Step Guide
First, we need to import the required libraries. I reccomend using a virtual environment to install the Python libraries. Here is the [requirements.txt](https://github.com/easierdata/stac-fastapi/blob/master/samples/requirements.txt) file I used for this tutorial:

```shell
which python3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
As of this writing, the repo that houses the Python bindings for IPFS is out of date and is [looking for a maintainer](https://github.com/ipfs-shipyard/py-ipfs-http-client/issues/316). Instead, we will install the IPFS CLI and use the subprocess library to run the CLI commands. We will also need to install the IPFS daemon, which will run in the background and allow us to access the IPFS network.

1 - [Install IPFS Kubo](https://docs.ipfs.tech/install/command-line/#install-ipfs-kubo) this will allow you to interact with the IPFS network from the command line.

2 - [Install IPFS Desktop](https://docs.ipfs.tech/install/ipfs-desktop/), which will run the IPFS daemon in the background as long as the application is running. I've found this to be the easiest way to run the IPFS daemon on my Macbook. Plus you get a nice GUI to manage your IPFS node.

Now that we have installed the Python libraries, Kubo CLI, and IPFS Desktop, we can get started with the tutorial! First, we will import the required libraries:
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
Before we continue with the steps to connect to the STAC API and search for Landsat 9 imagery from the Washington D.C. area, it's worth mentioning that we have set up a STAC server ourselves and populated it with IPFS CIDs for the Landsat 9 dataset. To learn more about the technique we used for this process, you can refer to this blog post: [A New Way to Reference and Retrieve Geographic Data](https://easierdata.org/updates/2022/2022-12-02-a-new-way-to-reference-and-retrieve-geographic-data).

If you're interested in setting up your own STAC server and populating it with IPFS CIDs, you can follow the steps outlined in our [stac-fastapi GitHub repository fork](https://github.com/easierdata/stac-fastapi).

With that background, let's continue with connecting to our STAC API and searching for Landsat 9 imagery from the Washington D.C. area:
```
catalog = Client.open("http://ec2-54-172-212-55.compute-1.amazonaws.com/api/v1/pgstac/")
bbox = [-76.964657, 38.978967, -76.928008, 39.002783]

search = catalog.search(
    collections=["landsat-c2l1"],
    bbox=bbox,
)

items = search.get_all_items()
item = items[0]
len(item)
> 1
```
After connecting to the STAC API and searching for the Landsat 9 imagery, the JSON response (item) will include links to the assets using traditional storage (S3) and IPFS. Here is a snippet of the JSON that includes the S3 and IPFS CID:

In this example, you can see how we injected the CID into the STAC json. This modification demonstrates how IPFS can be integrated into a geospatial workflow, alongside traditional storage systems like S3.
```json
{
  "assets": {
    "red": {
      "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band4.tif",
      "alternate": {
        "S3": {
          "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band4.tif"
          },
        "IPFS": {
          "href": "ipfs://QmTgttqUf7PvZgdSoe71j3njeEKk1hC3h22n2sQmety3To"
        }
      }
    },
    "nir08": {
      "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band5.tif",
      "alternate": {
        "S3": {
          "href": "s3://usgs-landsat/collection02/.../LC08_L1TP_014033_20210905_20210917_02_T1_sr_band5.tif"
          },
        "IPFS": {
          "href": "ipfs://QmZkWaKSuVhFKtAwNbxSogcT6hXHMksXjhgqLu6AXHSUKq"
        }
      }
    }
  }
}
```
At this point, In a traditional workflow, you would fetch the data from the S3 bucket using the href value. However, in this tutorial, we are going to fetch the data using IPFS.

We will grab bands 4 and 5 (Red and NIR) from the scene response object :
```py
red_band_cid = item.assets["red"].extra_fields["alternate"]["IPFS"]["href"].split("/")[-1]
nir_band_cid = item.assets["nir08"].extra_fields["alternate"]["IPFS"]["href"].split("/")[-1]

print(f"Red band CID: {red_band_cid}")
print(f"NIR band CID: {nir_band_cid}")
> Red band CID: QmTgttqUf7PvZgdSoe71j3njeEKk1hC3h22n2sQmety3To
> NIR band CID: QmZkWaKSuVhFKtAwNbxSogcT6hXHMksXjhgqLu6AXHSUKq
```
Next, we will fetch the bands from IPFS using the CIDs we extracted from the STAC server earlier. Because we aren't using a native Python library to interact with IPFS, we will use the subprocess library to run the IPFS CLI commands. The [check_output](https://docs.python.org/3/library/subprocess.html#subprocess.check_output) function will return the output of the command as a byte string. We will use this output to load the Landsat bands into numpy arrays.

```py
red_band = subprocess.check_output(["ipfs", "cat", red_band_cid])
nir_band = subprocess.check_output(["ipfs", "cat", nir_band_cid])
```
Now that we have the landsat scene data in-memory, we will define helper functions to load the Landsat data into numpy arrays and save the NDVI plot to a buffer that we'll upload to IPFS later:

```py
def load_landsat_band(band: bytes) -> np.ndarray:
    with rasterio.MemoryFile(band) as memfile:
        with memfile.open() as dataset:
            return dataset.read(1)

def save_plot_to_buffer(plot: plt.Figure) -> bytes:
    buffer = BytesIO()
    plot.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer.getvalue()
```
With the helper functions defined, we can load the Landsat bands into numpy arrays:

```py
red_band_4 = load_landsat_band(red_band)
nir_band_5 = load_landsat_band(nir_band)
```

Now, we can calculate the NDVI using the loaded numpy arrays. The forumula we are using for NDVI is straight from the [USGS website](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-difference-vegetation-index?qt-science_support_page_related_con=0#qt-science_support_page_related_con). We will also add a small value to the denominator to avoid divide by zero errors because there is a chance that the red and NIR bands will have the same value in a given pixel.

```py
eps = 0.0001  # Avoid divide by zero errors
ndvi = (nir_band_5 - red_band_4) / (nir_band_5 + red_band_4 + eps)
```

With the NDVI calculated, we can plot the NDVI image using matplotlib.

```py
# Set min and max values for better color differentiation
ndvi_min, ndvi_max = -1, 1

# Create a custom color map
cmap = plt.cm.RdYlGn
norm = mcolors.Normalize(vmin=ndvi_min, vmax=ndvi_max)

# Plot the NDVI image
fig, ax = plt.subplots()
im = ax.imshow(ndvi, cmap=cmap, norm=norm)
cbar = fig.colorbar(im, ax=ax, label='NDVI', cmap=cmap, norm=norm)
ax.set_title('Normalized Difference Vegetation Index (NDVI)')
# NDVI image plot is shown here
```

That last pieve of code should have generated a plot of the NDVI image. However, we want to save the plot to a buffer so we can add it to IPFS. We can do this by using the helper function we defined earlier. Essentially we are just 'saving' the png into memory instead of writing it to a file. That way we can upload it to IPFS without having to write it to disk.

```py
plot_buffer = save_plot_to_buffer(fig)
```

Now, let's add the plot to our local IPFS node using the [ipfs add](https://docs.ipfs.io/reference/cli/#ipfs-add) command. The `-q` flag will return the CID hash of the added file. We will use this hash to fetch the plot image from IPFS later.

```
ipfs_hash = subprocess.check_output(["ipfs", "add", "-q"], input=plot_buffer).decode().strip()
ipfs_hash
> 'QmZasRR5ath2hAXApYKwy4droFhiHAPpk4yvBDuKvKRYGE'
```

Now that we have the plot saved to IPFS, we can fetch it from our local node using the CID hash. We can use the [ipfs cat](https://docs.ipfs.io/reference/cli/#ipfs-cat) command to fetch the plot image from IPFS. The output of the command will be a byte string that we can use to load the image into a PIL image object to display it in the notebook.

```
ipfs_plot_png = subprocess.check_output(["ipfs", "cat", ipfs_hash])
img = pil_image.open(BytesIO(ipfs_plot_png))
display(img)
> NDVI image is shown
```
It's the same plot we generated earlier, but this time it's stored on IPFS! 

It's important to note that the IPFS node we just wrote to and fetched from are on our local machine. This means that the data is only available to us. If we want to share the data with others, we will need to pin the data to a public IPFS node. We can do this by using the [ipfs pin add](https://docs.ipfs.io/reference/cli/#ipfs-pin-add) command.
```py
subprocess.check_output(["ipfs", "pin", "add", ipfs_hash])
```
After pinning the data to our local IPFS node, we can fetch it from any IPFS node worldwide using the same IPFS get command as before. However, keep in mind that download speeds will be influenced by the distance between your computer and the requester's location, as well as the internet connection speeds for both parties. To make your data more accessible, you can consider using a pinning service like [Pinata](https://www.pinata.cloud/) or managing the pinning yourself by setting up your own IPFS nodes.

## Conclusion
In this blog post, we demonstrated how to calculate NDVI on Landsat 9 imagery using IPFS in a Jupyter notebook. By leveraging IPFS in place of traditional storage systems, we can benefit from content-addressing and decentralization. These features lead to faster data access, improved data persistence, and more efficient storage, highlighting the potential of IPFS in geospatial workflows.

## Footnotes
¹ The IPFS node may not actually be the closest node to you. But is simply the one that is most capable of serving the data. This is because IPFS nodes are not required to be online 24/7 and have various levels of bandwidth and storage capacity.