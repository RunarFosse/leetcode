#!/bin/bash

name=$1
time=$(date)

echo -e "# My Leetcode Solutions\nAll problems are tried solving in the most optimal way possible." > README.md
echo -e "\n\nLatest push from $name: $time." >> README.md