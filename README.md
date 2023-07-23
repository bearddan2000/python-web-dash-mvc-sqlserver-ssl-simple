# python-web-dash-mvc-sqlserver-ssl-simple

## Description
Creates a small database table `dog`
for dash project.

Sql server uses self-signed ssl.

## Tech stack
- python
  - dash
  - sqlalchemy
  - pandas

## Docker stack
- alpine:edge
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- [Avaible at](http://localhost)

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Interactive dash](https://github.com/plotly/dash-recipes/blob/master/dash_sqlite.py)
- [Dash table prop](https://stackoverflow.com/questions/69664921/plotly-dash-table-applies-border-radius-only-on-one-side)
