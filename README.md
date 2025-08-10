Linux Infrastructure Automation Lab

This project is a personal home lab designed to demonstrate core DevOps and MLOps skills, including infrastructure automation, container-based application deployment, and continuous monitoring. It serves as a practical environment for learning and showcasing hands-on experience with industry-standard tools.

⚙️ Technologies Used

    Ansible: For Infrastructure as Code (IaC) and configuration management.

    Docker & Docker Compose: To containerize applications and orchestrate the monitoring stack.

    Prometheus: For collecting time-series metrics from virtual machines.

    Grafana: For visualizing metrics and creating dashboards.

    Linux (Ubuntu): The operating system for the virtual machines.

    KVM/QEMU: The hypervisor used for creating the virtual machines.

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

➡️ Next Steps: Phase 4 - CI/CD with GitHub Actions

The project will be expanded to include Continuous Integration and Continuous Deployment (CI/CD). A GitHub Actions workflow will be configured to automatically build and push new Docker images and trigger the Ansible deployment playbook upon code changes.