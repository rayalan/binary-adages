Binary Adages
=============

The source code for my personal blog.

Setup
-----

Requires Python (3.10+ or so):

    git clone --recurse-submodules git@github.com:rayalan/binary-adages.git
    pip install -r requirements.txt
    pelican-themes -i pelican-themes\elegant

Writing
-------

Rebuild on change and host locally (port 8000) with:

    pelican -r -l

And to publish the blog:

    pelican -s publishconf.py
    ghp-import output -b gh-pages
    git push git@github:rayalan/rayalan.github.io.git gh-pages:master


Resources
---------

- There's a blank template under templates, which can be used for a starting post.
- [Elegant documentation](https://github.com/Pelican-Elegant/elegant)
- [Pelican](https://getpelican.com/)

Caveats
-------

### Invoke

As an experiment, there is also support for invoke, e.g.

    invoke build

in lieu of running Pelican directly, but that seems like more work than the pelican commands given above.

### Elegant

Elegant is available as a submodule. It likely needs to be installed, e.g.

    pelican-themes -i pelican-themes\elegant

It's likely that there's a more straight-forward way to keep everything in sync (e.g. changing the theme to `pelican-themes/elegant`).

### Elegant (Search)

Search is not yet working. The outdated documentation is for Tipue search; there's a more modern replacement (based on Stork), but it requires a Linux/macOS setup that I haven't dived into. It may also require theme changes.

### extract_toc (plugin)

[extract_toc](https://github.com/getpelican/pelican-plugins/blob/master/extract_toc/extract_toc.py) is a Pelican plugin that hasn't yet been exported to a standalone Python package. For now, it is simply copy-and-pasted into a folder, but in the future, it should be installed via requirements.txt when it is a standard Pelican plugin.
