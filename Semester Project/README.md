# SemesterProject_CS5402

## About

This project is providing data analysis on the upvote count on reddit posts based off other data associated with them.

## Requirements

Jupyter Notebooks, python3-pandas, python3-wordcloud

Reports require LaTeX for PDF generation.

## Generating the report

We officially used the PDF option.

### PDF

In Jupyter Notebooks use the Export as PDF option, ensure you have xetek and LaTeX installed. 

All LaTeX settings were from the Debian Buster default installations.

### HTML

In Jupyter Notebooks, use the Export to HTML... pretty simple.


## wrangler.py usage

> Note, there is a version of the wrangler included in the jupyter notebook.

1. Ensure you have python3, numpy, and pandas installed. (on Debian these packages are part of `main`)
2. Make a directory called "out" in `src_data`
3. In the root main directory, run `python3 src_data/wrangler.py"

