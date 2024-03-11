# Text Classification Service

This project is a text classification service based on a pretrained NLP model. It allows users to input a sentence and a list of labels, and it returns the predicted label for the input sentence.

## Getting Started

### Prerequisites

- Python 3.9
- Docker

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nagajavisetty/Text-Classification-Service-Deployment-with-Pretrained-NLP-Model.git
   cd Text-Classification-Service-Deployment-with-Pretrained-NLP-Model
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running Locally

1. Start the Flask development server:
   ```bash
   python model.py
   ```

2. Open your web browser and navigate to `http://localhost:80` to access the text classification service.

#### Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t {your-image-name:tag} .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 80:80 {your-image-name:tag}
   ```

3. Access the text classification service by navigating to `http://localhost:80` in your web browser.

### Pushing Docker image to Docker Hub

1. Open Docker Hub on a web browser and create a repository with the same name you gave when creating the Docker image.
2. Push the local Docker image to Docker Hub using the following command:
   ```bash
   docker login
   docker push {your-image-name:tag}
   ```

### Pulling the Docker Hub image to EC2 Instance

1. Create a new EC2 instance in AWS and open EC2 CLI.
2. Log in to Docker with the following command:
   ```bash
   docker login
   ```
3. Pull the image from Docker Hub using the following command:
   ```bash
   docker pull {your-image-name:tag}
   ```

## Create a Load Balancer

1. Navigate to the AWS Management Console and open the EC2 dashboard.
2. In the EC2 dashboard, under Load Balancing, select 'Load Balancers' and click on 'Create Load Balancer'.
3. Choose the load balancer type (e.g., Application Load Balancer).
4. Configure the load balancer settings, including listeners, availability zones, security settings, and routing configuration.
5. Complete the load balancer creation process by following the on-screen instructions.

## Create Auto Scaling

1. In the AWS Management Console, open the EC2 dashboard.
2. Under Auto Scaling, select 'Auto Scaling Groups' and click on 'Create Auto Scaling Group'.
3. Specify the launch configuration for the auto scaling group, including the EC2 instance type, AMI, key pair, security groups, and user data.
4. Configure the auto scaling group settings, including the minimum, maximum, and desired capacity, scaling policies, cooldown periods, and health checks.
5. Complete the auto scaling group creation process by following the on-screen instructions.

``` 


This README provides detailed instructions on setting up the project, running it locally, deploying it with Docker, pushing the Docker image to Docker Hub, pulling the Docker image to an EC2 instance, and creating a load balancer and auto-scaling in AWS. You can fill in the placeholders with your specific image names, tags, and AWS configuration details.
