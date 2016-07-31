
require 'lib/custom_helpers'
require 'lib/add_links_to_navigation.rb'
require 'lib/modify_widths.rb'
require 'lib/embed.rb'
require 'ansi/code'
# Per-page layout changes:
#
# With no layout
# For custom domains on github pages
page "CNAME", layout: false

page '/*.xml', layout: false
page '/*.json', layout: false
page '/*.txt', layout: false

##
#Blog Settings
##

#Better markdown support
set :markdown_engine, :redcarpet
set :markdown,
    fenced_code_blocks: true,
    smartypants: true,
    disable_indented_code_blocks: true,
    prettify: true,
    tables: true,
    with_toc_data: true,
    no_intra_emphasis: true

set :haml, ugly: true, format: :html5

activate :autoprefixer do |config|
  config.browsers = ['last 2 version', 'Firefox ESR']
  config.cascade  = false
  config.inline   = true
end

activate :blog do |blog|
  # This will add a prefix to all links, template references and source paths
  blog.prefix = "blog"
  blog.permalink = "{title}.html"

  # Enable pagination
  blog.paginate = true
  blog.per_page = 10
  blog.page_link = "page/{num}"
  blog.summary_separator = /<!-- more -->/
  blog.new_article_template = "new_article.markdown.erb"
  blog.layout = "blog_post"
end

###
# Other settings
###

# Assets
set :css_dir, 'css'
set :js_dir, 'javascripts'
set :images_dir, 'images'
set :fonts_dir, 'fonts'


###
# Helpers
###


helpers CustomHelpers

# Activate the syntax highlighter
activate :syntax
# activate :inliner

# Make url's prettier, without the .html
activate :directory_indexes

# Automatic image dimensions on image_tag helper
activate :automatic_image_sizes

# Easier bootstrap navbars
activate :bootstrap_navbar

activate :modify_widths
activate :embed

# Github pages require relative links
set :relative_links, true

# Build-specific configuration
configure :build do
  # Any files you want to ignore:
  ignore '/admin/*'

  # Minify CSS on build
  activate :minify_css

  # Minify Javascript on build
  activate :minify_javascript

  # Enable cache buster
  activate :asset_hash, ignore: [/^images\/.*/, /^fonts\/.*/, /^[^\/]*$/]

  # Use relative URLs
  activate :relative_assets
end

page "/feed.xml", layout: false


# deploy
activate :deploy do |deploy|
  deploy.deploy_method = :git
  deploy.build_before = true
  deploy.branch = 'master'
end
