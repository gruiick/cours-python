#!/bin/zsh

set -e

if [[ -z $1 ]]; then
  echo "Usage: build.sh NUMBER"
  exit 1
fi

(
  mkdir -p build
  cd build
  texi2pdf ../python-${1}.tex
)
