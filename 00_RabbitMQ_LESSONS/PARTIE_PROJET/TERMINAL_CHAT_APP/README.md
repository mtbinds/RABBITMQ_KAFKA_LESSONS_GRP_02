# RabbitMQ Chat Application

![RabbitMQ Logo](https://www.vectorlogo.zone/logos/rabbitmq/rabbitmq-ar21.svg)

This repository contains a simple chat application built with RabbitMQ that allows two users to communicate with each other in real-time.

## Introduction

This project demonstrates how to implement a chat application using RabbitMQ messaging broker in a Node.js environment. In this application, users can exchange messages asynchronously using RabbitMQ queues.

## Getting Started

To run this chat application, follow these steps:

1. **Start RabbitMQ using Docker:** Ensure that Docker is installed on your machine. Open a terminal and run the following command to start RabbitMQ in a Docker container:

    ```bash
    docker run -it -d --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
    ```

    This command will download and start a RabbitMQ container with the management plugin enabled. Port 5672 is used for the AMQP protocol, while port 15672 is used for accessing the RabbitMQ management UI.

2. **Clone the Repository:** Clone this repository to your local machine.

3. **Install Dependencies:** Navigate to the project directory and run the following command to install dependencies:

    ```bash
    npm install
    ```

4. **Start User1 (Publisher):** Open a terminal window/tab, navigate to the project directory, and run the following command:

    ```bash
    node user1.js
    ```

5. **Start User2 (Subscriber):** Open another terminal window/tab, navigate to the project directory, and run the following command:

    ```bash
    node user2.js
    ```

6. **Begin Chatting:** Start typing your messages in each user's terminal window/tab. Messages will be exchanged between users in real-time. You will receive an acknowledgment when the other user receives your message.
