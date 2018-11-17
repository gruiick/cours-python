#!/bin/zsh

set -e

if [[ -z $1 ]]; then
  echo "Usage: build.sh INPUT.md"
  exit 1
fi


out=${1:s/.md/.html}
darkslide --linenos=no $1 --destination ${out}
