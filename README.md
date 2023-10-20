
# GLSL to Blender Nodes

[![CI](https://github.com/jhutson/glsl-nodes/actions/workflows/ci.yml/badge.svg)](https://github.com/jhutson/glsl-nodes/actions/workflows/ci.yml)

_*** This project is in the early stages of development. ***_

This is a Python add-in to allow authoring Blender shader node trees as GLSL scripts. It will read a GLSL file, and produce one or more node groups that represent each part of the script. Each node group will contain a node graph that is the equivalent of the GLSL code.

The GLSL files understood by this add-in should be thought of as scripts equivalent to shader node trees. It is not a generic converter from arbitrary fragment shaders to Blender nodes.

## Development - Getting Started
This project requires [Python 3.10](https://www.python.org/downloads/release/python-3100/). Once you've cloned the project from git, run the following from the root folder to set up a virtual environment and install required packages:

```
python3.10 -m venv --upgrade-deps env && source env/bin/activate && pip install -r requirements.txt
```