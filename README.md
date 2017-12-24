Binary Adages
=============

This is the source of my blog on development practices.

Usage
-----

1. Thin of something witty and wise to say.

2. Write a blog post.

3. Review blog post for foot-in-mouth syndrome.

4. Commit changes.

5. Build and publish blog (optional)

Tips
^^^^

Build blog with:

    ablog build

Monitor blog as you write with with:

    ablog serve -p 8000 -n -r --patterns="*.py;*.rst"
    open 127.0.0.1:8000

ablog also needs a `_website` directory that won't create:

    mkdir _website

See  [Post Excerpts and Images](http://ablog.readthedocs.org/manual/post-excerpts-and-images/) and [Cross-Referencing Blog Pages](http://ablog.readthedocs.org/manual/cross-referencing-blog-pages/).

Sample Post
^^^^^^^^^^^

    .. post:: Dec 23, 2017
        :tags: atag
        :author: Alan Ray

Publish
-------

Setup
-----

Requires Python 3.6+.

    pip install -r requirements.txt

As of November 2017, this installation uses a custom version of ablog since advances in Sphinx and Python require changes for ablog to work out-of-the-box.
