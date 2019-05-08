# Install system level tools.
brew install asciidoctor
pip install -r requirements.txt

# Theme setup
git submodule update --init

# Clone the pelican plugin and only relevant submodules.
# Initialize the submodules and clean it.
git clone https://github.com/getpelican/pelican-plugins
cd pelican-plugins
git submodule --init
git submodule update pelican-ipynb
git submodule update render_math

