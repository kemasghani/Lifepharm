#!/bin/sh
# Enable the merge driver named in .gitattributes: on a store branch, merging master keeps the store's own JSON.
set -e
git config merge.ours.driver true
echo "merge.ours.driver enabled for $(git rev-parse --show-toplevel)"
