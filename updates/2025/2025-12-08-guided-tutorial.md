---
title: Building the Location Protocol into your applications

layout: post

date: 08, December, 2025

author: Seth Docherty

sub_heading: ""

tags:
  - Astral

  - Location Protocol
  
  - Tutorials

  - Development
---

# Building the Location Protocol into your applications

Location-aware systems increasingly need more than just coordinates; they need verifiable evidence that a specific event, asset, or observation is tied to a place and time in a way others can independently check. The Location Protocol addresses this by defining an open standard for cryptographically signed records that represent spatial features and related metadata, and the Astral SDK provides a practical implementation for creating and working with these attestations in real applications.

In this post, we’ll look at how and where to integrate the Location Protocol into common application workflows. The tutorial focuses on two typical patterns:

1. Data ingestion pipelines that extract geospatial data from APIs such as the USGS earthquake feed.
2. Data creation through user interfaces that capture user-drawn geometries from an interactive map.

Using the astral-sdk, we will wire the Location Protocol framework into each of these flows to transform raw geospatial artifacts into Location Protocol–compatible payloads and then create both off-chain and on-chain attestations.

The tutorial is designed for developers who want a concrete, reproducible reference for integrating verifiable location into existing systems or prototypes, rather than a high-level overview. If you follow along in the notebook, you will finish with a working example that connects data ingestion, location payload construction, attestation creation, and basic verification into a single, coherent flow.

[Exlore more with our notebook](../../notebooks/integrating_the_location_protocol_framework.ipynb)
