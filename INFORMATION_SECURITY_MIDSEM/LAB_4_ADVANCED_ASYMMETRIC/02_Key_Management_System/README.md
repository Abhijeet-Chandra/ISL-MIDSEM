# Key management system

## What it does

Generate, distribute, revoke, renew, and audit keys.

## Baseline and source status

- `00_original/SOURCE_STATUS.md` records that no official source listing appeared in the manuals.
- `00_original/generated_baseline.py` is runnable code derived from the official exercise and clearly labeled as an addition.
- The unchanged manuals are preserved in `SOURCE_MATERIAL/`.

## Modified versions (additions)

- `modifications/key_manager.py`
- `modifications/02_key_manager.py`

## Reusable blocks

Input/encoding -> core Key management system operation -> inverse/verification -> output.

## Know before modifying

Understand Lifecycle: generate -> distribute -> rotate/revoke, representation conversions, parameter validation, and the difference between a demonstration and production security.
