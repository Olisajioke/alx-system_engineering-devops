#!/usr/bin/env ruby
#Ruby code that 
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit(1)
end

input_string = ARGV[0]

pattern = /^h.n$/

if input_string.match?(pattern)
  puts input_string
end
