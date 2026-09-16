# Cryptographic access control

## What it does

Evaluate RBAC and time-based rules before key/data access.

## Baseline and source status

- `00_original/SOURCE_STATUS.md` records that no official source listing appeared in the manuals.
- `00_original/generated_baseline.py` is runnable code derived from the official exercise and clearly labeled as an addition.
- The unchanged manuals are preserved in `SOURCE_MATERIAL/`.

## Modified versions (additions)

- `modifications/access_control.py`
- `modifications/02_access_control.py`

## Reusable blocks

Input/encoding -> core Cryptographic access control operation -> inverse/verification -> output.

## Know before modifying

Understand Role permission and validity-window predicates, representation conversions, parameter validation, and the difference between a demonstration and production security.
