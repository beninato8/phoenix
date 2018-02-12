# Phoenix 2 Ship Searcher
All input is done through command line arguments.

Just run phoenix2.py and make sure phoenix2.csv is in the same directory.

If you don't have pandas installed, follow the instructions [here](https://pandas.pydata.org/pandas-docs/stable/install.html)

### TOC

[Demos](#demo)

[TODO](#todo)

[Installation](#installation)

## Demo

![](https://github.com/beninato8/phoenix/blob/master/vids/search/gifs/16a.gif)

See other demos [here](https://github.com/beninato8/phoenix/tree/master/vids)

## TODO

- [ ] Select what ships you own and only search those

- [x] Use substrings to search (kap instead of kappa-drive)

- [x] List multiple ships at once (cin,raz,von)

## Installation

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