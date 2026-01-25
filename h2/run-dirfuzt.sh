#!/bin/bash
# Script to run dirfuzt-0 on Mac M1 using Docker

# Make sure Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker daemon is not running. Please start Docker Desktop."
    exit 1
fi

# Run the binary in a Linux container
# Using Ubuntu for better compatibility with statically linked binaries
docker run --rm \
    -v "$(pwd):/work" \
    -w /work \
    ubuntu:20.04 \
    ./dirfuzt-0 "$@"
