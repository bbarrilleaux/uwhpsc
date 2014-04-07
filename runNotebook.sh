#!/bin/bash
# Start up iPython Notebook in the current folder from OSX Finder.
cd $(dirname "$0") && pwd
ipython notebook --pylab inline