# Iran Assistance Project

## Overview

The Iran Assistance Project is a Django-based web application designed to manage insurance-related data and services. It provides a user-friendly interface for providers to access their insurance information

## Tech Stack

- **Backend**: Django
- **Database**: PostgreSQL (or SQLite for development)
- **Containerization**: Docker

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop) installed on your machine.

### Clone the Repository

```bash
git clone https://github.com/MarziehKaviani/IranAssistanceProject.git
cd IranAssistanceProject
```

### Build the Docker Image

```bash
docker build -t iran_assistance_app .
```

### Run the Application

\`\`\`bash
docker run -d -p 8000:8000 iran_assistance_app
\`\`\`

### Access the Application

Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

" > README.md
