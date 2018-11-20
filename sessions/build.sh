#!/bin/zsh

set -e

if [[ -z $1 ]]; then
  echo "Usage: build.sh NUMBER"
  exit 1
fi


darkslide --linenos=no "${1}.md" --destination "${1}.html"
