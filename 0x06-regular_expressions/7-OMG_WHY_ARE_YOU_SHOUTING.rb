#!/usr/bin/env ruby
# This script extracts and prints capital letters from the input text.
input_text = ARGV[0]

capital_letters = input_text.scan(/[A-Z]/).join

if capital_letters.empty?
  puts ""
else
  puts capital_letters
end
