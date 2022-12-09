# Scrapy Assignment

An assignment project which has the solo purpose of scrapping websites URL, images URLs and contact phone number using Python`s Scrapy Framework.

## Installation

First - create a Virtual Environment:
```
$ python3 -m venv <path to new virtual environment>
```

Second - Activate Virtual Environment
```
$ source venv/bin/activate
```

Third - install dependencies:
```
$ pip install -r requirements.txt
```

## Usage

Paste a company URLs list to project root then open terminal, there are 3 commands available:
 * address
 * logo
 * phone

To evoke them use:

```
$ scrapy crawl <desired command> -O <file name>.json
```

There will be individuals files which after shall be merge by running the following command:</br>
<small><strong>OBS:</strong>Check out if you in the same level of the builders.py file (~/home/usr/scrapy_assignment/assignment/assignment)</small>

```
$ python3 builders.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)