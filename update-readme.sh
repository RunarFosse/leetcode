#!/bin/bash

name=$1
time=$(date)


print_directory_problems () {
    local directory=$1
    cd $directory

    # Print directory title
    echo "\n## $directory\n"

    # Print table headers
    echo "| Problem | Time complexity | Space complexity | Leetcode |\n"
    echo "| :------ | :-------------: | :--------------: | :--------------: |\n"

    for f in *.py; do
        # Extract Big O notation from time- and space-complexity
        local time_complexity=$(cat $f | grep "Time complexity:" -m 1 | grep -oE "O\(.*\)")
        local space_complexity=$(cat $f | grep "Space complexity:" -m 1 | grep -oE "O\(.*\)")

        # Print table row
        echo "| [$f]($directory/$f) | $time_complexity | $space_complexity | <a href=\"https://leetcode.com/problems/${f%.py}/\" target=\"_blank\">Link</a>\n"
    done
    cd ..
}

# Print main title and description
echo -e "# My Leetcode Solutions\nAll problems are tried solving in the most optimal way possible." > README.md

# Print all directories
echo -e $(print_directory_problems Easy) >> README.md
echo -e $(print_directory_problems Medium) >> README.md
echo -e $(print_directory_problems Hard) >> README.md

# Print last updated and by who
echo -e "\n\nLatest push from $name: $time." >> README.md