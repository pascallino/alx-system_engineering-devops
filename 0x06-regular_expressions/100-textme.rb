#!/usr/bin/env ruby

def extract_info_from_log(log_line)
  sender = log_line[/\m[:][+A-Za-z0-9]*/].gsub(/^[\m:]/, '')
  sender = sender.gsub(/^[\:]/, '')
  receiver = log_line[/\o[:][+A-Za-z0-9]*/].gsub(/^[\o:]/, '')
  receiver = receiver.gsub(/^[\:]/, '')
  flags = log_line[/s:[-1:0]*/].gsub(/^[s:]/, '')
  flags = flags.gsub(/^[\:]/, '')

  "#{sender},#{receiver},#{flags}"
end

# Check if an argument was provided
if ARGV.empty?
  puts "Please provide the log string as an argument."
  exit(1)
end

log_string = ARGV[0]

lines = log_string.split("\n")

lines.each do |line|
  result = extract_info_from_log(line)
  puts result
end
