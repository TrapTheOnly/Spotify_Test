# Spotify Test App

## About App

The Spotify regional server warehouse provides music streaming services for the billions of clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason, the clients must wait for responding with regarding the next time schedule:

* First interval: Between 12:00 – 17:00 the maximum wait time must be 2 seconds

* Second Interval: After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds

* Third Interval: After the 23:59 till the 12:00 of the next day the waiting time must be 1 second

The exponential backoff of these intervals must be increased by the next factors:

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
python3 spotify.py server {{Same Hostname}} -p (OPTIONAL) {{Port number}}
```