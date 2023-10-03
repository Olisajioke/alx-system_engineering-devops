#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

pattern = /School/

input_string = ARGV[0]
matches = input_string.scan(pattern)

result = matches.join

puts result
