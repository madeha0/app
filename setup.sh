#!/usr/bin/env bash
apt-get update && apt-get install -y \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    && apt-get clean
