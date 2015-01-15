PLUGIN_REPO=https://raw.githubusercontent.com/getpelican/pelican-plugins/master

pip install -U \
    pelican \
    pelican-extended-sitemap \

wget $PLUGIN_REPO/disqus_static/disqus_static.py
wget $PLUGIN_REPO/plantuml/plantuml_rst.py
