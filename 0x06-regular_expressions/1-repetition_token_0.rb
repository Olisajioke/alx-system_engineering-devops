#!/usr/bin/env ruby

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit(1)
end

pattern = /hb*t*n/
input_string = ARGV[0]

match = pattern.match(input_string)

if match
  puts match[0]
else
  puts ''
end
