# This app solves the following problem

```
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13...19
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teen. The input is passed as
command line arguments and output is to be printed on screen
```


## Installation

Make sure the that the ptython version is >=3.8. 

### Environment Setup

The following demonstrates setting up and working with a development environment:

```
$ make virtualenv

$ source env/bin/activate

```

## Run cli application

Go to the project root directory and execute the command:

```
$ python commandline_parser/app.py --help

$ python commandline_parser/app.py -i 10 10 10

$ python commandline_parser/app.py -i 10 10

$ python commandline_parser/app.py -v
```

## Testcases

The command to test it as follows:

```
$ make test

or

$ pytest
```

## Docker

Included is a basic `Dockerfile` for building and running the application, and can be built with the included `make` helper:

```
$ make docker

$ make run
```

## Docs

This project includes a `docs` folder containing the sample snapshot of the commandline interface.
