#! /bin/bash

# Command for 1a
wget https://schlieplab.org/Static/Teaching/DIT852/private-healthcare-percent-gdp.csv

# Command for 1b
input_file="private-healthcare-percent-gdp.csv"
removed_headers_file="removed_headers_output.csv"
awk 'NR > 6' "$input_file" | awk '$1 == "AFG"; 1' > "$removed_headers_file"

# Command for 1c
cat "$removed_headers_file" | uniq -c | wc -l

# Command for 1d
filter_file="filtered-healthcare_2004-2014.csv"

awk -F ',' 'NR > 4 {print $1, $48, $49, $50, $51, $52, $53, $54, $55, $56, $57, $58}' OFS=',' "$input_file" > "$filter_file"

# Command for 1e
awk -F',' 'NR > 5 {gsub(/"/, "", $48);print $1, $48}' "$input_file" | sort -k2,2nr -t' ' | head -n 10

# Command for 1f
nordic_countries_file="nordic_countries_healthcare.csv"

awk -F',' 'NR > 4' "$input_file" | awk 'NR==1 || $1 ~ /"(DNK|FIN|ISL|NOR|SWE)"/'  > "$nordic_countries_file"
