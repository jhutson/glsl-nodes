#!/bin/bash
set -e
mkdir -p build
pushd build

docker --version
docker image inspect antlr/antlr4 > /dev/null 2>&1 || {
  [[ ! -d antlr4 ]] && git clone https://github.com/antlr/antlr4.git --single-branch --depth 1
  pushd antlr4/docker
  docker build -t antlr/antlr4 .
  popd
}

[[ ! -d grammars-v4 ]] && git clone https://github.com/antlr/grammars-v4.git --single-branch --depth 1
docker run --rm -it -v ./grammars-v4/glsl:/work antlr/antlr4 -Dlanguage=Python3 -visitor GLSLLexer.g4 GLSLPreParser.g4 GLSLParser.g4 -o generated

popd
mkdir -p src/parser
mv build/grammars-v4/glsl/generated/* ./src/glslnodes/glsl
