require 'rake'
require 'httparty'
require 'json'

desc "Initial setup"
task :bootstrap do
  puts 'Installing dependencies...'
  puts `bundle install --without distribution`
end

namespace :deploy do



  desc "Deploys RSS and Atom feeds"
  task :feeds do
    puts "Feeds deployed."
  end

  desc "Deploys to production and syncs feeds"
  task :all => [:fetch_gh_pages, :gh_pages, :feeds] do
    puts 'Deploy all succeeded.'
  end

  task :fetch_gh_pages do
    Dir.mkdir('build') unless Dir.exist?('build')
    Dir.chdir('build') do
      `git init`
      remote_exists = (`git remote | grep origin`).chomp.length > 0
      `git remote add origin https://github.com/liyocee/liyocee.github.io.git` unless remote_exists
      `git pull origin master`
    end
  end

  task :gh_pages do
    head = `git log --pretty="%h" -n1`.chomp

    Dir.chdir('build') do
      `cp feed.rss.xml feed`
      `cp feed.rss.xml index.php/`

      message = "Site updated to #{head}."
      `git add .`
      `git commit --allow-empty -m \"#{message}\"`
      `git push origin master`
    end
  end
end

namespace :publish do
  desc "Build and deploy to production"
  task :production do
    Rake::Task['build'].invoke
    Rake::Task['deploy:production'].invoke
    Rake::Task['deploy:feeds'].invoke
  end
end

namespace :build do
  desc 'Builds, then tests'
  task :test do
    Rake::Task['build'].invoke
    Rake::Task['test'].invoke
  end
end

desc "Build site locally"
task :build do
  sh 'bundle exec middleman build --verbose --no-clean'
end

desc "Start middleman server"
task :server do
  puts "Starting Middleman server"

  middleman = Process.spawn("bundle exec middleman")

  trap("INT") {
    Process.kill(9, middleman) rescue Errno::ESRCH
    exit 0
  }

  Process.wait(middleman)
end

desc 'Runs html-proofer against current build/ directory.'
task :test do
  require 'html/proofer'

  puts 'Testing build/ directory.'
  HTML::Proofer.new('build/', {
    ext: '.html',
    check_html: true,
    disable_external: true,
    alt_ignore: [/.*/],
    parallel: { in_processes: 3},
    }).run
end

desc "Create new blog article"
task :article, :title do |task, args|
  title = args[:title]
  abort "You must specify a title." if title.nil? || title.length < 1

  output = `bundle exec middleman article '#{title}'`
  # output is something like 'create  source/blog/2016-05-28-testing-testing.html.markdown'
  dir_name = output.scan(/[0-9]{4}-[0-9]{2}-[0-9]{2}.*\.html\.markdown/)[0][11...-14]
  full_path = "source/img/blog/#{dir_name}"
  sh "mkdir #{full_path}" unless File.exists? full_path
  sh "open #{full_path}"

  image_path = full_path.gsub(/^source/, "")
  image_filename = "#{image_path}/background.jpg"
  image_details = fetch_cloudy_conway

  image_source_path = "source#{image_filename}"

  puts "Writing background image file: #{image_source_path}"
  File.open(image_source_path, 'w') { |file| file.puts image_details[1] }
  puts 'Please resize the image.'

  puts 'Applying article template frontmatter.'
  new_article_filename = output.scan(/source.*/)[0]
  contents = File.read(new_article_filename)
  contents.gsub!(/background_image: /, "background_image: #{image_filename}")
  contents.gsub!(/background_image_source: /, "background_image_source: #{image_details[0]}")
  File.open(new_article_filename, 'w') { |file| file.puts contents }

  sh "open -a 'iA Writer' #{new_article_filename}"
end

task :default => :server

def fetch_cloudy_conway
  require 'net/http'
  require 'uri'
  require 'twitter'

  puts 'Fetching latest @CloudyConway image...'

  client = Twitter::REST::Client.new do |config|
    config.consumer_key        = ENV['TWITTER_CONSUMER_KEY']
    config.consumer_secret     = ENV['TWITTER_CONSUMER_SECRET']
    config.access_token        = ENV['TWITTER_ACCESS_TOKEN']
    config.access_token_secret = ENV['TWITTER_ACCESS_SECRET']
  end

  tweet = client.favorites(count: 100).select { |t| t.user.screen_name == "CloudyConway" }.first
  tweet ||= client.user_timeline('CloudyConway').first
  media = tweet.media.first
  puts "Retrieved tweet: #{tweet.url}"
  image_url = media.media_url
  large_image_url = URI.parse(image_url.to_s + ":large")
  response = Net::HTTP.get_response large_image_url
  puts "Retrieved image data: #{large_image_url}"

  [tweet.url, response.body]
end

def git_branch_name
  `git rev-parse --abbrev-ref HEAD`
end
