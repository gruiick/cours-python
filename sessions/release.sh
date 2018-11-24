#!/bin/zsh

set -e

if [[ -z $1 ]]; then
  echo "Usage: build.sh NUMBER"
  exit 1
fi


darkslide --linenos=no "${1}.md" --embed --destination "${1}.html"
prince "${1}.html" -o "${1}.pdf"
