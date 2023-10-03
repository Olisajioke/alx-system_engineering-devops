#!/usr/bin/env ruby
# regex_matcher.rb


if ARGV.empty?
  puts "Please provide an input string as an argument."
else
  input_string = ARGV[0]


  regex = /^h(b*t)n$/

  matches = input_string.scan(regex)

  if matches.empty?
    puts "No matches found."
  else
    puts "Matches found: #{matches.join(', ')}"
  end
end

