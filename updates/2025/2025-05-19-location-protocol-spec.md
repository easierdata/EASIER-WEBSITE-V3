---
title: The **Location Protocol** specification - A standardized framework for working location information on the decentralized web

layout: post

date: 19, May 2025

author: Seth Docherty

sub_heading: ''

tags:

- Astral

- Easier

- Collaboration

---

# The **Location Protocol** specification - A standardized framework for working location information on the decentralized web

In collaboration with [Astral](https://www.astral.global/), we have been designing a standardized framework for working with location information on the decentralized web. The goal of this work is to enrich the emerging decentralized geospatial with established geospatial standards, making it easier to create and share geographic data and services in a decentralized manner, but also bringing novel mechanisms for verifiability, transparency, and trust to the web more generally. An initial version of the **Location Protocol** specification is outlined below, including xxx, yyy, and zzz.

## What is the Location Protocol Spec?

The location protocol framework is designed to enable independent implementations to interoperate without sharing code, while remaining flexible enough to support Earth-based, metaverse, and symbolic digital location contexts. Built on the [Ethereum Attestation Service](https://attest.org/) (EAS), the Location Protocol framework provides a standardized way to create attestations for location data. It allows users to create, sign, and verify location attestations that can be used across different platforms and applications. The location attestation object is a core component of the Location Protocol framework. A location attestation is a digital signature that verifies the authenticity and integrity of an arbitrary metadata object containing location information.

## Location Attestation Object

A location attestation object is a geospatial data artifact that includes a digital signature that verifies the authenticity and integrity of an arbitrary metadata object. At minimum it conforms to the [base data model](#base-fields) and can be extended with [composable fields](#composable-fields) to provide more context or information and leverage [EAS properties](#eas-properties) to customize the attestations.

The following diagram illustrates the composition of an attestation object that we'll be referencing in this document.

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

### Base fields

The location attestation object at a minimum must contain the fields below as to identify and represent the location data.

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

The `location` value is interpreted based on the `locationType` field. Implementations should not attempt to decode without first resolving `locationType`.

### Composable fields

A location attestation object can be composed of each representing a different aspect of the location data. These sub-objects can be used to provide additional context or information about the location data.

#### Common fields

The location attestation object supports additional fields that are common to all location attestations but not necessary to use. These fields provide additional information about the attestation and its context.

| Field Name | Type | Description |
|------------|------|-------------|
| media | `bytes`, `mediaType` | bytes array representing the media data associated with the location data. The `mediaType` is a MIME-type-style string describing the media data. |
| attributes | `string` | Additional attributes of the location data. |
| eventTimeStamp | `uint64` | The UNIX timestamp of the event associated with the location data. _Note, this should not be confused with the `time` field that represents when the attestation was created_. |
| eventId | `byte32`, `string` | An external identifier to be used as foreign key to link non-referenced attestations or external sources.  |
| recepient | `address` | The address of the recipient of the attestation. |
| memo | `string` | An arbitrary message or note. |

#### Proof fields

The location attestation object supports additional verification properties that can be used _prove_ the authenticity and integrity of the location data. These properties are optional but recommended for use cases that require a higher level of assurance.

| Field Name | Type | Description |
|------------|------|-------------|
| proof | `byte32` | The proof of the authenticity and integrity of the location data. |
| proofType | `string` | The type of proof used to verify the location data. |
| proofVersion | `uint8` | The version of the proof used to verify the location data. |
| prooverAddress | `address` | The address of the prover who generated the proof. |
| proofTime | `uint64` | The timestamp of when the proof was generated. |

### EAS Properties

The location protocol framework is built on top of the Ethereum Attestation Service (EAS) and uses the [EAS SDK](https://github.com/ethereum-attestation-service/eas-sdk) to create, sign, and verify attestations. The following properties are common to all EAS attestations that are stored on the blockchain (onchain) and off the blockchain (offchain) and are included in the location attestation object

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

The `schemaString` and `schemaUID` properties are used to define the structure of the data being attested, while the `refUID` property is used to link attestations together. The `expirationTime` property is used to set a time limit on the validity of the attestation, while the `recipient` property specifies who will receive the attestation. Once the attestation is created, it is signed and stored on the blockchain, returning a UID representing created attestation

**Attestation properties**

An attestation is retrievable by its UID, a 32-byte hash, to identify the attestation on the blockchain. Here are the following properties that are returned when an attestation is retrieved from the blockchain:

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

## Creating Location Attestations

This document provides a guide for creating location attestation objects for the Ethereum Attestation Service (EAS). It covers the steps to create, sign, and verify location attestations.

## Making an attestation

### Step 1: Identify the schema

The first step in creating a location attestation is to identify the schema that will be used. The schema defines the structure of the attestation and the data it will contain. A schema in EAS is defined by:

- **Schema UID**: A unique identifier for the schema on the EAS schema registry.
- **Schema String**: The string representation of the schema, which includes the fields and their types.

To create a location attestation, you can use the following schema:

```json
{
  "Schema Components": {
    "schemaUID": "0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a",
    "schemaString": "string srs, string locationType, string location, uint8 specVersion"
  }
}
```

This schema conforms to the base data model for creating location attestation objects.

### Step 2: Prepare a location attestation object

At it's core, attesting is a way to make a claim about some data. In this case, the claim is about a location. Whether that's a physical address, a GPS coordinate, or some other [form of location data](./location-attestation.md/#supported-location-types). As mentioned above, the `schemaString` defines the structure of the data that will be attested. Let's assign some values to the fields in the schema:

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

Before creating the attestation object, you need to encode the data according to the schema. The encoding process ensures it conforms to the structure defined by the schema associated with the attestation. Why is the encoding necessary?

**On-chain Validation**: Smart contracts rely on structured data to verify the integrity and correctness of an attestation. The SchemaEncoder ensures the data adheres to the schema's format, making it possible for on-chain logic (e.g., verification or revocation) to process the data reliably.

**Consistency and Interoperability**: By encoding data according to a defined schema, different systems and parties can interpret and validate the data uniformly, ensuring compatibility across applications and platforms.

We'll take the `locationAttestationObject` and encode it using the schemaString. Here's what our encoded location attestation object looks like:

```string
0x000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000009455053473a343332360000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e646563696d616c44656772656573000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001634342e3936373234332c202d3130332e37373135353600000000000000000000
```

> You can verify this encoding with any ETH ABI Decoder tool such as [this](https://adibas03.github.io/online-ethereum-abi-encoder-decoder/decode). All you need to do is paste the encoding into the input box and enter the schema field types in the order they appear in the schema string. For example, for the above encoding, you would enter `string, string, string, uint8` as the types.

### Step 4: Create the attestation object

At this point, we are now ready to create the attestation object. The attestation object contains the data, representing the encoded location attestation object, and the required EAS properties. Here's an example of the structure of an attestation object:

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

After the attestation is signed, submitted and added to the blockchain, a UID is generated, that can be used to query the attestation and view it's details. Here's an attestation for the location attestation object we created above.

**Attestation UID**: 0x628f06c011351ef39b419718f29f20f0bc62ff3342d1e9c284531bf12bd20f31

**EAS Explorer Link**:  https://sepolia.easscan.org/attestation/view/0x628f06c011351ef39b419718f29f20f0bc62ff3342d1e9c284531bf12bd20f31

### Example of creating an On-Chain Location Attestation with the EAS SDK

The following code TypeScript snippet demonstrates how to create a location attestation object using the EAS SDK.

```TypeScript
import { EAS, SchemaEncoder } from "@ethereum-attestation-service/eas-sdk";

const eas = new EAS(EASContractAddress);
eas.connect(signer);

// Initialize SchemaEncoder with the schema string
const schemaEncoder = new SchemaEncoder("string srs, string locationType, string location, uint8 specVersion");
const encodedData = schemaEncoder.encodeData([
  { name: "srs", value: "EPSG:4326", type: "string" },
  { name: "locationType", value: "decimalDegrees", type: "string" },
  { name: "location", value: "44.967243, -103.771556", type: "string" },
  { name: "specVersion", value: 1, type: "uint8" },
]);

const schemaUID = "0xedd6b005e276227690314960c55a3dc6e088611a709b4fbb4d40c32980640b9a";

const tx = await eas.attest({
  schema: schemaUID,
  data: {
    recipient: "0xFD50b031E778fAb33DfD2Fc3Ca66a1EeF0652165",
    expirationTime: 0,
    revocable: true
    data: encodedData,
  },
});

const newAttestationUID = await tx.wait();

console.log("New attestation UID:", newAttestationUID);
```

## Demonstrating real-world uses

### 1. Event Check-in using GeoIP

This example snippet demonstrates how location attestations could be used to as a way to verify attendance at an event. The app uses the device's IP address to get the location and create an attestation object. This could be used for events like concerts, conferences, or any other event where attendance needs to be verified.

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

### 2. Geocaching attestations with QR codes

This example snippet demonstrates how QR codes could be used in a scenario such as geocaching, treasure hunts, or location-based games event. The app scans a QR code, containing geo-spatial metadata, triggering the generation of location attestation.

```TypeScript
const { signer } = getProviderSigner();

// Register schema if not already registered. Will return the schema UID if already registered
const schemaString: "string srs, string locationType, uint40[2][] location, uint40 specVersion, uint64 eventTimestamp, string memo";
const schemaUID = await registerSchema(signer, schemaString);

// Extract QR code metadata and Create the attestation object
const qrData = await decodeQR(imagePath)
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
    { name: "memo", value: "Geocaching event - Location 1", type: "string" }
  ]
};

const newAttestationUID = await createOnChainAttestation(signer, attestationData);
```

### 3. Attesting to media generated with Proofmode

This example snippet demonstrates how [Proofmode](https://proofmode.org/) (a mobile app for capturing verifiable photos) practical implementation of media verification attestations using EAS as to preserve the integrity and origin of digital evidence. This proof of concept is particularly valuable for applications requiring verified media evidence, such as journalism, human rights documentation, legal evidence collection, and scientific field research where the authenticity and provenance of media are critical.

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
  ]
};

const newAttestationUID = await createOnChainAttestation(signer, attestationData);
```

## Conclusion

The Location Protocol Specification is a significant step towards creating a standardized framework for storing location data on the blockchain. By leveraging the Ethereum Attestation Service, we can create, sign, and verify location attestations that can be used across different platforms and applications. This opens up new possibilities for how we create, share, and trust spatial information in the decentralized web.

We are excited to see how the community will use this framework to build innovative applications and services that leverage location data. We encourage developers, researchers, and organizations to explore the Location Protocol Specification and contribute to its evolution. Together, we can create a more open, transparent, and trustworthy ecosystem for location data on the blockchain.
