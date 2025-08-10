Linux Infrastructure Automation Lab

This project is a personal home lab designed to demonstrate core DevOps and MLOps skills, including infrastructure automation, container-based application deployment, and continuous monitoring. It serves as a practical environment for learning and showcasing hands-on experience with industry-standard tools.

⚙️ Technologies Used

    Ansible: For Infrastructure as Code (IaC) and configuration management.

    Docker & Docker Compose: To containerize applications and orchestrate the monitoring stack.

    Prometheus: For collecting time-series metrics from virtual machines.

    Grafana: For visualizing metrics and creating dashboards.

    Linux (Ubuntu): The operating system for the virtual machines.

    KVM/QEMU: The hypervisor used for creating the virtual machines.

    GitHub Actions: For building Continuous Integration/Continuous Deployment (CI/CD) pipelines.

🚀 Phase 1: SysAdmin & DevOps Lab

In this phase, a foundational Linux environment was built and automated. The key accomplishments include:

    Infrastructure as Code (IaC): Used Ansible playbooks to automatically provision and configure two virtual machines (web-server-vm and db-server-vm) with essential services like Nginx and PostgreSQL.

    Containerization & Monitoring: Deployed a monitoring stack using Docker Compose, consisting of Prometheus for data collection and Grafana for visualization.

    End-to-End Monitoring: Configured Prometheus to scrape system metrics from the VMs using Node Exporter, demonstrating an end-to-end monitoring solution.

🚀 Phase 2: MLOps Expansion

This phase expanded the project to include MLOps principles, focusing on containerizing a machine learning application.

🚀 Phase 3: MLOps Deployment & Automation

This phase focused on the automated deployment of a containerized machine learning application. The key accomplishments include:

    Application Containerization: The machine learning model was containerized into a Flask web application, allowing it to run as a persistent service.

    Automated Deployment with Ansible: An Ansible playbook was created and used to automate the entire deployment pipeline. This included logging into Docker Hub, pulling the latest application image, and starting the container on a dedicated virtual machine.

    Functional Verification: The successful deployment was verified by accessing the application's homepage and using a curl command to send a POST request to the /predict endpoint, confirming the model was functional and accessible.

🚀 Phase 4: CI/CD with GitHub Actions

This phase integrated Continuous Integration and Continuous Deployment (CI/CD) into the project. The key accomplishments include:

    Automated Workflow: A GitHub Actions workflow was configured to automatically trigger the entire deployment process upon a git push to the main branch.

    End-to-End Pipeline: The workflow automatically built a new Docker image, pushed it to Docker Hub, and then executed the Ansible playbook to pull the latest image and deploy it to the virtual machine.

    Increased Efficiency: This pipeline eliminates manual steps, enabling faster and more reliable delivery of code changes to production.

➡️ Next Steps: Phase 5 - Kubernetes Integration

The project will be expanded to include container orchestration. The existing Docker container will be deployed using Kubernetes, demonstrating a more scalable and resilient deployment strategy.