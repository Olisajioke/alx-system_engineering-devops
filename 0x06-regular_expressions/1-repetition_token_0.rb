#!/usr/bin/env ruby

def match_string(input)
  pattern = /^hb(t{1,6})n$/
  if input.match?(pattern)
    puts "#{input} matches the pattern."
  else
    puts "#{input} does not match the pattern."
  end
end

if ARGV.length == 1
  match_string(ARGV[0])
else
  puts "Please provide exactly one argument."
end
