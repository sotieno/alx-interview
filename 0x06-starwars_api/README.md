# 0x0F-starwars_api

This script prints all characters of a Star Wars movie using the [Star Wars API](https://swapi-api.alx-tools.com/) and request module:

* The first positional argument passed is the movie ID - example: 3 = “Return of the Jedi”

* Displays one character name per line in the same order as the "characters" list in the /films/ endpoint

## Requirements

Install Node 10 

```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Install semi-standard | [Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

Install request module and use it | [Documentation](https://github.com/request/request)

```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
