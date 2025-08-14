# Companion
A set of C.R.U.D. operations with the new version of
HPE Networking Central

Installation:

# must have git installed

[Install Git](https://github.com/git-guides/install-git)


# Must have docker and docker compose installed.
[Install Docker Desktop](https://www.docker.com/products/docker-desktop)

Works well with docker-desktop for macbook

```
% git clone https://github.com/xod442/companion.git
% cd companion
companion%  docker-compose up -d
```

Use: localhost:5002


# Create user credentials

- /utilities/get_client_api.py  returns the token for all future api calls.

- /utilities/api_call.py sends the api_method, api_path, and api_data to the pycentral
api endpoint.

- app.py has the flask application routes that are called from the /templates/navbar.html file.
