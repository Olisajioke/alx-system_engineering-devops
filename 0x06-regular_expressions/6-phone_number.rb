#!/usr/bin/env ruby
# This script checks for a 10-digit phone number in the input text.
pattern = /\b\d{10}\b/

input_text = ARGV[0]

match = input_text.match(pattern)

if match
  puts match.to_s
else
  puts "No 10-digit phone number found in the input text."
end

