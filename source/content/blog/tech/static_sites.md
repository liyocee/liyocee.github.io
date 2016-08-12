Title: Static Sites - What I learned putting together this blog, Part 1
Status: published
Slug: static_sites
Date: 2016-08-12 9:00
Tags: Static Sites, CMS, Blogging Tools, Tech

<!-- PELICAN_BEGIN_SUMMARY -->
When it comes to assembling a static site, the technology ecosystem is littered with countless tools,
each with its own strengths, shortcomings and philosophy. I set out to set my own biased criteria as to what
a best tool should meet, and here is what I put together...
<!-- PELICAN_END_SUMMARY -->

> Having options is the Ultimate Freedom


I wanted to put together a simple, static personal blog that met the following three major criteria:

-   Adding posts should be done in plain text in an a text editor that I like : **Sublime Text**
-   Publishing the added posts online should be done in just **one** command
-   My published blog should be served from any CDN - Content Delivery Network , of my choice


So, I started exploring the tools available in my arsenal that could meet the above criteria, and below
is what I found out:

# 1. Content Management Systems(CMSs):

They come in all shapes and sizes, ranging from Wordpress, Drupal, Django CMS , Joomla and many others.

Of my particular interest was Wordpress because it's widely used and mostly touted to be
**the tool to be**, when it comes to putting together a personal blog.

These CMS tools are very good for a different audience and different purposes, but for me, they just couldn't fit my criteria:

- Yes, they give you _fancy editors_ to create your content, without you having to bang your head with
those html tags
- Yes, they ship with many templates and have large communities around them building very nice templates
that one can adopt to put together a well designed blog/webiste
- Yes, they have plugins for anything, some free ,some premium and some fremium for an extra functionality
you may need that doesn't come shipped with the core underlying tool
- Yes, the give one several options for publishing their content online, with the likes of wordpress
eliminating the whole fuss altogether by allowing you to just do everything on their online tools


But for me, the above just didn't cut it to make me want to adopt any of them.

Adopting any one of them would me:

- My content shoud conform to the lingua that each tool has prescribed
- That once I get started using one of them, I would be locked in and even if it reaches a point when I just don't like it; just tossing it away and moving on to the next tool would be quite a hassle, especially porting my content
- That there's no way I could get my content published to any CDN of my choice, _I stand corrected_
- That I would have to put up with a lot of bloated code and nothingness that my published content end up being bundled with, with a lot of functionality that I cannot and will never need


Hence, I moved on to:


# 2. Static Sites Generators:

They too come in all shapes and sizes, ranging from Pelican, Jekyll, Middleman, Brunch, GitBook, MkDocs, Cactus, Nikola ; just to mention a few.

Each one of them has got its initial learning cover, its own strengths and its own shortcomings.

I personally tinkered with Pelican(Python Based) and Middleman(Ruby based) and yeah, they just met my needs:

- Each one of them allowed me to write my posts in plain text, ofcourse giving you options to spruce it up using simple, lightweight syntaxes like Markdown and .rst
- They didn't get in my way as to which editor to use for writting the posts
- They allowed me to publish my content with just one command, ofcourse with a few one-off  configurations I had to do
- They allowed me to publish my content to any CDN of my choice, and I ended up publishing the content to Github Pages(gh-pages)
- And Yeah, they didn't just shove anything down my throat - (I like having options and freedom that comes with it)

I ended up going with Pelican, not for any particular shortcomings that Middleman might have had, but just because I consider myself a Pythonista.

Apart from this blog, I also put up this [site](http://zeptohub.com){:target='blank'} using the Pelican Generator and hosted by Github Pages CDN, just to push the limits as to what these static sites generators are capable of.


In the next post, I will delve deeper on how I used Pelican to put up this blog and this [website](http://zeptohub.com){:target='blank'}.
