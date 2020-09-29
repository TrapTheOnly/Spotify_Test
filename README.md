# Spotify Test App

## Table Of Contents
1. [About](https://github.com/TrapTheOnly/Spotify_Test#about-app)
2. [Installation](https://github.com/TrapTheOnly/Spotify_Test#installation)
3. [Usage](https://github.com/TrapTheOnly/Spotify_Test#usage-guide)

## About App

The Spotify regional server warehouse provides music streaming services for the billions of clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason, the clients must wait for responding with regarding the next time schedule:

* First Interval: From 00:00 till 11:59 the maximum wait time is 1 second

* Second interval: From 12:00 till 16:59 the maximum wait time is 2 seconds

* Third Interval: From 17:00 till 23:59 the maximum wait time is 4 seconds

The backoffs of these intervals are increased exponentially by next factors:

* For the first and third intervals: doubles each iteration
* For the second interval: triples on each iteration

## Installation

```
git clone https://github.com/TrapTheOnly/Spotify_Test.git
```

Install requirements
```
pip install -r requirements.txt
```

## Usage Guide

You need at least 2 seperate terminals being open:

Server Terminal
```
python3 spotify.py server {{Hostname}} -p (OPTIONAL) {{Port number}}
```

Client Terminal
```
python3 spotify.py client {{Same Hostname}} -p (OPTIONAL) {{Port number}}
```

Example of Hostname (recommended):
`127.0.0.1`

By default Port number is set to `65432`

To stop server, head to Server Terminal and press ``Ctrl+C`` in terminal.