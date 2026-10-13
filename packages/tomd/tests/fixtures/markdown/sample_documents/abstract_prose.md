---
title: "Standard Wording Anchors and Abstract Demonstration"
document: P3000R0
date: 2026-09-28
intent: info
audience:
  - "EWG"
  - "LEWG"
author:
  - "Jane Doe <jane@example.com>"
---

## Abstract

This proposal specifies an anchor-rich navigation model for **WG21 ISO C++** technical specifications. It introduces `std::execution` refinements and cross-references [P2300R10](https://wg21.link/p2300r10) with *zero runtime overhead*.

## 1. Introduction

Section anchors enable direct URL linking into individual proposal headings.

### 1.1 Background & History

Historically, WG21 papers lacked standardized stable anchor tags.

#### 1.1.1 Legacy Incompatibilities

Previous toolchains produced conflicting anchor names or omitted them.
