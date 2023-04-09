# python-web-api-flask-basic-auth--mysql-chained-sql-pop

## Description
Creates an api of `pop` by using chained sql functions for a flask project.
Has the ability to query by parameters.
If path is not found, will default to 404 error.

Requires basic authentication for CRUD opperations.

| username | password |
| -------- | -------- |
| *user* | *pass* |


Remotely tested with *testify*.

## Tech stack
- python
  - flask
  - sqlalchemy
  - testify
  - requests

## Docker stack
- python:latest
- mariadb:latest

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop
  - Schema id, name, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/pop/<id> -u 'user:pass'
  - Read: http://localhost/pop/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/pop/<id>/<name>/<color> -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/pop/<id> -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
