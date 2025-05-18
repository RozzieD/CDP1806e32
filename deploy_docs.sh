#!/bin/bash

set -e

BUILD_DIR="docs/_build"
TARGET_BRANCH="gh-pages"

echo "Deploying Sphinx docs from $BUILD_DIR to $TARGET_BRANCH..."

# Make sure docs are built
if [ ! -d "$BUILD_DIR" ]; then
  echo "ERROR: Build directory $BUILD_DIR does not exist. Run 'sphinx-build -b html docs/ $BUILD_DIR' first."
  exit 1
fi

# Create a temporary directory
TEMP_DIR=$(mktemp -d)

# Copy HTML output
cp -r $BUILD_DIR/* $TEMP_DIR

# Switch to orphan branch
git switch --orphan $TARGET_BRANCH

# Remove all tracked files (ignore errors)
git rm -rf . > /dev/null 2>&1 || true

# Copy documentation into place
cp -r $TEMP_DIR/* .

# Remove temp dir
rm -rf $TEMP_DIR

# Commit and push to GitHub Pages branch
git add .
git commit -m "Deploy updated Sphinx documentation to GitHub Pages"
git push -f origin $TARGET_BRANCH

# Return to main branch
git switch main

echo "Deployment complete. Check your site at GitHub Pages."
