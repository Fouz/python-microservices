# Python Microservice

A basic CRUD web application that implements microservices architecture in python with Django, Flask, RabbitMQ and React. That allows user to create product with title and image link and 'like' the products.

Both Django and Flask are spawn with docker-compose as different isolated microservices eatch with it's own database. Django microservice exposes the API to allow user to Create, Read, Update and Delete products. While Flask microservice exposes the API to allow user to like the product. Both microservices will be communicating and maintaining data consistency via RabbitMQ.

## Tech Stack

    * React - Frontend framework
    * TypeScript - React UI framework
    * Django - Backend framework
    * Flask - Micro web framework
    * RabbitMQ - Message broker
