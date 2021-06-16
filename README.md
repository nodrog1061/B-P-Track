# **VERRY EARLY BUILD**
<img alt="PyPI - Python Version" src="https://img.shields.io/badge/Python-%3E%3Dv3.9-brightgreen"> <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/nodrog1061/B-P-Track?include_prereleases"> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/nodrog1061/B-P-Track">
# What is BnP Track (Bin and People Track)?
BnP Track is a custom-built REST API system designed to be used in partnership with an Arduino to track either or the flow of people in a building or the usage of bins in a building the system is built in Python using the Flask library for delivery of webpages and pickle for the storage of data instead of a database. 

# How to use BnP Track
BnP track uses standerd POST and GET requrets with both JSON files and URL Parameters a standerd comunication may look like this:

## Example requrest

```
http://10.0.0.1:5000/api/pTrack?apiKey=XU8kQXnR-nH__-00GJRVin72Ozs
```
as the url
``` json
{
  "room": 6,
  "pIn": 25,
  "pOut":10
}
```
and as the body of the request
