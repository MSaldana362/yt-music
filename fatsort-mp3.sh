#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: device not provided"
    echo "Usage: $0 /dev/sdc1"
    exit 1
fi

DEVICE="$1"

echo "Unmounting $DEVICE..."
if ! sudo umount "$DEVICE"; then
    echo "Error: failed to unmount $DEVICE"
    exit 1
fi

echo "Sorting $DEVICE..."
if ! sudo fatsort -n "$DEVICE"; then
    echo "Error: failed to sort $DEVICE"
    exit 1
fi

echo "Done. Device can now be unplugged or remounted."
