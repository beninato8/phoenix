# Phoenix 2 Ship Searcher

Search through phoenix ships to find the ones that meet your requirements

All input is done through command line arguments.

Just run phoenix2.py and make sure phoenix2.csv is in the same directory.

If you don't have pandas installed, follow the instructions [here](https://pandas.pydata.org/pandas-docs/stable/install.html)

### Table of Contents

[Current Features](#features)

[Demos](#demo)

[TODO](#new-features)

[Installation](#installation)

## Features

Run `python3 phoenix2.py help` to see features

## Demo

![](https://github.com/beninato8/phoenix/blob/master/vids/search/gifs/16.gif)

See other demos [here](https://github.com/beninato8/phoenix/tree/master/vids)

## New Features

**TODO**

- [ ] Select what ships you own and only search those

**Completed**

- [x] Use substrings to search (kap instead of kappa-drive)

- [x] List multiple ships at once (cin,raz,von)

- [ ] Fix ~~bug~~ feature with overlapping text for just rare (rar:rare => Super Rare and Rare)

### TOC

[Demos](#demo)

[TODO](#todo)

[Installation](#installation)

## Demo

![](https://github.com/beninato8/phoenix/blob/master/vids/search/gifs/16.gif)

See other demos [here](https://github.com/beninato8/phoenix/tree/master/vids)


## Installation

### Option 1 - Cloning Repo

 - Clone the repo like this (Make sure you are in the right directory first)
```
git clone https://github.com/beninato8/phoenix.git
```

 - Make a new directory
```
mkdir -p ~/Github/
cd ~/Github/
```

Clone the repo like this [(Make sure you are in the right directory first)](#make-a-new-directory):
```
#Make sure you are in the right directory first
git clone https://github.com/beninato8/phoenix.git
```

### Make a new directory
```
mkdir -p ~/Github/
cd ~/Github/
```

### Alternatively, you could...

Run [this](https://github.com/beninato8/phoenix/blob/master/install.sh) script
```
#bash <(curl -s https://raw.githubusercontent.com/beninato8/phoenix/master/install.sh)
```