Linux Infrastructure Automation Lab

This project is a personal home lab designed to demonstrate core DevOps skills, including infrastructure automation, container-based application deployment, and continuous monitoring. It serves as a practical environment for learning and showcasing hands-on experience with industry-standard tools.

⚙️ Technologies Used

    Ansible: For Infrastructure as Code (IaC) and configuration management.

    Docker & Docker Compose: To orchestrate the monitoring stack.

    Prometheus: For collecting time-series metrics from virtual machines.

    Grafana: For visualizing metrics and creating dashboards.

    Linux (Ubuntu): The operating system for the virtual machines.

    KVM/QEMU: The hypervisor used for creating the virtual machines.

🚀 Phase 1: SysAdmin & DevOps Lab

In this phase, a foundational Linux environment was built and automated. The key accomplishments include:

    Infrastructure as Code (IaC): Used Ansible playbooks to automatically provision and configure two virtual machines (web-server-vm and db-server-vm) with essential services like Nginx and PostgreSQL.

    Containerization & Monitoring: Deployed a monitoring stack using Docker Compose, consisting of Prometheus for data collection and Grafana for visualization.

    End-to-End Monitoring: Configured Prometheus to scrape system metrics from the VMs using Node Exporter, demonstrating an end-to-end monitoring solution.

➡️ Next Steps: Phase 2 - MLOps Expansion

The project will be expanded to include MLOps principles, focusing on containerizing a machine learning application, automating its deployment with Ansible, and setting up a CI/CD pipeline using GitHub Actions.
