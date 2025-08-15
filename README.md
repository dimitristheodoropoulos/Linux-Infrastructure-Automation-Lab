Linux Infrastructure Automation Lab

This project is a personal home lab designed to demonstrate core DevOps and MLOps skills, including infrastructure automation, container-based application deployment, and continuous monitoring. It serves as a practical environment for learning and showcasing hands-on experience with industry-standard tools.

⚙️ Technologies Used

    Ansible: For Infrastructure as Code (IaC) and configuration management.

    Docker & Docker Compose: To containerize applications and orchestrate the monitoring stack.

    Kubernetes: For container orchestration, managing scalable and resilient application deployments.

    Minikube: A tool for running a single-node Kubernetes cluster locally.

    Prometheus: For collecting time-series metrics from virtual machines.

    Grafana: For visualizing metrics and creating dashboards.

    Linux (Ubuntu): The operating system for the virtual machines.

    KVM/QEMU: The hypervisor used for creating the virtual machines.

    GitHub Actions: For building Continuous Integration/Continuous Deployment (CI/CD) pipelines.

    ArgoCD: The GitOps tool used for automated application deployment.

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

🚀 Phase 5: Kubernetes Integration

This phase expanded the project to include container orchestration. The key accomplishments include:

    Cluster Setup: A local Kubernetes cluster was set up using Minikube, providing a robust environment for managing containerized applications.

    Declarative Deployment: The Docker container for the ML application was deployed using Kubernetes Deployment and Service objects, demonstrating a declarative and scalable deployment strategy.

    Service Exposure: The application was exposed to the network using a Kubernetes NodePort Service, making it accessible from outside the cluster.

🚀 Phase 6: GitOps with Kubernetes & ArgoCD

This final phase completed the end-to-end automation cycle by implementing a GitOps workflow. The key accomplishments include:

    ArgoCD Integration: Deployed ArgoCD to the Kubernetes cluster to act as the Continuous Deployment (CD) tool.

    GitOps Workflow: Configured ArgoCD to continuously monitor the ml-app-k8s-manifests repository, ensuring that any changes to the Kubernetes manifests are automatically and declaratively applied to the cluster.

    End-to-End Pipeline: With this setup, a git push to the main branch now triggers a complete, automated deployment: a new Docker image is built, pushed to Docker Hub, and ArgoCD automatically syncs the new image tag to the running Kubernetes pod.

    Verification: The successful deployment was verified by checking ArgoCD's UI for a Healthy status and confirming application functionality with a curl command.

🚀 Phase 7: Advanced MLOps and LLM Integration

This phase focuses on enhancing the project with modern LLM capabilities and advanced MLOps practices. The key accomplishments and next steps are:

    LLM Integration: Integrated a large language model (LLM) via the Google Gemini API into the application, transforming it from a simple ML model to a powerful AI-driven service.

    Application Scaling: Manually scaled the application from a single pod to multiple replicas using kubectl, demonstrating the ability to manage application capacity and resilience.

    Next Steps (Planned):

        Automated Scaling: Implement a Horizontal Pod Autoscaler (HPA) to automatically adjust the number of pods based on resource usage.

        Monitoring Integration: Extend the existing Prometheus and Grafana setup to collect and visualize real-time metrics from the ml-app pods.

        Infrastructure as Code (IaC): Use Terraform to programmatically manage the Minikube cluster.

🔖 Project Versions

    v1.0-phase6: This tag represents the project's state at the completion of the GitOps phase, before the LLM integration work began.