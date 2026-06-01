terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "demo_net" {
  name = "grnet-demo-network"
}

resource "docker_container" "demo_container" {
  name  = "grnet-demo"
  image = "alpine:latest"
  command = ["sleep", "infinity"]
  networks_advanced {
    name = docker_network.demo_net.name
  }
}
