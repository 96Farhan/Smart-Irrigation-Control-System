# Smart Irrigation Control System

### Quick Deployment

* Update local database of software

```
sudo apt-get update
```

* Uninstall Old Versions of Docker

```
sudo apt-get remove docker docker-engine docker.io
```

* Install Docker

```
sudo apt install docker.io
```

* Start and Automate Docker

```
sudo systemctl start docker

sudo systemctl enable docker
```

* Install docker compose

```
sudo apt install docker-compose
```

* Build docker containers

```
docker-compose build
```

* Run docker containers

```
docker-compose up
```

* Run docker containers in detached mode

```
docker-compose up -d
```
* You can also install dockers by executing following command in project directory:

```
./docker-script.sh
```

### Server

* HTTP URL

```
http://localhost:8000
```

### Rest API

* The evolution of API’s functionality is inevitable, but the headache of maintaining API docs doesn’t have to be. Swagger tools takes the hard work out of generating and maintaining API docs, ensuring documentation stays up-to-date as API evolves.

* Swagger UI allows anyone — development team or end consumers — to visualize and interact with the API’s resources without having any of the implementation logic in place. It’s automatically generated from OpenAPI (formerly known as Swagger) Specification, with the visual documentation making it easy for back end implementation and client side consumption.

* URL to access Swagger REST API

```
http://localhost:8000/swagger/
```

### System Admin Panel

* URL to access PTS Admin Panel

```
http://localhost:8000
```
