# Network Security & Homo-Fork Project

This project involves running a network security analysis environment using Docker, Firmadyne, and a Go-based application named `Homo-Network`. Below are the steps required to set up and run the project.

## Requirements

- Docker & Docker Compose
- Go (Golang)
- Telnet client
- Git (optional)
- Firmadyne (cloned recursively to the home directory, as specified in its GitHub page)
- Homo-Network (publicly available on GitHub). In it's configuration file, the IP address for the CnC must be changed to 0.0.0.0.

### Note

This setup was tested on Kali virtual machines, and assumes that the host has the IP 10.0.2.15, which is the default in the Kali image. To run the setup on a different distribution, the IP can be added manually to the VM's interfaces.

## Setup & Run

### 1. Build and Start Docker Containers

Open a terminal and run the following command:

```bash
cd ~/NetworkSecurity/wnap320
./setup.sh
cd ..
docker-compose up
```

### 2. Access the Firmadyne Docker Container

Open a new terminal
 
```bash
cd ~/NetworkSecutiry
docker exec -it networksecurity_firmadyne_1 /bin/bash
cd firmadyne
./scratch/1/run.sh
```

### 3. Run Homo-Network

Open a new terminal

```bash
cd /Homo-Network
go run .
```

### 4. Infect the Network

Open a new terminal

```bash
cd ~/NetworkSecurity
bash infectNetwork.sh
```

### 5. Connect Via Telnet

Open a new terminal 

```bash
telnet 127.0.0.1 1234
Login : root
Password : root
bots
methods
!tcpmix
```

