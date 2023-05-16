---
title: Proof of Concept Workflow Atomization Demo
layout: post
date: 16, May 2023
author: Matthew Nanas
sub_heading: ''
tags:
- IPFS
- Filecoin
- Code
- Publications
related_posts: []
---
# Proof of Concept Workflow Atomization Demo

With a couple of use cases of code atomization now defined (shown in the previous post), this article will present a proof of concept for atomizing a simple Python workflow and generating a manifest of CIDs for the components used.

The process presented is a simple 3 step procedure:

1. Workflow execution
2. Workflow component extraction
3. CID distribution and analysis

# Set-Up

To begin and follow this demo, create a Web3.Storage account if you have not already. [Generate an API token](https://web3.storage/docs/how-tos/generate-api-token/), our program depends on the Web3.Storage API to upload content to IPFS.

Next, clone the following Github repository: [Python-Atomizer](https://github.com/easierdata/Python-Atomizer).

In the root directory of our project, create a `.env` file and ensure it has the following content (replace the filler with your own API key):

```shell
WEB3_STORAGE_KEY="<API KEY GOES HERE>"
```

# Code Profiling

The first step to this process as highlighted in the introduction is workflow execution. If one were to take a workflow out of an intricate program they must know what functions were invoked. To achieve this, the python-atomizer ingests a code profile produced by the `cProfile` python module.

To generate this code profile, execute the following (in a terminal) in the repositories' root directory:

```shell
$ python -m cProfile -o inputs/profile inputs/morans_example.py
```

The command above will execute the `cProfile` python module (as specified by the `-m` flag) and output the recorded profile into the inputs folder in the `profile` file. `inputs/morans_example.py` refers to the entry to our program.

When executing the program, a window should pop up that illustrates a graph of a Moran's I calculation. After closing the window, the program will stop running, allowing another command to be ran in the terminal. After execution, you may notice the inputs directory now has three files: `.gitkeep`, `morans_example.py`, and `profile`. Now we are ready to move on to the second step.

# Workflow Extraction

Next, the workflow needs to be extracted and atomized. The Typescript program of this repository does both simultaneously through parsing the newly generated profile, traversing through program and module files, and writing executed components to an outputs folder. After, each component will be uploaded to IPFS through the Web3.Storage API and a dictionary for these component/CID pairs will be written.

To achieve this, execute the following in a terminal within the root directory of the repository:

```shell
$ ts-node index.ts
```

# Accessing CIDs

After the atomizer has finished executing, an outputs folder will be generated within the root directory. Here you will find both the extracted components and a file labeled manifest.json which contains a list of the components, associated CIDs, and dependencies. In the use case of a publication, one could incorporate this manifest so that queries with related CIDs will find the result as expected. Additionally, the CIDs can be used in-text to reference unchanged code, unaffected by future updates of modules/libraries. These CIDs are also accessible through your [Web3.Storage account dashboard](https://web3.storage/account/).
