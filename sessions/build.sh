#!/bin/zsh

set -e

if [[ -z $1 ]]; then
  echo "Usage: build.sh NUMBER"
  exit 1
fi

(
   cd build
   texi2pdf ../python-${1}.tex
)
