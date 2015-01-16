#!/bin/sh
PLUGIN_REPO=https://raw.githubusercontent.com/getpelican/pelican-plugins/master

download() {
    mkdir -p plugins
    if test -f plugins/$(basename $1)
    then
        echo got $1
    else
        wget $PLUGIN_REPO/$1 -O plugins/$(basename $1)
    fi
}

pip install -q -U \
    pelican \
    pelican-extended-sitemap

download plantuml/plantuml_rst.py
download googleplus_comments/googleplus_comments.py
