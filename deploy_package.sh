#!/bin/bash

python3 setup.py egg_info
python3 setup.py sdist
twine upload dist/fbmessage-*.tar.gz
rm -rf dist
