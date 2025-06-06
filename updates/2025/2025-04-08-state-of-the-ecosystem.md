---
title: State of the Ecosystem - A Closer Look at the Decentralized Geospatial Web

layout: post

date: 08, April 2025

author: Seth Docherty

sub_heading: ''

tags:

- Astral

- Easier

- Collaboration

---

# State of the Ecosystem - A Closer Look at the Decentralized Geospatial Web

As part of our ongoing efforts under [The Decentralized Geospatial Collaborative](https://decentralizedgeo.org/), we've started to define the ecosystem for decentralized geospatial tooling.  We've also been fostering a community on the [Telegram Astral channel](https://t.me/+UkTOSXnDcDM5ZTBk), with discussions on expanding the possibilities of decentralization within the digital geospatial realm. In this post, we take a closer look at the core applications and tools that form the backbone of this ecosystem, each playing a critical role in enabling decentralized geospatial capabilities.

## Core Components of the Decentralized Geospatial Ecosystem

These applications and protocols are redefining how geospatial data is stored, shared, and verified in a decentralized and trust-minimized manner.

### 1. STAC Ecosystem: Discover geospatial content on decentralized networks

The **[STAC Ecosystem](https://stacspec.org/en)** enables users to discover geospatial content stored on decentralized networks. By leveraging the interoperability of SpatioTemporal Asset Catalog (STAC) specification, we can extend the metadata that describes each collection of data.  This includes tags like [content identifiers](https://docs.ipfs.tech/concepts/content-addressing/) (CIDs) for retrieving content from IPFS and a [Filecoin Piece](https://spec.filecoin.io/systems/filecoin_files/piece/) CID to identify storage providers on the Filecoin network that are storing the file.

- **Capabilities:**
  - Provides a standardized way to describe geospatial assets and collections.
  - Enables decentralized discovery of geospatial content.
  - Enhances interoperability between geospatial tools and decentralized storage solutions.
- **How it fits in:**
  - Acts as a bridge between traditional geospatial workflows and decentralized storage solutions.
  - Facilitates the creation of geospatial applications that leverage decentralized networks like IPFS and Filecoin.

### 2. ipfs-stac: Decentralized retrieval of geospatial content

The **[ipfs-stac](https://github.com/DecentralizedGeo/ipfs-stac)** library provides an interface between geospatial datasets and decentralized storage solutions like IPFS and Filecoin. Built as a Python client, it enables users to manage and retrieve geospatial assets in a decentralized way, ensuring data persistence and integrity without reliance on centralized servers.

- **Capabilities:**
  - Stores and retrieves geospatial metadata and assets using IPFS and Filecoin.
  - Supports the **STAC (Spatiotemporal Asset Catalog) specification**, making it interoperable with existing geospatial tools.
  - Enhances data availability for decentralized applications needing reliable geospatial data sources.

- **How it fits in:**
  - This tool bridges the gap between Web3 storage solutions and traditional GIS workflows.
  - It allows researchers, developers, and institutions to securely share and retrieve geospatial datasets without a central authority.

### 3. Web3 Geo-Dashboard and Extension: Explore Decentralized Geospatial Data

The motivation behind this project is to demonstrate how decentralized technologies like IPFS and Filecoin can foster an open ecosystem for geospatial data exploration and management. The **[Web3 Geo-Dashboard](https://github.com/DecentralizedGeo/web3-geo-dashboard)** provides a visual interface to explore STAC endpoints that contain geospatial assets stored on IPFS and Filecoin. The accompanying **[Browser Extension](https://github.com/DecentralizedGeo/web3-geo-extension)** enhances the dashboard's interactive capabilities, allowing users to simply retrieve the data they are interested in via CIDs, instead of relying on centralized servers.

- **Capabilities:**
  - Visually explore geospatial datasets from STAC endpoints.
  - Manage and retrieve geospatial assets stored on IPFS and Filecoin.
  - Data retrieval is managed at the content level: reference data based on **what** it is instead of **where** to access and download it.

- **How it fits in:**
  - Cultivates an open ecosystem for exploring decentralized geospatial data.
  - Allows users and developers to explore and verify metadata stored on decentralized networks.

### 4. API: A gateway for accessing location proofs on decentralized networks

The **[API](https://github.com/DecentralizedGeo/astral-api)** serves as a **unified access point** for accessing location proofs that are designed to work seamlessly with the Astral Location Protocol, a framework for verifiable geospatial attestations. By aggregating and standardizing attestations across multiple blockchains and storage solutions, it simplifies the development of decentralized geospatial applications.

- **Capabilities:**
  - Provides a standard API for querying location proof attestations.
  - Enables interoperability between different decentralized network systems.
  - Supports multi-blockchain verification mechanisms.
  - OGC-compliant, allowing for integration with existing geospatial standards.

- **How it fits in:**
  - Acts as the core infrastructure query layer for decentralized proof-of-location applications.
  - Enables developers to easily integrate location verification into their decentralized applications.

### 5. SDK: Tools for Location Proof Integration

The **[SDK](https://github.com/DecentralizedGeo/astral-sdk)** provides developers with tools for integrating Astral-compatible location proofs into applications. It supports issuing, formatting, and verifying location attestations in alignment with the Astral Location Protocol.

- **Capabilities:**
  - Offers utilities to interact with location proof APIs.
  - Facilitates generation and validation of geospatial attestations.
  - Built to streamline onboarding to the broader decentralized location proof ecosystem.

- **How it fits in:**
  - Enables developers to add location verification features with minimal setup.
  - Helps standardize proof-of-location workflows across multiple apps and services.

### 6. spatial-sol: Geospatial Computation for Smart Contracts

**[spatial-sol](https://github.com/DecentralizedGeo/spatial-sol)** is a Solidity library for performing geospatial calculations directly within EVM-compatible smart contracts. It provides the foundational math and geometry tools necessary to reason about spatial relationships on-chain.

- **Capabilities:**
  - Implements core geospatial functions (e.g., point-in-polygon, distance checks) in Solidity.
  - Enables smart contracts to interact with geospatial data natively.
  - Useful for applications that rely on real-time or rule-based location logic on-chain.

- **How it fits in:**
  - Acts as the building block for integrating geospatial reasoning into decentralized applications.
  - Supports location-aware dApps and contracts without needing to offload computation to external services.

### 7. Decentralized Location Logger: Log verifiable geotagged records

The **[Decentralized Location Logger](https://github.com/DecentralizedGeo/astral-logbook)** enables users to record, store and verify location data using blockchain and decentralized storage. Built on top of Astrals Location Protocol, this tool is particularly useful for creating **tamper-proof** geospatial records, essential for use cases such as environmental monitoring, supply chain tracking, and disaster response.

- **Capabilities:**
  - Allows users to record geotagged entries with content as location proof attestations.
  - Attached content is stored on IPFS/Filecoin, ensuring availability and verifiability.
  - Explore an interactive map of entries.

- **How it fits in:**
  - Provides an open and censorship-resistant way to track and verify geospatial events.
  - Enables individuals and organizations to create immutable location-based records.

## The Broader Ecosystem

The success of the decentralized geospatial ecosystem is driven by the contributions of developers, researchers, and community members who are exploring new ways to leverage these tools. Here's a few of community-led initiatives and projects that are pushing the boundaries of decentralized geospatial technologies:

[Devonian](https://www.linkedin.com/company/devonian) is a research and development group advancing verifiable geocompute for environmental data by leveraging decentralized, permissioned IPFS‐based workflows. Their flagship product, [Cherty](https://home.cherty.io/), provides a platform for securely publishing, exchanging, and validating geospatial models and data, ensuring greater transparency and trust in environmental and resource monitoring applications.

[FOAM](https://www.foam.space/) is building decentralized geospatial infrastructure with a focus on privacy-preserving and open location protocols. Their work spans proof-of-location standards, open maps, and geospatial registries for Web3 ecosystems.

[Proximum](https://www.proximum.xyz/) is exploring new ways to generate and verify location claims using zero-knowledge proofs and decentralized identifiers (DIDs). Their research bridges technical advancements in privacy and location-based trust systems.

[Hivemapper](https://docs.hivemapper.com/) is a decentralized, user-owned mapping network where contributors use dashcams to map the world and earn tokens. Their platform combines crowdsourced data collection with AI-powered map generation.

[dClimate](https://www.dclimate.net/) is a decentralized network for climate data, forecasts, and models. By making environmental data open, transparent, and tamper-resistant, they’re helping build more resilient systems for everything from agriculture to disaster planning.

## The Road Ahead

The decentralized geospatial web is still evolving, and these tools represent just the beginning of what’s possible. With continued innovation, we anticipate:

- Defining and implementing OGC standards.
- Greater adoption of proof-of-location frameworks.
- Integration with emerging Web3 technologies like Zero-Knowledge Proofs for privacy-preserving location verification.
- Extending the ecosystem with new tools and applications that leverage decentralized geospatial data.

If you're interested in contributing, exploring, or building on top of these tools, we invite you to check out the [DecentralizedGeo Hub](https://decentralizedgeo.github.io/DecentralizedGeo-hub/) and get involved in shaping the future of decentralized geospatial technology.
