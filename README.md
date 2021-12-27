# fastapi poc with docker

simple fastapi app to play with docker and fast api mechanics

---

## Technologies

You will need Python 3.9, docker, and docker-compose.

Additionally, see [requirements](./project/requirements.txt) below for required modules.

---

## Setup


```
# create a python 3.9 environment
conda create --name fastapidocker python=3.9 

# activating the environment
conda activate fastapidocker
```

---

## Usage

```
docker-compose up -d --build
docker-compose down -v

```

---

## Contributors

[David Lopez](https://github.com/sububer)

---

## License

[MIT]('./LICENSE')