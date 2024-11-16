#!/bin/bash

# Clean previous build artifacts and generate DAT files
make clean
make createDATfiles

# Deduplicate entries in various data files
# The following commands remove duplicate lines from each file in-place.
# Note: Duplicate tuples/lines are identified and removed using `awk`.

files=("sell.dat" "items.dat" "user.dat" "seller.dat" "bids.dat" "bidder.dat")

for file in "${files[@]}"; do
    if [[ -f $file ]]; then
        echo "Processing $file..."
        awk -i inplace '!seen[$0]++' "$file"
    else
        echo "Warning: $file not found. Skipping..."
    fi
done

# Create the database, load data, and run the queries
make makeAdatabase
make loadData
make run7queries


