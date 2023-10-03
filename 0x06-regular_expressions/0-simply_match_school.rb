#!/usr/bin/env ruby
require 'oniguruma'

regex = Oniguruma::ORegexp.new('School')
if regex.match(ARGV[0])
  puts ARGV[0]
else
  puts "$"
end
