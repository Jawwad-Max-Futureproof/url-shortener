# URL Shortener

made by [Jawwad](https://github.com/JawwadUddin) and [Max](https://github.com/Velocima)

## Installation & Usage

Requires python version 3.9.x and [pipenv](https://pipenv.pypa.io/en/latest/)

### Installation

- Open terminal and run the following commands:

```sh
git clone git@github.com:Jawwad-Max-Futureproof/url-shortener.git url-shortener
cd url-shortener
pipenv shell
pipenv install
```
- Note: you need to create a config file with a postgres database setup, the following format should be used:
```
DATABSE_URI = postgresql://username:password@host:port/db_name
```
### Usage

- To start a dev server run `pipenv run dev`
- In the browser go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to use the app

## Changelog

The full changelog can be found [here](./changelog.md)

The full commit history can be found [here](https://github.com/Jawwad-Max-Futureproof/url-shortener/commits/main)

## Bugs

### Known bugs

Feel free to raise any issues you find [here](https://github.com/getfutureproof/fp_lap4_morris_debug-Velocima/issues)
