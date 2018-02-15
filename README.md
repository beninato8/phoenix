# Phoenix 2 Ship Searcher

Search through phoenix ships to find the ones that meet your requirements.

All input is done through command line arguments.

Just run phoenix2.py and make sure phoenix2.csv is in the same directory.

You can either run the program using `python3 phoenix2.py [args]` or you can use the shell script, 
which is simply running the previous command. To run the script, simply do `./phoenix [args]`

If you don't have pandas installed, follow the instructions [here](https://pandas.pydata.org/pandas-docs/stable/install.html)

### Table of Contents

[Current Features](#features)

[Demos](#demo)

[New Features](#new-features)

[Installation](#installation)

## Features

Run `./phoenix help` to see features

## Demo

<p align="center">
    <img src="https://raw.githubusercontent.com/beninato8/phoenix/master/vids/search/gifs/16.gif" width="600"/> <!---->
</p>

See other demos [here](https://github.com/beninato8/phoenix/tree/master/vids)

## New Features

**TODO**

- [ ] Select what ships you own and only search those

- [ ] ***Fix ~~bug~~ feature with overlapping text options (For example, rar:rare shows both Super Rare and Rare, and since Super Rare has the word Rare in it, both options are shown)***

**Completed**

- [x] Use substrings to search (kap instead of kappa-drive)

- [x] List multiple ships at once (cin,raz,von)

## Installation

 - First, make sure you are in the right directory.
```
mkdir -p ~/Github/
cd ~/Github/
```
 - Clone the repo like this
```
git clone https://github.com/beninato8/phoenix.git
```
 - You could also download a zip of the repo [here](https://github.com/beninato8/phoenix/archive/master.zip) which is just the link found from clicking the Clone or Download button in the repo.

 - The only files you need to run the program are phoenix2.csv and phoenix2.py (and optionally the phoenix executable if you want to run the program that way). All the others can be deleted if you want to save space.