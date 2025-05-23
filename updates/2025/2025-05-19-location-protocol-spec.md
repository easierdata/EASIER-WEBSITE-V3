---
title: The **Location Protocol** specification - A standardized framework for working with location information on the decentralized web

layout: post

date: 19, May 2025

author: Seth Docherty

sub_heading: ''

tags:

- Astral

- Easier

- Collaboration

---

# The **Location Protocol** specification - A standardized framework for working with location information on the decentralized web

In collaboration with [Astral](https://www.astral.global/), we have been designing a standardized framework for working with location information on the decentralized web. The goal of this work is to enrich the emerging decentralized geospatial web with established geospatial standards, making it easier to create and share geographic data and services in a decentralized manner, but also bringing novel mechanisms for verifiability, transparency, and trust to the web more generally. An initial version of the **Location Protocol** specification is detailed below, including the motivation for the protocol, an outline of the core metadata model, how to use the protocol to record location-based records, and some demonstrations and potential real-word use-cases.

## What is the Location Protocol?

The Location Protocol is an implementation‑agnostic format for encoding, signing, and verifying spatial records both on- and off‑chain. As a general-purpose, open standard for digitally signed spatial records it enables independent applications to interoperatively talk to each other about where things are in space, whether in reference to the Earth's surface, somewhere in the metaverse, or another digital location context. These digitally signed spatial records are versatile, and can represent the location of events, objects, features, and interactions. Further, the Location Protocol is designed to support an extensible range of geospatial feature types, data formats, and location proofs, including formal cryptographic evidence (i.e., from zkmaps or Proximum) and informal supporting media (i.e., photo or video documentation), as well as arbitrary metadata (i.e., additional fields or an attribute table).

Compatible with the [Ethereum Attestation Service](https://attest.org/) (EAS), the Location Protocol provides a standardized way to formulate assertations about a location or geographic feature. More specifically, it allows users to formalize these assertions by creating and signing "*location attestations*" that can be used across different platforms and applications. The location attestation object is a core component of the Location Protocol and is a digitally signed metadata object containing verifiable information about a location and the entity making an attestation.

## Location Protocol Specification

The Location Protocol specification is built around a location attestation object, which is a geospatial data artifact that includes a digital signature verifying its source, structured metadata about location attributes, and potentially some additional supporting fields. At a minimum, a valid location attestation object must include a few [base fields](#base-fields), but can be extended with [composable fields](#composable-fields) to provide more context, and can also leverage [EAS properties](#eas-properties) for additional functionality. Below, an outline is provided for the base fields, which can support many different representations of location information, as well as a description of the composable fields and properties.

### Base fields

The location attestation object at a minimum must contain the fields below in order to identify and represent the location information.

| Field Name | Type | Description |
|------------|------|-------------|
| srs[^1] | `string` | The spatial reference system used to represent the location data. |
| locationType | `string` | The type of location data being represented. |
| location | `string`, `int40[2]`, `int40[2][]`, `int40[2][][]` | The actual location data |
| specVersion | `uint8` | The version of the specification used to generate the attestation. |

[^1]: It is recommended that the `srs` field conforms to EPSG code (e.g. `EPSG:4326`), OGC URN (e.g. `urn:ogc:def:crs:OGC:1.3:CRS84`), or a well-known identifier for the spatial reference system.

#### Supported location types

The `locationType` field identifies the type of location data being represented. The following location types are supported:

| Location Type | Additional Details | Data Type | Example |
|---------------|--------------------|-----------|---------|
| decimalDegrees | Comma separated Latitude and longitude decimal degree coordinates | `string` | `37.7749, -122.4194` |
| dms | Latitude and longitude coordinates in degrees, minutes, and seconds | `string` | `37°46'30.0"N 122°25'10.0"W` |
| scaledCoordinates[^2] | A scaled integer representation of coordinate pairs, representing points lines or polygons | `int40[2]`, `int40[2][]`, `int40[2][][]` | `[[-74000000, 40700000], [-74100000, 40700000], [-74100000, 40800000], [-74000000, 40800000], [-74000000, 40700000]]` |
| geoJson | A GeoJSON object representing a geographic feature as points lines or polygons | `string` | `{ "type": "Point", "coordinates": [ -122.4194, 37.7749 ] }` |
| wkt | A WKT (Well-Known Text) representation of a geometric object as points lines or polygons | `string` | `POINT(-122.4194 37.7749)` |
| placeNames | Known place names | `string` | `San Francisco, CA`, `Eiffel Tower` |
| address | Standard mailing address | `string` | `1600 Amphitheatre Parkway, Mountain View, CA 94043` |
| h3 | A hierarchical hexagonal grid system used for spatial indexing | `string` | `8928308280fffff` |
| geohash | A hierarchical spatial data structure which subdivides space into buckets of grid shape | `string` | `u4pruyd` |
| w3w | A geocoding system that encodes geographic coordinates into three dictionary words | `string` | `apple.banana.orange` |
| mgrs | A military grid reference system used for geospatial referencing | `string` | `33TWN0000000000` |
| utm | A universal transverse mercator coordinate system used for mapping | `string` | `33TWN0000000000` |
| spcs | Comma separated x, y coordinates in a state plane coordinate system | `string` | `2000000, 500000` in a specific state plane zone |

[^2]: It's up to the implementor to set the precision and provide guidance on the default precision to be used. The maximum coordinate precision that can be set is 10⁹ as `int40` can store values up to ±549,755,813. For example, a coordinate of `123.456` with a precision of 10¹⁰ would exceed the maximum value of `int40` and would not be valid.

The `location` value is interpreted based on the `locationType` field. Implementations should not attempt to decode `location` without first resolving `locationType`.

### Composable fields

A location attestation object can be extended by additional fields that describe, support, or verify different aspects of the encoded location information. These composable fields can be grouped by (a) "common fields" and (b) "proof fields", which can each be thought of as sub-objects.

#### Common fields

The location attestation object supports additional fields that may be common to most location attestations but are still optional. These fields provide additional information about the context of an attestation, such as a textual description (i.e., "memo"), when the location information was recorded (i.e., "eventTimeStamp"), or other values associated with the location (i.e., "attributes"). The composable nature of location attestation objects allow for the inclusion of additional arbitrary fields that may be relevant to specific use cases or applications. The common fields listed below is what's currently recognized by our downstream API.

| Field Name | Type | Description |
|------------|------|-------------|
| media | `bytes`, `mediaType` | bytes array representing the media data associated with the location. The `mediaType` is a MIME-type-style string describing the media data. |
| attributes | `string` | Additional attributes associated with the location. |
| eventTimeStamp | `uint64` | The UNIX timestamp of the event associated with the location record. _Note, this should not be confused with the `time` field that represents when the attestation was created_. |
| eventId | `byte32`, `string` | An external identifier to be used as foreign key to link non-referenced attestations or external sources.  |
| recepient | `address` | The address of the recipient of the attestation. |
| memo | `string` | An arbitrary message or note. |
| ... | `any`[^3] | An arbitrary field to extend the base model. |

[^3]: The `any` type is a placeholder for any arbitrary field, following an [acceptable Solidity ABI](https://docs.attest.org/docs/tutorials/create-a-schema#schema-fields). Learn more about Solidity ABI types and the Contract ABI Specification [here](https://docs.soliditylang.org/en/v0.8.16/abi-spec.html).

#### Proof fields

The location attestation object can include verification fields that can incorporate corroborating evidence to _prove_ the authenticity and integrity of the location information. These fields are optional but recommended for use cases that require a higher level of assurance.

| Field Name | Type | Description |
|------------|------|-------------|
| proof | `byte32` | The proof of the authenticity and integrity of the location data. |
| proofType | `string` | The type of proof used to verify the location data. |
| proofVersion | `uint8` | The version of the proof used to verify the location data. |
| prooverAddress | `address` | The address of the prover who generated the proof. |
| proofTime | `uint64` | The timestamp of when the proof was generated. |

## Working with the location protocol on EAS to create location attestations

### EAS Properties

The Location Protocol is flexible and can be consumed by Ethereum Attestation Service (EAS) using the [EAS SDK](https://github.com/ethereum-attestation-service/eas-sdk) to create, sign, and verify location attestations. The following properties are common to all EAS attestations that are stored on the blockchain (onchain) and off the blockchain (offchain) and are therefore also included as part of the location attestation object. Though largely similar, there are a few small differences between the properties available for creating an attestation and those available when retrieving attestations.

**Properties for creating attestations**

| Property Name | Type | Description | Required |
|---------------|------|-------------|----------|
| schemaString | `string` | The schema string that defines the structure of the data to be attested. | :heavy_check_mark: |
| schemaUID | `byte32` | The unique identifier of the schema associated with the attestation. | :heavy_check_mark: |
| refUID | `byte32` | The reference UID of the attestation, if any. | |
| expirationTime | `uint64` | The Unix timestamp when the attestation expires (0 for no expiration). | |
| recipient | `address` | The address of the recipient of the attestation. | |
| time | `uint64` | The UNIX timestamp of when the attestation was created. _(offchain only)_ | :heavy_check_mark: |
| revocable | `bool` | A boolean indicating whether the attestation is revocable or not. | |
| data | `bytes` | The location attestation object. | :heavy_check_mark: |
| value | `uint256` | The ETH value that is being sent with the attestation. _(onchain only)_ | |

The `schemaString` and `schemaUID` properties are used to define the structure of the data being attested to, while the `refUID` property is used to link attestations together. The `expirationTime` property is used to set a time limit on the validity of the attestation, while the `recipient` property specifies who will receive the attestation. Once an attestation is created, it is signed and stored on the blockchain, returning a UID representing the created attestation.

**Properties when retrieving attestations**

An attestation is retrievable by its UID, a 32-byte hash, to identify the attestation on the blockchain. In addition, the following properties are returned when an attestation is retrieved from the blockchain:

| Property Name | Type | Description |
|---------------|------|-------------|
| uid | `byte32` | The unique identifier of the attestation. |
| schemaString | `string` | The schema string that defines the structure of the data to be attested. |
| schemaUID | `byte32` | The unique identifier of the schema associated with the attestation. |
| refUID | `byte32` | The reference UID of the attestation, if any. |
| time | `uint64` | The UNIX timestamp of when the attestation was created. |
| expirationTime | `uint64` | The Unix timestamp when the attestation expires (0 for no expiration). |
| revocationTime | `uint64` | The Unix timestamp when the attestation was revoked, if applicable. |
| recipient | `address` | The address of the recipient of the attestation. |
| attester | `address` | The address of the attester who created the attestation. |
| revocable | `bool` | A boolean indicating whether the attestation is revocable or not. |
| data | `bytes` | The location attestation object. |

<br>

Ultimately, the (an attestation object and location attestation object) is an instance of the more general EAS attestation and extends the data model in order to support the Location Protocol while remaining extremely flexible. The following diagram illustrates the composition of a location attestation object and the relationship of the various fields and properties outlined above:

```mermaid
---
config:
  theme: mc
---
C4Container
    Node(obj, "Attestation Object") {
      Node(attestationProps, "Attestation Properties") {
        System(recipient, "Recipient", "The entity receiving the attestation.")
        System(expirationTime, "Expiration Time", "The time until the attestation remains valid.")
        System(revocable, "Revocable", "Indicates if the attestation can be revoked.")
        System(refUID, "Reference UID", "Unique identifier for the attestation reference.")
        System(schemaUID, "Schema UID", "The schema identifier associated with the attestation")
        System(schemaString, "Schema String", "A string defining the structure of the data to be attested.")

        Node(data, "Data", "Contains the location attestation object.") {
          Node(locationDataContainer, "Location Attestation Object") {
            System(srs, "srs", "The spatial reference system.")
            System(locationType, "Location Type", "The type of location data.")
            System(location, "Location", "The actual location data.")
            System(specVersion, "Specification Version", "The version of the specification.")
            
            Node(systemRef, "Optional fields") {
              System(objectFields, "Common Fields", "Additional commonly supported fields.")
              System(proofFields, "Proof Fields", "Proofs verifying authenticity and integrity.")
            }
          }
        }
      }
    }

    UpdateLayoutConfig($c4ShapeInRow="4")
```

## Creating Location Attestations

Below is an example of how to create location attestation objects using the Ethereum Attestation Service (EAS). It covers the steps to create, sign, and verify location attestations.

## Making an attestation

### Step 1: Identify the schema

The first step in creating a location attestation is to identify the schema defining the data (location attestation object). A schema is a structured framework that outlines the format of the data. A schema string is a string representation of the schema, defined in the following format:

```text
`<dataType> <fieldName>, <dataType> <fieldName>, ...`
```

Where `<dataType>` is the type of data (e.g., `string`, `uint8`, `int40[2]`, etc.) and `<fieldName>` is the name of the field.

A schema in EAS is defined by a schema UID, a 32-byte hash that uniquely identifies the schema on the EAS schema registry.

To create a location attestation, the following example JSON schema can be used:

```json
{
  "schemaComponents": {
    "schemaUID": "0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a",
    "schemaString": "string srs, string locationType, string location, uint8 specVersion"
  }
}
```

The schemaComponents listed above conforms to the base data model for creating location attestation objects and can be viewed on the EAS schema registry [here](https://sepolia.easscan.org/schema/view/0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a).

### Step 2: Prepare a location attestation object

At it's core, an EAS attestation is a formalized assertion or claim about something, in this case a location. This could be a physical address, a GPS coordinate, or some other [form of location data](./location-attestation.md/#supported-location-types). As mentioned above, the `schemaString` defines the structure of the location information that will be encoded and passed into the attestation object. Let's assign some values to the fields in the schema using decimal degrees and a basic reference system conforming to a specific EPSG code:

```json
{
  "locationAttestationObject": {
    "srs": "EPSG:4326",
    "locationType": "decimalDegrees",
    "location": "44.967243, -103.771556",
    "specVersion": 1
  }
}
```

### Step 3: Encode the location attestation object

Before creating an attestation object, a schemaEncoder object is created using the `schemaString` to encode the location attestation object. The encoding process ensures that the data conforms to the structure defined by the schema associated with the attestation. Why is this encoding necessary?

**On-chain Validation**: Smart contracts rely on structured data to verify the integrity and correctness of an attestation. The SchemaEncoder ensures the data adheres to the schema's format, making it possible for on-chain logic (e.g., verification or revocation) to process the data reliably.

**Consistency and Interoperability**: By encoding data according to a defined schema, different systems and parties can interpret and validate the data uniformly, ensuring compatibility across applications and platforms.

We'll take the `locationAttestationObject` and encode it using the `schemaString`. Here's what the encoded location attestation object looks like:

```string
0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000009455053473a343332360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e646563696d616c44656772656573000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001634342e3936373234332c202d3130332e37373135353600000000000000000000
```

> It is possible to verify this encoding with any ETH ABI Decoder tool such as [this](https://adibas03.github.io/online-ethereum-abi-encoder-decoder/decode). Just paste the encoding into the input box and enter the schema field types in the order they appear in the schema string. For example, for the above encoding, you would enter `string, string, string, uint8` as the types.

The encoded `locationAttestationObject` is then passed into the `data` property of the attestation object.

### Step 4: Create the attestation object

The attestation object contains the EAS properties, one of which is the data property that contains the encoded location attestation object. The following illustrates the structure of an attestation object:

```json
{
  "attestation object": {
    "schemaUID": "0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a",
    "schemaString": "string srs, string locationType, string location, unit8 specVersion",
    "recipient": "0x1234567890abcdef1234567890abcdef12345678",
    "data": "encodedLocationAttestationObject"
    }
}
```

After the attestation is signed, submitted and added to the blockchain, a UID is generated that can be used to query the attestation and view it's details. Here is a resultant attestation UID for an attestation that also incorporates the location attestation object from above.

**Attestation UID**: 0x628f06c011351ef39b419718f29f20f0bc62ff3342d1e9c284531bf12bd20f31

**EAS Explorer Link**:  [https://sepolia.easscan.org/attestation/view/0x628f06c011351ef39b419718f29f20f0bc62ff3342d1e9c284531bf12bd20f31](https://sepolia.easscan.org/attestation/view/0x628f06c011351ef39b419718f29f20f0bc62ff3342d1e9c284531bf12bd20f31)

### Example of creating an On-Chain Location Attestation with the EAS SDK

The following TypeScript code snippet demonstrates how to create a location attestation object using the EAS SDK.

```typescript
1    import { EAS, SchemaEncoder } from "@ethereum-attestation-service/eas-sdk";
2
3    const eas = new EAS(EASContractAddress);
4    eas.connect(signer);
5
6    // Initialize SchemaEncoder with the schema string
7    const schemaEncoder = new SchemaEncoder("string srs, string locationType, string location, uint8 specVersion");
8    const encodedData = schemaEncoder.encodeData([
9      { name: "srs", value: "EPSG:4326", type: "string" },
10     { name: "locationType", value: "decimalDegrees", type: "string" },
11     { name: "location", value: "44.967243, -103.771556", type: "string" },
12     { name: "specVersion", value: 1, type: "uint8" },
13   ]);
14
15   const schemaUID = "0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a";
16
17   const tx = await eas.attest({
18     schema: schemaUID,
19     data: {
20       recipient: "0xFD50b031E778fAb33DfD2Fc3Ca66a1EeF0652165",
21       expirationTime: 0,
22      revocable: true,
23      data: encodedData,
24     },
25   });
26
27  const newAttestationUID = await tx.wait();
28
29  console.log("New attestation UID:", newAttestationUID);
```

Line 1 imports the EAS SDK and the SchemaEncoder class. Line 3 creates an instance of the EAS class, which is used to interact with the Ethereum Attestation Service. Line 4 connects the EAS instance to a signer, which is used to sign transactions. Lines 6-13 create a new SchemaEncoder instance with the schema string and encode the location attestation object. Lines 15-25 create a new attestation using the `attest` method of the EAS instance, passing in the schema UID and encoded data. Lines 27-29 wait for the transaction to complete and log the new attestation UID to the console.

## Patterns and strategies demonstrating the use of the Location Protocol

Here are some demonstration examples to illustrate how geographical information can be recorded and integrated into the location protocol and used to make location attestations. We have created some [helper functions](https://github.com/DecentralizedGeo/eas-sandbox) to make it easier to work with EAS and create location attestations. These functions will be incorporated and wrapped up into an SDK.

### 1. Event Check-in using GeoIP

This example demonstrates how location attestations could be used to as a way to verify attendance at an event. The Typescript app uses the device's IP address to record location and create an attestation. This could be used for events like concerts, conferences, or any other event where verifying attendance for an event could be useful. Here, we've extended the base model by incorporating several optional [composable fields](#composable-fields) as well as a custom extensible field. The `eventId` represents a unique identifier for the event, the `eventTimestamp` is the time of the event, and the `ticketId` is a unique identifier for the ticket purchased.

```TypeScript
// 1. Get the provider and signer
const { signer } = getProviderSigner();

// Register schema if not already registered. Will return the schema UID if already registered
const schemaString = "string srs, string locationType, string location, uint8 specVersion, string eventId, uint64 eventTimestamp, string ticketId"
const schemaUID = await registerSchema(signer, schemaString);

// Grab the IP Address of the mobile device and use GeoIP to get the location
const ipAddress = await publicIpv4();
const locationData = geoip.lookup(ipAddress);
const geoJsonPoint = {
    type: "Point",
    coordinates: [locationData.ll[1], locationData.ll[0]]
};
const geoJsonPointString = JSON.stringify(geoJsonPoint);

// Create the attestation object
const attestationObject: OnChainAttestationData = {
  recipient: "0xFD50b031E778fAb33DfD2Fc3Ca66a1EeF0652165",
  revocable: true,
  schemaUID: schemaUID,
  schemaString: schemaString,
  dataToEncode: [
    { name: "srs", value: "EPSG:4326", type: "string" },
    { name: "locationType", value: "geoJson", type: "string" },
    { name: "location", value: geoJsonPointString, type: "string" },
    { name: "specVersion", value: 1, type: "uint8" },
    { name: "eventId", value: "GEO-OPEN-HACK-2025", type: "string" },
    { name: "eventTimestamp", Math.floor(time.getTime() / 1000), type: "uint64" },
    { name: "ticketId", value: "ticket-1234567890", type: "string" }
  ]
};

const newAttestationUID = await createOnChainAttestation(signer, attestationData);
```

### 2. Using a QR code for geocaching

This example demonstrates how a QR codes could be used for geocaching, treasure hunts, or location-based gaming events. The application would first scan a QR code geospatial metadata, formatted according to the Location Protocol, and finally triggering the generation of an attestation on EAS. In this case, the QR code metadata is mapped to the base model field `location` as scaled coordinates and an optional composable field `memo` representing a note or message associated with the geocache. The `eventTimestamp` represents the time of when the QR code was scanned.

```TypeScript
const { signer } = getProviderSigner();

// Register schema if not already registered. Will return the schema UID if already registered
const schemaString: "string srs, string locationType, uint40[2][] location, uint40 specVersion, uint64 eventTimestamp, string memo";
const schemaUID = await registerSchema(signer, schemaString);

// Extract QR code metadata and Create the attestation object
const qrData = await decodeQR(imagePath) // Returns {lat: <latitude coordinate>, long: <longitude coordinate>}
const attestationObject: OnChainAttestationData = {
  recipient: "0xFD50b031E778fAb33DfD2Fc3Ca66a1EeF0652165",
  revocable: true,
  schemaUID: schemaUID,
  schemaString: schemaString
  dataToEncode: [
    { name: "srs", value: "EPSG:4326", type: "string" },
    { name: "locationType", value: "scaledCoordinates", type: "string" },
    { name: "location", value: [qrData.lat, qrData.long], type: "uint40[2][]" },
    { name: "specVersion", value: 1, type: "uint8" },
    { name: "eventTimestamp", value: Math.floor(time.getTime() / 1000), type: "uint64" },
    { name: "memo", value: qrData.note, type: "string" }
  ]
};

const newAttestationUID = await createOnChainAttestation(signer, attestationData);
```

### 3. Preserving and sharing verifed photograph metadata generated by Proofmode

This example demonstrates how the Location Protocol can be used to support the preservation and dissemination of metadata generated by [ProofMode](https://proofmode.org/), a mobile app for capturing verifiable photos. A verified photo from ProofMode includes information about mediaType and media, and location information that can be easily parsed into a Location Protocol compliant attestation for further verification and downstream use. The Location Protocol can extend the capability of applications like ProofMode by incorporating and mapping the verifiable metadata components into the [proof fields](#proof-fields) of a location attestation object. In this case, the `proofType` is set to "ProofMode", and the `proof` field contains the hash of the image file. The `proofTime` represents the time of when the proof was generated. We can also include the composable fields to capture the actual media data, a bytes array representing the media, to the `media` field field, `mediaType` is a MIME-type-style string describing the media data. and the `memo` field contains any additional notes or attributes. The `location` field is set to the location of the photo, and the `eventTimestamp` represents the time of when the photo was taken. This strategy could be particularly valuable for applications requiring verified media evidence, such as journalism, human rights documentation, legal evidence collection, and scientific field research where the authenticity and provenance of media are critical.

```TypeScript
// 1. Get the provider and signer
const { signer } = getProviderSigner();

// Register schema if not already registered. Will return the schema UID if already registered
const schemaString: "string srs, string locationType, string location, uint40 specVersion, uint40 eventTimestamp, string memo, string mediaType, bytes media";
const schemaUID = await registerSchema(signer, schemaString);

// Extract the ProofMode zip file and grab the metadata
const files = extractZipFile(zipFilePath, extractDir);
const proofModeData = getProofModeMetadata(files);

// Create the attestation object
const attestationObject: OnChainAttestationData = {
  recipient: "0xFD50b031E778fAb33DfD2Fc3Ca66a1EeF0652165",
  revocable: true,
  schemaUID: schemaUID,
  schemaString: schemaString,
  dataToEncode: [
    { name: "srs", value: "EPSG:4326", type: "string" },
    { name: "locationType", value: "decimalDegrees", type: "string" },
    { name: "location", value: proofModeData.location, type: "string" },
    { name: "specVersion", value: 1, type: "uint8" },
    { name: "eventTimestamp", BigInt(proofModeData.timestamp), type: "uint64" },
    { name: "memo", value: proofModeData.notes, type: "string" },
    { name: "mediaType", value: proofModeData.mediaType, type: "string" },
    { name: "media", value: proofModeData.media, type: "bytes" },
    { name: "proofType", value: "ProofMode", type: "string" }
    { name: "proof", value: proofModeData.fileHash, type: "string" },
    { name: "proofTime", value: proofModeData.proofGenerated, type: "uint64" }
  ]
};

const newAttestationUID = await createOnChainAttestation(signer, attestationData);
```

<br>

These three demonstrative strategies are only a few the many recipes that could be used to make Location Protocol compliant attestations that ensure location information is verifiable, transparent, interoperable, and trustworthy on the decentralized web. Importantly, these strategies can be extended and combined to create new recipes that provide additional verification and security for location information. Ongoing work includes the development of a library of recipes for using the Location Protocol to make more complex and extensible location attestations, including those that include formal [location proofs as evidence](#proof-fields). It also includes the development of an SDK for creating location attestations compliant with the Location Protocol, with the recipe library, will streamline application development.

## Scenarios for real-world applications of Location Attestations

### Touch-Grass

The [Touch Grass app](https://touch-grass-gamma.vercel.app/), is a fun and interactive way to encourage people to spend time outdoors. It lets users "touch grass" and record these moments — using attestations to prove they were actually outside. The app checks if they're in an outdoor area, like a park or nature reserve. Once confirmed, it records the details of the user being outside and uses their wallet address to sign a secure digital ledger so it can't be changed or erased. Users can see their own history of outdoor events, view a global map of where others have touched grass, and even compete on a leaderboard to see who is the most active outdoors.

### Kolektivo

[Kolektivo](https://www.kolektivo.network/) focuses on empowering local communities in Curaçao to restore ecosystems and improve food security through regenerative agriculture. Leveraging decentralized technology to support these initiatives, using community currencies and decentralized governance to ensure transparent, equitable resource allocation and to incentivize sustainable practices. Using the location protocol, regenerative agricultural stewards, could verify the location of say wind data that's collected from a weather station, and use that data to create an attestation object. This could be used to verify the location of the weather station, and the data collected from it, and provide a verifiable record of the data that could be impacted by extreme weather events.

### M3tering

The [M3tering Protocol](https://m3ter.ing/) is a blockchain-based initiative designed to combat energy poverty in underserved regions like sub-Saharan Africa and Latin America through incentivized decentralized solar energy production through tokenized rewards. Participants can become electricity providers by installing rooftop solar systems and earn protocol tokens based on energy output, fostering a self-reinforcing "DePIN flywheel effect" that drives infrastructure growth. By leveraging smart contracts to ensure immutable tracking of energy data and automated payments and a decentralized governance model (DAO) to empower communities to manage resources transparently, M3tering aims democratize clean energy access while reducing reliance on centralized systems.

### Whiteflag Protocol

[Whiteflag Protocol](https://www.whiteflagprotocol.org/standard/) utilizes blockchain technology to establish secure, decentralized communication channels in conflict zones, enabling stakeholders to share cryptographically verified messages—such as protected area designations or danger zone alerts—through immutable on-chain transactions authenticated via private keys and web resource control. Its standardized message schema supports seven functional categories, from emergency signals to resource coordination, while elliptic-curve encryption ensures sensitive data remains accessible only to intended recipients despite public blockchain visibility. The extensible nature of decentralized protocols enables new functionality. Using the location protocol framework alongside Whiteflag enables new functionality, providing humanitarian organizations and other key stakeholders with a spatial lens for crisis mapping by providing real-time, cryptographically signed geospatial data to improve the accuracy of conflict zone boundary markers and resource tracking

## Call to action

The Location Protocol Specification is a significant step towards creating a standardized framework for storing location data on the blockchain. By leveraging the Ethereum Attestation Service, we can create, sign, and verify location attestations that can be used across different platforms and applications. This opens up new possibilities for how we create, share, and trust spatial information in the decentralized web.

We are excited to see how the community will use this framework to build innovative applications and services that leverage location data. We encourage developers, researchers, and organizations to explore the Location Protocol Specification and contribute to its evolution. Together, we can create a more open, transparent, and trustworthy ecosystem for location data on the blockchain.

**Notes Captured from the discussion**

we would love feedback on any aspect of this. In particular, do you have a an application that would benefit from the location protocol? Do you have a use case that you would like to see supported? Do you have a specific location data type that you would like to see supported. Does the location protocol spec fields meet you needs? Is there a location component (locationType) that's not included in the spec that you use and would like to see included?  

Flexibility is core to the Location Protocol, allowing users to extend the base model of a location attestation object with additional fields to suit their needs.

This is a core element of the the Decentrlized geospatial web, and treating location data as a first class citizen. We are excited to see how the community will use this framework to build innovative applications and services that leverage location data. We encourage developers, researchers, and organizations to explore the Location Protocol Specification and contribute to its evolution. Together, we can create a more open, transparent, and trustworthy ecosystem for location data on the blockchain.

(Reference to other projects that we are working on)

- spatial.sol for performing spatial queries on the blockchain
- API to query geospatial attestations with an interactive mapping interface
