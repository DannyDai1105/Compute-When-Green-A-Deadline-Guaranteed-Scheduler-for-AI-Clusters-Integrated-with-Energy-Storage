# README.md
# Compute-When-Green
A deadline-guaranteed power-computing co-scheduling framework for AI data centers with battery energy storage.

## Project Overview
AI datacenters run mixed workloads: low-latency inference jobs that must execute immediately, and delayable training jobs that can be scheduled within deadlines.
Compute-When-Green (CWG) shifts flexible training workloads to time windows with abundant renewable energy and low grid price, coordinating battery charge/discharge, to cut operational cost and carbon emissions without violating deadlines.

## Simulation
This repository contains a 24-hour time-series simulation and visualization script for our hackathon demo.
It compares a naive baseline (run jobs on arrival) against the CWG scheduling strategy.

### Install dependencies
```bash
pip install -r requirements.txt
