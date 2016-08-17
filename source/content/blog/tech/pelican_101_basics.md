Title: Static Sites - What I learned putting together this blog, Part 2
Status: published
Slug: pelican_101_basics
Date: 2016-08-17 9:00
Tags: Static Sites, Pelican 101, Tech, Github Pages

<!-- PELICAN_BEGIN_SUMMARY -->
This is Part 2 on a step by step guide on how to get your hands dirty with  pelican, **a python based static site generator**, to put together a personal blog and have it published online without spending a dime. Part 1 of this post can be found [here]({filename}/blog/tech/static_sites.md) .

<!-- PELICAN_END_SUMMARY -->

[Pelican](http://docs.getpelican.com/en/3.6.3/index.html){:target: '_blank'} is a very nice to have tool in your  arsenal,  for any creative. As I tinkered with it when assembling this blog, I learned a few things that I thought it would be nice to share for anyone who would want to get started on it.

Let's dive right into it:

# Setting up the project
-------------------------

####1.  Creating Project Repository

Head to [Github](http://github.com){:targe='_blank'} and create a github repository for the project source's code. Inorder for you to be able to use github as your CDN(Content Delivery Network) to serve your blog when published, the repository has to be named as: ```your_github_username.github.io```

![Creating Github Pages Reposiotry]({filename}gh_pages.png)

This way, github will recognise the project as Github Pages and be able to serve it as a static site when you visit:
```http://your_github_username.github.io```

You see, no need to spend a dime to buy some domain and hosting space somewhere so as to be able to create you digital presence. Times have never been so exciting !

####2. Cloning the project and setting up relevant git branches

 Clone the project repository:
    ```git clone https://github.com/your_githib_username/your_github_username.github.io``` .
Then create a local **dev** branch, switching to it at the same time:

    cd your_github_username.github.io
    git checkout -b dev


####3. Installing project dependencies

- Create a **requirements.txt** file in the project root folder and put a bunch of project dependencies:

*requirements.txt* file:

    beautifulsoup4==4.5.1
    blinker==1.4
    docutils==0.12
    feedgenerator==1.8
    Jinja2==2.8
    Markdown==2.6.6
    MarkupSafe==0.23
    pelican==3.6.3
    Pillow==3.3.0
    Pygments==2.1.3
    python-dateutil==2.5.3
    pytz==2016.6.1
    six==1.10.0
    smartypants==1.8.6
    typogrify==2.0.7
    Unidecode==0.4.19
    webassets==0.11.1
    Fabric==1.12.0
    ghp-import==0.4.1

- Create  a python virtual enviroment for the project:
    - Install virtualenv via pip if you don't have it installed already:
        ```pip install virtualenv```
    - Create virtual environment for the project:
        ```virtualenv venv```
    - Ignore the  created virtual environmennt folder from being tracked by git:
        ```echo '/venv' >> .gitignore```
    - Activate the python virtual enviroment:
        ```source venv/bin/activate```

- Then install project dependencies from the requirements file:
   ``` pip install -r requirements.txt```


#  Generating Pelican's Initial files
---------------------------------------
Running ```pelican-quickstart ``` on your terminal will ask you a bunch of questions as it generates the static site.

**Note,** On the:  ```> Where do you want to create your new web site? [.]``` question, provide ```source``` so
that the generated files are put in the source folder.

#  Creating your first article and quick previewing the generated site
-----------------------------------------------------------------------

####1. Create your first article
Use your preferred text editor and create your first article with the following content:

```
Title: My First Article
Date: 2016-08-15 9:00
Category: blogging_101

Yeay, this is my shot at blogging
```
Given that this example article is in **Markdown** format(you can use any format you like .rst), save it
in the ```content``` folder of the sorce directory with a *.md* file extension.

####2. Generate your site
From your site directory, in the source folder, run the ``pelican`` command to generate your site:

    pelican content

####3. Preview your site

Open a new terminal session and run the following commands to switch to your
``output`` directory and launch Pelican's web server:

    cd ~/your_project_directory/source/output
    python -m pelican.server

Preview your site by navigating to ```http://localhost:8000/``` in your browser.


# Publishing your site
-----------------------------------------------------------------------
To publish your site, we will use python's fabric automation tool to automate a bunch of commands.

Replace the contents of the ```fabfile.py``` file in the ```source folder``` with:

    from fabric.api import local, env
    import os
    import shutil
    # Local path configuration (can be absolute or relative to fabfile)
    env.deploy_path = 'output'
    DEPLOY_PATH = env.deploy_path
    # Github Pages configuration
    env.github_pages_branch = "master"


    def clean():
        """Remove generated files"""
        if os.path.isdir(DEPLOY_PATH):
            shutil.rmtree(DEPLOY_PATH)
            os.makedirs(DEPLOY_PATH)


    def gh_pages():
        """Publish to GitHub Pages"""
        clean()
        local('pelican -s publishconf.py')
        local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
        local("git push origin {github_pages_branch}".format(**env))


    def publish():
        gh_pages()


Update your ```publishconf.py``` file in the ```source``` folder so as it looks like:

    from __future__ import unicode_literals
    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *

    SITEURL = 'http://your_github_username.github.io'
    RELATIVE_URLS = False
    DELETE_OUTPUT_DIRECTORY = True


    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'


To publish your site, run:

    pelican publish


Congrats, your have just created and published your blog using pelican. Preview your blog by navigating to ```http://your_github_username.github.io```

Remember to commit and push your changes upstream, on your github repository:

    cd <your_project_folder>
    git add .
    git commit -m 'Generated my blog using pelican'
    git push origin dev   # push to the dev branch upstream


In the next post, I will be delving deeper into:

- Understanding the folders and files that were generated by pelican
- How to spruce up the generated site to your taste by using custom themes
- How to organize and structure your blog files , in my opionated way
- How to publish your blog on your custom domain
