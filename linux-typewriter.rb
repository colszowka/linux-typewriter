#!/usr/bin/env ruby
require 'rubygems'
require 'sinatra'

KeypressPy = Thread.new do
  system File.join(File.dirname(__FILE__), 'bin', 'keypress.py')
end

Sounds = Dir[File.join(File.dirname(__FILE__), 'sounds', '*.wav')]

get '/key' do
  sound_file = Sounds[rand(Sounds.length)]
  thread = Thread.new do 
    system "aplay #{sound_file}"
  end
  "played #{File.basename(sound_file)}"
end
