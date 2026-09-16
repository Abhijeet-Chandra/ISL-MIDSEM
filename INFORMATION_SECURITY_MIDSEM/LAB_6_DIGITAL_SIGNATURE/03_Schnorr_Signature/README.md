# Schnorr signature

## What it does

Demonstrate Schnorr signing and verification.

## Baseline and source status

- `00_original/SOURCE_STATUS.md` records that no official source listing appeared in the manuals.
- `00_original/generated_baseline.py` is runnable code derived from the official exercise and clearly labeled as an addition.
- The unchanged manuals are preserved in `SOURCE_MATERIAL/`.

## Modified versions (additions)

- `modifications/02_schnorr.py`
- `modifications/schnorr.py`

## Reusable blocks

Input/encoding -> core Schnorr signature operation -> inverse/verification -> output.

## Know before modifying

Understand e=H(R||m); s=k+ex; verify g^s=R*y^e, representation conversions, parameter validation, and the difference between a demonstration and production security.
