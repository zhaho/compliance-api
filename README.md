


# What is Compliance-API?

*Compliance-API for seamless tracking and management of compliance hosts through a versatile set of endpoints, allowing CRUD operations and detailed filtering based on services, environments, owners, and teams.*

# Features

* Simple overview of all your hosts in your environment.

# Prerequisite

* Docker
* Docker Compose

# Run

```bash
git clone https://github.com/zhaho/compliance-api.git
cd compliance-api && cp src/assets/_remove_.env ./.env # Edit .env as your liking
docker-compose up
```

# How to use the Compliance-API

1. Create a team
2. Create hosts related to that team
3. Create services related to that host

