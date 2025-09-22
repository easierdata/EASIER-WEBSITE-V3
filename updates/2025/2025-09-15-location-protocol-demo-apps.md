---
title: Using the Location Protocol to Decentralize and Verify Geospatial Data - Three Demonstrative Applications

layout: post

date: 15, September 2025

author: Seth Docherty

sub_heading: ""

tags:
  - Astral

  - Easier

  - Apps

  - Location Protocol
---

# Using the Location Protocol to Decentralize and Verify Geospatial Data: Three Demonstrative Applications

Reliable digital location information is foundational to scientific research, news reporting, and many online services. Yet, traditional methods for sharing and verifying this data fall short. Too often, location records are easy to alter, hard to trace, and siloed within single apps. The location protocol intends to close these gaps. It sets out a standard approach for recording, authenticating, and exchanging “location claims”—assertions linking events or observations to specific places.

## Building Integrity, Trust, and Provenance into the Decentralized Geospatial Web

We designed the [Location Protocol](https://spec.decentralizedgeo.org/) to increase trust in location information by formalizing a simple yet powerful primitive: a location claim. These important digital artifacts define a format for apps and devices to represent spatial information, enhanced through digital signatures and cryptographic protocols.

Location claims inherit several key properties when used within the Web3 paradigm. Specifically, these claims become tamper-evident and independently verifiable through consensus, benefiting from decentralized trust models instead of relying on a single authority. The integrity, authenticity, and provenance of the geospatial data can be validated by any participant, with records potentially being anchored in a distributed ledger.

This post highlights applications and use cases of the Location Protocol to demonstrate some of these advantages. In particular, when multiple applications and services are capable of reading and verifying location claims, it increases transparency and interoperability, building confidence in location data across the entire ecosystem.

## 1. Astral Logbook

The [Astral Logbook](https://logbook.astral.global/) is akin to a journal for physical events. For example, the value of the Astral Logbook lies in its documentation: your entry isn’t just a story, it’s anchored to the actual places you were. Think of researchers, travelers, or field workers being able to say: “Yes, **I*** collected **this** observation **there**, here is some supporting **evidence**.” The Astral logbook achieves this by allowing users to claim ownership of assertions they submit and any associated data. Assertions, represented as submitted entries, are tied to a [Web3 wallet](https://www.miniorange.com/blog/web3-authentication/), a digital key that represents identity, and any attached media is uploaded to [Storacha](https://storacha.network/), a decentralized content-addressable storage service for retrieving content via the IPFS network and providing long-term storage on Filecoin.

:::{image} ../../_img/posts/2025-09-15/logbook-map-selection.png
  :alt: Logbook map selection
  :align: center
  :height: 500px

:::

Once logged in, selecting a location on the map opens an entry form where users can attach media, add notes, and then submit. Each submitted “location claim becomes a [location attestation](https://spec.decentralizedgeo.org/introduction/core-concepts/#core-terminology), a digital artifact associated with a cryptographic signature, that’s registered on-chain on the [Ethereum Attestation Service (EAS)](https://attest.org/). Once the submission is finalized and registered on EAS, your assertion of the “location claim” is recorded on a blockchain, and any attached media is stored on Storacha and retrievable on IPFS by its content identifier (CID).

The inherent transparency of the location claim enables anyone to review the details, and the immutable nature of CIDs ensures data integrity of the media file referenced in the location claim. To illustrate this, here's a [link to a sample previously registered entry](https://logbook-git-feat-addingstoracha-astralprotocol.vercel.app/attestation/uid/0x042d6a0675583c41f8425cffcd003371578fe824d819e384463cfca2327e8de9) and the [attached photo](https://bafybeiaefdbedsgtxltubh35kwxjfrpfgjzjeuzcaolzh6ifewgtmklrhq.ipfs.w3s.link/), conveniently retrievable from IPFS, that was snapped while hanging out at one of [Night Shift’s](https://nightshiftbrewing.com/locations/beer-gardens/) beer garden locations. One can verify the location claim by cross-referencing the EXIF data of the image.

:::{image} ../../_img/posts/2025-09-15/logbook-entry-submission.png
  :alt: Logbook entry submission
  :align: center
  :height: 500px

:::

Here's the link to [my registered entry](https://sepolia.easscan.org/attestation/view/0x042d6a0675583c41f8425cffcd003371578fe824d819e384463cfca2327e8de9) which includes the photo I snapped while hanging out at one of Night Shift’s beer garden locations, conveniently uploaded to decentralized networks.

## 2. Proofmode Android App

Imagine you witness a rare species or a serious crime and want to share trustworthy media. Or you file a home insurance claim after a natural disaster and need to provide verifiable evidence of the damage. [Proofmode](https://proofmode.org/) helps you prove the authenticity of your pictures and videos. At the moment of capture, ProofMode strengthens the media's verifiability by adding an extra layer of immutable metadata using the device's sensors, hardware fingerprinting, cryptographic signing, and third-party notaries. When that content circulates, this metadata serves as “proof” of the content, ensuring it hasn’t been tampered with or modified, which helps support the veracity of events at a particular time and place. While this doesn’t resolve all forms of [information disorder](https://shorensteincenter.org/information-disorder-framework-for-research-and-policymaking/#Part_1_Conceptual_Framework), it creates a stronger chain of trust, especially for advocacy, reporting, or documentation in sensitive contexts.

We have been collaborating closely with the [Guardian Project](https://guardianproject.info/) team to integrate the [Location Protocol](https://spec.decentralizedgeo.org/) into the [Proofmode Android app](https://gitlab.com/SethDocherty/proofmode-android/-/tree/nodejs-integration?ref_type=heads). Users can now assert verifiable evidence of the location data associated with their proofs on the blockchain, with the proofs being published and securely stored on IPFS (and soon Filecoin) to ensure data integrity and immutability.

As part of the development effort, we extended the settings menu to let users add their existing wallet IDs, enabling them to submit attestations to EAS. We are currently working on adding support for [Privy](https://www.privy.io/onboarding) and streamlining wallet authentication, particularly for new users, to allow them to create wallets and log in using their email or phone number.

:::{image} ../../_img/posts/2025-09-15/proofmode-wallet-config.png
  :alt: Proofmode settings menu
  :align: center
  :height: 500px

:::

:::{important}
Within the settings menu, users can enable an array of proof options pertaining to the metadata that appears in the generated proof. Depending on the need or use case, enabling more proof options will make the proof metadata more robust. To enable the ability to create location attestations, the “location” option must be enabled in this menu.
:::

Proofs within the Proofmode app are created either by importing existing media from the gallery or by taking a picture within the app, and they can then be shared with others. Users have several sharing options to choose from, but if the proofs include a locational component in proof generation, they can spawn both on-chain or off-chain location attestations. Selecting the on-chain option submits it to EAS linked to you through your wallet ID. The off-chain option saves the location attestation payload to a JSON file, allowing users to choose where and how to submit it—whether through another blockchain solution, a decentralized network, or a private database.

:::{subfigure} AB|AB
  :gap: 8px
  :subcaptions: above
  :name: proofmodeShare

  ```{image} ../../_img/posts/2025-09-15/proofmode-share-proof.png
    :align: left
    :class: side-by-side-images
    :height: 700px
  ```

  ```{image} ../../_img/posts/2025-09-15/proofmode-proof-attestation.png
    :align: right
    :class: side-by-side-images
    :height: 700px
  ```

:::

Once the submission is complete, users can view the [resulting location attestation on EAS](https://sepolia.easscan.org/attestation/view/0x9fe99608e639afc71e5195c5c065aa0a58a1e23954190ca9523548a39d9456e1). From there, they can share this attestation, which functions as:

- An added layer of validation, like a receipt, for the proof metadata.
- A reference to the CID of the proof itself, enabling retrieval from decentralized networks.

In many cases, the geospatial metadata is just as crucial as the visual evidence itself, but current systems for storing and verifying this data are often fragmented, insecure, or controlled by centralized providers. Our aim is to support Guardian Project's mission to build trust and enhance digital resilience by providing necessary standards and components (i.e, Location Protocol and location attestations) to generate decentralized mechanisms for spatial data creation and consumption that increase integrity, provenance, and trust.

## 3. Astral MCP Agent

The [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), or MCP, acts as a universal adaptor that allows AI assistants to work efficiently with data, tools, and services in a consistent and organized manner. APIs are ideal for this protocol because MCP’s standardized framework presents APIs as an easy-to-use “plug and play” interface, eliminating the need for custom integrations or connections. By wrapping the [Astral API](https://docs.astral.global/api/getting-started) into an MCP agent, users can query Location Protocol-compliant attestations across multiple blockchains using natural language, offering a more intuitive experience for data exploration and analysis.

The [Astral MCP agent](https://github.com/DecentralizedGeo/astral-api-mcp) makes it easier to ask meaningful questions and receive reliable answers about where things happen, such as:

- Searching the blockchain for location claims by place, type, or date, just by using everyday questions.
- Analytical work, such as generating maps or analyzing trends in location data, becomes much easier and can even be automated.

Here’s a glimpse of how developers and researchers can explore live attestation data through familiar AI tools, instead of writing custom programs.

<!-- :class-grid: outline -->

:::{subfigure} AB|AB
  :gap: 8px
  :subcaptions: above
  :name: mcpPrompts

  ```{image} ../../_img/posts/2025-09-15/astral-mcp-prompt1.png
    :height: 900px
    :class: side-by-side-images
  ```

  ```{image} ../../_img/posts/2025-09-15/astral-mcp-prompt2.png
    :align: right
    :height: 900px
    :class: side-by-side-images
  ```

  Click on the images to enlarge them for better readability.
:::

Want to try it out for yourself? Import our [python package](https://pypi.org/project/astral-mcp-server/) as an [MCP agent in VSCode](https://code.visualstudio.com/docs/copilot/customization/mcp-servers?originUrl=%2Fdocs%2Fcopilot%2Fcustomization%2Fmcp-servers) and check out our [guide](https://github.com/DecentralizedGeo/astral-api-mcp/blob/main/docs/mcp-tools-guide.md) for more details on the available tools and example prompts to test!

## Why Interoperability is the Key

The real value of the Location Protocol isn’t just what one app can do—it’s what happens when multiple apps can talk the same language about location.

- A photo from ProofMode can be imported into the Logbook, retaining its trusted location stamp, additional metadata, and links to supporting evidence.
- Location claims can be queried with the Astral MCP agent, and the underlying metadata can be used alongside or transferred into other Dapps, keeping the chain of trust intact and valid.
- Across this ecosystem, people and organizations gain a way to verify where something happened, rather than relying solely on a caption or claim.

As the Location Protocol ecosystem expands, its standardized approach enables independent applications, whether centralized or decentralized, to interoperate and exchange spatial data using a common language. This technical interoperability increases confidence in location records by providing verifiable provenance, signed metadata, and portability across platforms—strengthening the reliability and trust of digital location information for a broad range of use cases. Another useful analogy is to think of the Location Protocol as the extension that provides the spatial component in decentralized databases, such as blockchain-based distributed ledgers. For example, each location attestation can be thought of as a row in a larger database, and the location protocol and EAS are the standards in infrastructure that allow the rows to be integrated. Applications such as proof mode provide interfaces to bring it all together and make it easier to contribute important attributes, while the astral API provides a mechanism to query geospatial content that is cryptographically signed.

## Wrapping up

Verification remains a complex challenge, but the Location Protocol offers a practical, extensible framework for recording and exchanging spatial claims with cryptographic integrity. By supporting signed, portable metadata and standardized structures, apps and services such as the Astral Logbook, ProofMode, and Astral MCP agent illustrate how verifiable trust can be rooted in our digital ecosystem from the technical ground up. With the rise of the agent economy, it becomes increasingly possible for misinformed evidence to be placed on a map, and with this new paradigm, it is easier to validate location information because of the inherent transparency and integrity — it becomes straightforward to ask, “Who added this content, and what makes it trustworthy?”
