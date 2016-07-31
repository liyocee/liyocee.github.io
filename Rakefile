require 'rake'
require 'httparty'
require 'json'

desc "Initial setup"
task :bootstrap do
  puts 'Installing dependencies...'
  puts `bundle install --without distribution`
end

namespace :deploy do
    task :fetch_gh_pages do
        Dir.mkdir('build') unless Dir.exist?('build')
        Dir.chdir('build') do
          `git init`
          remote_exists = (`git remote | grep origin`).chomp.length > 0
          `git remote add origin https://github.com/ashfurrow/ashfurrow.github.io.git` unless remote_exists
          `git pull origin master`
        end
      end

end
