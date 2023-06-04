# Django DRF Dockerized Project Template

This repository serves as a template for creating a Django REST Framework (DRF) project that is containerized using Docker. It provides a structured starting point for developing Django-based web applications with a RESTful API, allowing for easier setup and deployment.

## Features

- Django 3.x and Django REST Framework (DRF) pre-configured
- PostgreSQL database integration
- Docker and Docker Compose configuration for containerization
- Separation of development and production settings
- Automatic database setup and migrations using Django's `manage.py` commands
- Ready-to-use Django project structure following best practices
- Simple API endpoint for testing purposes
- Customizable and extensible to fit your project's needs

## Prerequisites

Before using this template, ensure that you have the following dependencies installed on your system:

- Docker: [Install Docker](https://www.docker.com/get-started)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

To start a new project using this template, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-project.git
```

2. Navigate into the cloned directory:

```bash
cd your-project
```

3. Create a new Django secret key:

```bash
cp .env.example .env
```

Open the `.env` file and replace the value of `SECRET_KEY` with a randomly generated secret key.

4. Build and run the Docker containers:

```bash
docker-compose up -d --build
```

This command will download the required Docker images, set up the containers, and start the development server.

5. Access the Django application:

You can access the Django application running on `localhost:8000` in your web browser.

6. Test the API endpoint:

A sample API endpoint is available at `localhost:8000/api/`. You can modify or extend it according to your project's requirements.

## Configuration

- **Django Settings**: The project-specific Django settings are located in the `config/settings/` directory. You can modify these files to adjust the project's configuration based on your needs.

- **Database**: By default, this template uses PostgreSQL as the database backend. You can update the database settings in the `.env` file to match your requirements.

- **Docker Configuration**: The Docker configuration files (`Dockerfile` and `docker-compose.yml`) are included in the root directory. If you need to make changes to the container setup or add additional services, you can modify these files accordingly.

## Development Workflow

- During development, you can modify the Django code, and the changes will be automatically detected and applied.
- To stop the development server and the associated containers, use the following command:

```bash
docker-compose down
```

## Deployment

To deploy the project to a production environment, you can use Docker Compose or any other preferred deployment method. Ensure that you update the necessary configurations for a production environment, such as using a secure secret key, configuring HTTPS, and setting up any required production database or caching services.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

This project template is inspired by the excellent Django and Docker tutorials and best practices available in the Django and Docker communities.