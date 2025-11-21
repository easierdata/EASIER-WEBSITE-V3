---
title: Preserving Proof - Integrating Decentralized Storage with Location Protocol in Proofmode

layout: post

date: 17, November 2025

author: Seth Docherty

sub_heading: ""

tags:
  - Astral

  - Easier

  - Proofmode

  - Location Protocol
  
  - Proofs
---

# Preserving Proof - Integrating Decentralized Storage with Location Protocol in Proofmode

Journalists documenting conflict zones need to prove where evidence was captured. Climate researchers tracking deforestation require verifiable location data. Communities establishing land rights depend on immutable geographic records. The capability to create “proofs” from captured media is front and center in [Proofmode](https://proofmode.org/), an open-source mobile application that verifies the provenance of photos and videos. In Proofmode, media can be captured or analyzed using multiple layers of its immutable metadata. The integrity of the media is ascertained by generating “proof artifacts”. These artifacts include hardware fingerprinting, cryptographic signing, and third-party notaries, which are combined into a “proof” allowing anyone to [verify](https://proofmode.org/verify/) the authenticity of the selected media.

While the metadata acts as contextual “proof” of the content, is the content and context itself reliable? How do you decide who and what to trust? With the [rise in “AI Slop”](https://www.npr.org/2025/08/28/nx-s1-5493485/ai-slop-videos-youtube-tiktok), our media environment is slowly degrading, blurring the lines between [what is genuine or deceptive](https://mashable.com/article/fake-hurricane-milton-ai-images-real-consequences). The trustworthiness of content itself remains a vital concern.

To enhance trust and provenance, we’ve collaborated with the [Guardian Project](https://guardianproject.info/) team to integrate the [Location Protocol Framework](https://spec.decentralizedgeo.org/) to strengthen the integrity of the geospatial context and to support storing proofs on [Filecoin](http://filecoin.io) directly from within the Proofmode app. In addition to Filebase, we’ve added support for [Storacha](https://storacha.network/), a decentralized content-addressable storage service that uploads data to Filecoin. Furthermore, through use of the Location Protocol Framework, users of Proofmode can leverage the [Ethereum Attestation Service](https://attest.org/) (EAS) to make tamper-evident, independently verifiable assertions regarding the location data associated with their proofs. This combination of decentralized infrastructure significantly enhances data integrity, immutability, veracity, and trust.

Following a brief mention of our development efforts in a [previous post](https://easierdata.org/updates/2025/2025-09-15-location-protocol-demo-apps#proofmode-android-app), this article will detail the integration process. This includes explaining how the technical challenge of integrating Node.js into the Proofmode Android app was overcome and outlining the architectural strategy for uploading proofs to IPFS and Filecoin, as well as for submitting location attestations from the generated proofs.

## Proofmode Proofs and the Role of Decentralized Storage

A Proofmode proof set, or "bundle" (a .zip archive), is a self-contained collection of files and metadata created during a specific act of media capture (typically a photo or video). Its purpose is to preserve the integrity of the captured media and all associated data, enabling easy transfer, verification, and sharing.

### Key Proof Artifacts

Each proof set contains an event log made up of the following core “artifacts,” which are used to verify the location, time, and source of the media:

1. The original media file (e.g., JPG photo, MP4 video).  
2. JSON and/or CSV metadata files documenting:  
   - Timestamps  
   - Device and hardware fingerprints  
   - Geolocation data (GPS)  
   - Network/environmental data (WiFi, cellular)  
   - Capture context (e.g., sensor readings, user notes)  
   - Cryptographic hash of the original media file  
3. Third-party notary receipt from [OpenTimestamps](https://opentimestamps.org/)  
4. Digital signature files signed with an OpenPGP signer key  
5. Public key of the signer for verification

### Leveraging Decentralized Storage for Persistence

To prevent loss, censorship, and vendor lock-in associated with centralized systems, decentralized storage allows Proofmode users to retain full control over their proofs. This makes every proof artifact fully portable and accessible from anywhere via a [content identifier](https://docs.ipfs.tech/concepts/content-addressing/) (CID) that points to the content itself. Proofs can be retrieved by [retrieving from an IPFS node](https://docs.ipfs.tech/quickstart/retrieve/) or through an [IPFS HTTP Gateway](https://docs.ipfs.tech/concepts/ipfs-gateway/).

Storacha is a decentralized storage service that serves data via IPFS and backs data up to Filecoin, offering a distinct advantage in scalability and persistence. It provides fast, "hot storage" retrieval using the IPFS network while guaranteeing long-term "*cold storage*" on the Filecoin network. Storacha achieves this persistence by managing Filecoin "[deals](https://docs.filecoin.io/storage-providers/filecoin-deals/storage-deals)" and ensuring enrolled storage providers continuously and cryptographically [prove ongoing custodianship](https://spec.filecoin.io/#section-algorithms.pos) of the data.

## Using Proof Sets Alongside the Location Protocol

The Location Protocol enriches the emerging decentralized geospatial web by incorporating established geospatial standards. It provides a common format for portable, signed records of spatial information—coordinates, boundaries, imagery, and other geospatial data—that work across decentralized and conventional systems. The goal is to make it easier to create and share geographic data in a decentralized manner while bringing verifiability, transparency, and trust to spatial information.

By integrating the Location Protocol framework into Proofmode, a proof set becomes the foundation for generating portable, standardized location claims. The GPS coordinates contained within the Proof set are transformed into cryptographically signed location attestations, immutable on-chain assertions registered using EAS, or kept as signed off-chain records. Using Storacha for decentralized storage of proof artifacts, the media evidence is linked and directly referenced in the location claim, guaranteeing availability, verifiability, and auditability for all downstream users and independent third parties.

To illustrate this concept, a proof set is defined within the location payload schema as follows:

```TypeScript
const locationPayload = [  
  { name: "eventTimestamp", value: 1729545600, type: "uint256" },  
  { name: "srs", value: "EPSG:4326", type: "string" },  
  { name: "locationType", value: "geojson-point", type: "string" },  
  { name: "location", value: '{"type":"Point","coordinates":[-71.1061694,42.3576967]}', type: "string" },  
  { name: "recipeType", value: ["Proofmode"], type: "string[]" },  
  { name: "recipePayload", value: ["bafkreiabc123..."], type: "string[]" },  
  { name: "mediaType", value: ["image/jpeg"], type: "string[]" },  
  { name: "mediaData", value: ["bafkreiabc123..."], type: "string[]" },  
  { name: "memo", value: "Proofmode v2.6.0-RC-1 autogenerated=true", type: "string" }  
];
```

In the example above, the [proof metadata](https://docs.google.com/spreadsheets/d/10_xS2DZ8tX1A0jyxvFwmD8TYANb6Wmkrw89Lvjs01Bk/edit?gid=0#gid=0) was mapped to the corresponding protocol fields. A crucial element to note is that when the proof set is uploaded to Storacha, both the proof set and its artifacts generate a CID that is then integrated into the location payload:

1. The CID of the proof set is mapped to the **recipePayload** field, with the **recipeType** set to *Proofmode*.  
2. The CID of the media file is mapped to the **mediaData** field, with **mediaType** set to the file’s format.

Using services like the [Astral API](https://docs.astral.global/api/getting-started), these location attestations become easily queryable records that can be used in tandem with Proofmode’s [ProofCheck web app](https://check.proofmode.org/) to retrieve the proof bundle from IPFS and verify its authenticity via its CID. By combining cryptographically signed location attestations with storage on IPFS and Filecoin, the complete proof bundle remains immutable, accessible, verifiable, and persistent within decentralized infrastructure.

To facilitate storing proofs on Storacha and creating location attestations, we built a bridge between the Proofmode Android app and the Node.js runtime. This allows us to use JavaScript-based libraries that don’t have native Android versions, allowing the integration of the [Storacha JS Client](https://github.com/storacha/upload-service/),  [Astral SDK](https://github.com/DecentralizedGeo/astral-sdk), and [Location Protocol](https://easierdata.org/updates/2025/2025-05-19-location-protocol-spec) framework into Proofmode. As a result, users can store their proofs on Filecoin and generate both on-chain and off-chain location attestations that are queryable, verifiable, and securely stored on decentralized networks.

## Integrating JavaScript SDKs with Native Android

The primary technical obstacle of implementing the Location Protocol framework into Proofmode was integrating our TypeScript-based reference implementation into a native Android application.

The [Astral SDK](https://github.com/DecentralizedGeo/astral-sdk), which manages the creation of location attestations and their registration on the Ethereum blockchain via the [EAS SDK](https://github.com/ethereum-attestation-service/eas-sdk), is written entirely in TypeScript and distributed via npm. However, Android development relies on Kotlin and the Android SDK, and there are currently no native mobile libraries available for the EAS SDK.

### Nonviable Traditional Solutions

We considered two traditional approaches to bridge this technology gap, neither of which proved feasible:

1. **Rewrite SDKs in Kotlin:** This would involve a massive undertaking to port complex cryptographic and blockchain functionality from TypeScript to Kotlin, requiring the reimplementation of critical features and ensuring feature parity.

2. **Rebuild Proofmode in a Cross-Platform Framework:** Shifting to a framework like React Native would mean abandoning the existing native Android architecture.

### The Constraint: Proofmode's Native Dependencies

Proofmode’s architecture relies heavily on deep access to the Android SDK for critical functions such as media capture, sensor fusion, device integrity checks, and cryptographic operations. The app's proof generation process is tightly integrated with device-level capabilities that JavaScript runtimes cannot reliably replicate. Specifically, cross-platform frameworks like React Native cannot provide the level of device fingerprinting and sensor access required by Proofmode's verification model. Given these deep dependencies and the monumental effort required to rewrite the codebase, neither traditional option was practical.

The solution was to incorporate the existing npm packages directly into the native Android environment without compromising the app's essential native capabilities.

## Node.js Mobile: Embedding Node.js in Native Apps

[Node.js Mobile](https://nodejs-mobile.github.io/) is a specialized port that embeds the complete Node.js runtime directly within native Android and iOS applications. Instead of relying on translation or cross-compilation, this framework enables the execution of standard npm packages alongside native code (Kotlin or Swift).

The architecture uses HTTP-based communication between Android and JavaScript layers, creating a bridge that maintains clear separation while enabling bidirectional data flow.

<div style="text-align: center; margin: 2em 0;">
  
```{mermaid}
flowchart TD
    AndroidApp([Android ProofMode App]) --> NodeBridge[NodeJsBridge Manager]
    NodeBridge --> StartNode{Start Node.js?}
    StartNode -->|Success| JSRuntime[<b>JavaScript Runtime</b><br/><i>Starts HTTP Server on localhost:3000</i>]
    StartNode -->|Failed| AndroidFallback[Android-Only Mode]
    JSRuntime --> ConnectionMgr[<b><u>Connection Manager Bridge</u></b><br/>Request Router]

    subgraph AndroidManagers ["<b><em>Android Layer</em></b>"]
        AM1[<b>MediaWatcher.java</b><br/>Proof Generation Module]
        AM2[<b>LocationAttestationManager.kt</b><br/> Proof Artifact Location Data]
        AM3[Manage UI Updates and User Notifications from Responses]
        AM4[<u><b>NodeJsBridge.kt</b></u><br/>Communication Bridge]
    end

    subgraph JSCounterparts ["<b><em>JavaScript Layer</em></b>"]
        JS1[<b>main.js</b><br/>HTTP Server & Routing]
        JS2[<b>locationAttestation.js</b><br/>Astral SDK Library]
        JS3[<b>storachaService.js</b><br>Storacha upload-service Library]
        JS4[<u><b>NodeJsBridge.js</b></u><br/>Connection Manager]
    end

    ConnectionMgr --> Routes{Request Type}
    Routes -->|Location Payload| LocationAPI["/create-location-attestation"]
    Routes -->|Proof Set | StorachaAPI["/storacha/upload"]
    StorachaAPI -->JS3
    LocationAPI --> JS2
    JS1 --> Response[HTTP Response]
    JS2 --> Response
    JS3 --> Response
    Response --> AM3--> AndroidManagers 

    AM1 -.->|Proof Set| AM4
    AM2 -.->|Location Payload| AM4
    AM4 -.->|HTTP Calls| ConnectionMgr
    JS4 -.-> JS1

    AndroidManagers ~~~ JSCounterparts
    style AndroidApp fill:#90EE90
    style JSRuntime fill:#FFD700
    style ConnectionMgr fill:#87CEEB
    style AndroidFallback fill:#FFA07A
    style Response fill:#98FB98
    style NodeBridge fill:#DDA0DD
    style Routes fill:#87CEEB
```

<p class="diagram-caption">
  📌 <strong>Interactive Diagram:</strong> Use mouse wheel to zoom in/out and click & drag to pan around the architecture
</p>

</div>

### Bridge Architecture and Communication Flow

On app startup, native Kotlin code initializes the Node.js runtime through a JNI (Java Native Interface) bridge implemented in C++. The Node.js layer starts an HTTP server on `localhost:3000`, creating a local API accessible only to the Android application.

Android managers send HTTP requests to specific endpoints. `LocationAttestationManager.kt` handles location attestations by sending POST requests to `/create-location-attestation`. Here's the Android-side implementation:

```TypeScript
val locationData = JSONObject().apply {
    put("location", geoJsonFeature)
    put("locationType", "geojson-point")
    put("srs", "EPSG:4326")
    put("memo", "Proofmode v2.6.0-RC-1 autogenerated=false")
    put("chainId", 11155111) // Sepolia testnet
}

val response = httpClient.post("http://localhost:3000/create-location-attestation") {
    contentType(ContentType.Application.Json)
    setBody(locationData.toString())
}
```

The Node.js layer receives requests through a connection manager that handles queuing, retry logic, and error handling. Requests route to JavaScript modules that wrap attestation functionality. The `locationAttestation.js` module interfaces with the Astral SDK:

```TypeScript
const { AstralSDK } = require('@astral-protocol/sdk');

async function createLocationAttestation(locationData) {
  const astral = new AstralSDK({
    provider: ethereumProvider,
    chainId: locationData.chainId
  });

  const unsignedProof = await astral.buildLocationProof({
    location: locationData.location,
    locationType: locationData.locationType,
    srs: locationData.srs,
    memo: locationData.memo
  });

  const onchainProof = await astral.registerOnchainLocationProof(unsignedProof);
  
  return {
    uid: onchainProof.uid,
    transactionHash: onchainProof.txHash,
    timestamp: onchainProof.timestamp
  };
}
```

The JavaScript function executes Astral SDK methods—building location proofs, signing them cryptographically, submitting blockchain transactions—then returns attestation data via HTTP response to Android.

### Design Considerations

Implementing this bridge required careful decisions about operation placement:

**Android-side operations:**

- GPS data collection and sensor fusion  
- Media file management and metadata extraction  
- UI updates and user notifications (toast messages)  
- Device integrity checking and fingerprinting

**Node.js-side operations:**

- Blockchain transaction signing and submission  
- Astral SDK and EAS interaction  
- Cryptographic operations requiring npm packages  
- Storacha interface for uploading proofs

Data is serialized into JSON payloads that flow bidirectionally across the HTTP boundary. The connection manager implements robust error handling, including retry logic for failed blockchain transactions and network interruptions. If Node.js runtime initialization fails—due to corrupted assets or memory constraints—Proofmode falls back to "Android-Only Mode," continuing to function without any of the Node.js-side operations.

This architecture delivers key advantages:

- **Direct TypeScript library usage** without code translation  
- **Single blockchain logic codebase** shared across platforms  
- **Simple SDK updates** via npm package management  
- **Access to npm ecosystem** for additional functionality  
- **Platform extensibility** to iOS using the same pattern

The main implementation challenge involved managing bidirectional messaging: ensuring data serialization correctness, handling thread asynchronicity to prevent UI blocking, and implementing robust error handling across HTTP boundaries.

## Creating Location Attestations: End-to-End Workflow

With the bridge operational, creating location attestations becomes straightforward for users while maintaining technical complexity underneath.

### User Experience

1. User captures photo or video in Proofmode  
2. App automatically collects sensor data: GPS coordinates, timestamp, device info, network information  
3. Proof bundle is automatically uploaded to IPFS (via settings or per-capture)  
4. User opts to create location attestation  
5. App transforms proof set metadata into a [location payload](https://spec.decentralizedgeo.org/introduction/core-concepts/#core-terminology)  
6. Location attestation created on EAS blockchain, with reference to the CID of the proof  
7. Location attestation can be shared via UID, queryable from the Astral API and EAS Explorer  
8. Complete proof bundle can be shared via CID, retrievable from IPFS

### Technical Implementation

The workflow involves multiple system layers coordinating data flow:

1. **MediaWatcher.java** detects new media capture and triggers proof generation  
2. **LocationAttestationManager.kt** retrieves GPS coordinates and constructs the Location Protocol payload according to the [Location Protocol schema](https://spec.decentralizedgeo.org/specification/schemas/):

```TypeScript
const locationPayload = [
  { name: "eventTimestamp", value: 1729545600, type: "uint256" },
  { name: "srs", value: "EPSG:4326", type: "string" },
  { name: "locationType", value: "geojson-point", type: "string" },
  { name: "location", value: '{"type":"Point","coordinates":[-71.1061694,42.3576967]}', type: "string" },
  { name: "recipeType", value: [], type: "string[]" },
  { name: "recipePayload", value: [], type: "bytes[]" },
  { name: "mediaType", value: ["image/jpeg"], type: "string[]" },
  { name: "mediaData", value: ["bafkreiabc123..."], type: "string[]" },
  { name: "memo", value: "Proofmode v2.6.0-RC-1 autogenerated=false", type: "string" }
];
```

1. HTTP POST request sent to Node.js bridge at `/create-location-attestation`  
2. Node.js calls Astral SDK's `buildLocationProof()` to create an unsigned proof structure  
3. Astral SDK formats proof according to EAS schema specifications  
4. `registerOnchainLocationProof()` submits blockchain transaction to EAS contracts  
5. Transaction confirmed on selected network (Sepolia, Base, Arbitrum, or Celo)  
6. Attestation UID and transaction hash returned to Android  
7. Android layer manages UI Notification with link to view Location attestation on EAS Explorer.

The Location Protocol payload structure includes several key components:

- **eventTimestamp**: Time the attested event occurred  
- **srs**: Spatial reference system (coordinate system)  
- **locationType**: Format of location data (geojson-point, coordinates-decimal, WKT, H3)  
- **location**: Geographic coordinates or spatial data  
- **recipeType/recipePayload**: Optional verification methods (location proofs)  
- **mediaType/mediaData**: Attached media files (typically IPFS CIDs)  
- **memo**: Human-readable context or metadata

Once created, location attestations are publicly queryable. Users can view attestations on [easscan](https://sepolia.easscan.org) by navigating to `https://<network>.easscan.org/attestation/view/<uid>` (replacing `<network>` with the blockchain network `<uid>` with the attestation identifier). The Astral API provides programmatic access for querying attestations by attester address, location bounds, timestamp ranges, and other filters.

The Astral SDK handles multi-chain complexity, supporting both offchain attestations ([EIP-712](https://eips.ethereum.org/EIPS/eip-712) signatures without gas costs) and onchain attestations (immutable blockchain records). Proofmode uses onchain attestations to provide the strongest guarantees of verifiability and durability.

## Real-World Applications

Location attestations integrated with decentralized storage enable practical applications across multiple domains.

### Disaster Documentation and Relief

Proofmode was deployed during [Hurricane Otis relief efforts](https://proofmode.org/blog/hurricane-otis-proofmode) in Acapulco, Mexico. Volunteers documented disaster damage to support insurance claims and coordinate relief efforts. Location attestations strengthen this work by providing cryptographic proof of where damage occurred, when documentation happened, and who created the records. Decentralized storage ensures evidence remains accessible even when local infrastructure fails. Third parties can verify claims without requiring trust in the documenting organizations.

### Journalism and Human Rights Documentation

During the [2024 US Election](https://proofmode.org/blog/proofmode-us-election-2024), Proofmode provided a verifiable camera app for documenting polling locations and election-related events. Journalists and activists working in conflict zones or documenting human rights violations can create verifiable evidence with location attestations. The Location Protocol enables building geographic timelines of events that can be independently verified. Decentralized publication prevents censorship or tampering by hostile actors.

### Environmental Monitoring and Climate Science

The [Baseline Earth project](https://proofmode.org/earth) encourages creating verifiable records of natural resources before disasters or environmental changes occur. Researchers documenting deforestation, wildlife populations, or ecological degradation can now create location-verified observations persisting on decentralized storage. This supports longitudinal studies and open science by enabling third-party verification of field data collection without requiring access to institutional databases.

### Indigenous Land Rights and Community Documentation

Communities can create immutable records of land use, cultural sites, and resource extraction activities. Location attestations provide cryptographic proof for legal proceedings. The Location Protocol's standardized formats ensure data interoperability across legal and technical systems. Decentralized storage reduces dependency on institutional servers that may be hostile to indigenous sovereignty claims or subject to data loss.

### Scientific Field Research

Researchers conducting field observations can create verifiable data collection records with precise location information, timestamps, and sensor context. This addresses reproducibility challenges in field sciences and supports open science initiatives by making verification data publicly accessible. The combination of location attestations and decentralized storage creates infrastructure for scientific data provenance that persists beyond individual research projects or institutions.

These applications share common requirements: trustworthy location data, persistent accessibility, and verification without centralized intermediaries. The integration of the Location Protocol framework into Proofmode, supported by decentralized storage services like Storacha, provides this infrastructure.

## Building Toward a Decentralized Geospatial Web

In supporting the Guardian Project’s mission, this work advances the Location Protocol and decentralized geospatial web: geographic data that is verifiable, transparent, accessible, and portable without centralized gatekeepers.

Leveraging the Node.js Mobile toolkit was a critical design decision in integrating the TypeScript-based libraries initially built for the Location Protocol framework directly into the native Proofmode Android application. This strategy allowed us to utilize the NPM ecosystem for the required TypeScript packages while preserving the existing business logic, eliminating the need for costly rewrites in Kotlin or other languages. By creating a communication bridge between native Kotlin code and the Node.js runtime, we added support for Location Protocol-compliant attestations and storing proofs on Filecoin. Moreover, this approach is not limited to Android. Creating a Swift communication bridge, we’d be able to reuse the same JavaScript code, enabling the same capabilities in the Proofmode iOS app.

For Proofmode users, location attestations transform GPS coordinates from device metadata into immutable, verifiable location claims that can be confirmed by anyone. Combined with decentralized storage on IPFS and Filecoin, users have tools for creating trustworthy evidence where trust is most needed. They can verify the integrity of a proof using the bundled artifacts with apps like [ProofCheck](https://check.proofmode.org/), where they can enter the proof bundle's CID to retrieve its content from IPFS and verify its authenticity. Services like the [Astral API](https://docs.astral.global/api/getting-started) act as a gateway to access location attestations from multiple blockchains, enabling geospatial analysis of proofs generated with Proofmode.

Imagine activists using Proofmode to archive events as they unfold, creating cryptographically signed location attestations of where it was captured, anchoring them on the blockchain, and storing the captured content on decentralized storage like IPFS for accessibility and Filecoin for resiliency. This process captures trustworthy provenance metadata alongside the raw media content, enabling tamper-proof verification of each capture’s authenticity and geospatial origin. Journalists and analysts can use tools like ProofCheck to validate the integrity and legitimacy of submitted media, while services such as the Astral API provide seamless access to amassed location attestations across blockchains for comprehensive geospatial analysis.

By validating the authenticity and origin of contributed footage, journalists can effectively filter out "[information pollution](https://en.wikipedia.org/wiki/Information_pollution)." Visual analysis of this validated footage, used as a data layer on a map alongside external sources, can reveal spatial relationships and confirm the unfolding of genuine events. The aggregation of trusted insights provides news agencies with reliable evidence to make informed decisions and respond quickly to escalating situations, all without dependence on centralized authorities.

Developers can explore Proofmode's codebase at [gitlab.com/guardianproject/proofmode](https://gitlab.com/guardianproject/proofmode/proofmode-android) and our implementation at [gitlab.com/SethDocherty/proofmode-android](https://gitlab.com/SethDocherty/proofmode-android/-/tree/storacha-integration?ref_type=heads). Learn more about the Decentralized Geospatial Collaborative at [decentralizedgeo.org](https://decentralizedgeo.org/), the Astral SDK at [github.com/DecentralizedGeo/astral-sdk](https://github.com/DecentralizedGeo/astral-sdk), and the Location Protocol framework at [spec.decentralizedgeo.org](https://spec.decentralizedgeo.org/). The architecture is open source, so we welcome contributions from developers and feedback. Do you have any ideas or use cases, or looking to adapt the Location Protocol framework? Let us know by joining our [Telegram community](https://t.me/+UkTOSXnDcDM5ZTBk) or by [email](mailto:toshan@umd.edu), and we’d be happy to collaborate as we continue building tools for the decentralized geospatial web.  
