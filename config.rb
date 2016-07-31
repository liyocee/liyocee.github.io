# For custom domains on github pages
page "CNAME", layout: false

# Assets
set :css_dir, 'stylesheets'
set :js_dir, 'javascripts'
set :images_dir, 'images'
set :fonts_dir, 'fonts'



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


# Activate the syntax highlighter
activate :syntax

activate :autoprefixer do |config|
  config.browsers = ['last 2 version', 'Firefox ESR']
  config.cascade  = false
  config.inline   = true
end

# Make url's prettier, without the .html
activate :directory_indexes

# Automatic image dimensions on image_tag helper
activate :automatic_image_sizes


# Easier bootstrap navbars
activate :bootstrap_navbar

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
  activate :asset_hash

  # Use relative URLs
  activate :relative_assets
end


activate :deploy do |deploy|
  deploy.deploy_method = :git
  deploy.build_before = true
  deploy.branch = 'master'
end
