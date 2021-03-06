# Install system level tools.
brew install asciidoctor
pip install -r requirements.txt

# Theme setup
#git submodule update --init
if [ ! -d src/templates/hn-theme ]; then
    git clone https://github.com/haridas/hn-theme src/templates/hn-theme
fi

# Clone the pelican plugin and only relevant submodules.
# Initialize the submodules and clean it.
if [ ! -d pelican-plugins ]; then
    git clone https://github.com/getpelican/pelican-plugins

    cd pelican-plugins
    git submodule init
    git submodule update --remote pelican-ipynb
    #git submodule update --remote pelican-gist
fi

