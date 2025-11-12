# ˚₊‧꒰ა PSUSphere ໒꒱ ‧₊˚
*Your Student Management System for Palawan State University ⋆.*

![Django](https://img.shields.io/badge/Django-4.2.16-pink.svg) 
![Python](https://img.shields.io/badge/Python-3.11-ff69b4.svg) 
![Docker](https://img.shields.io/badge/Docker-Ready-pink.svg) 
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-ff69b4.svg)

## ꣑ৎ About   

This web application is for managing **Colleges, Programs, Organizations, Students, and Memberships** with an easy-to-use Django Admin interface and Faker-powered data seeding.


---

## ꣑ৎ Features
- Manage **Colleges** with created/updated timestamps  
- Manage **Programs** linked to Colleges  
- Manage **Organizations** with descriptions and college affiliations  
- Manage **Students** with IDs, full names, and academic programs  
- Manage **Organization Memberships** linking Students to Organizations  
- Custom **Django Admin** dashboards for better navigation  
- Seeder command (`python manage.py create_initial_data`) to generate test data using Faker  

---

## ꣑ৎ Technology Stack

* **Backend**  Django 4.2.16, Python 3.11 

* **Frontend** Bootstrap 5, HTML5, CSS3 

* **Database** SQLite

* **Container** Docker, Docker Compose

* **Authentication** Django AllAuth

---

## ꣑ৎ Setting Up

### Pre-requisites:
- **Docker** installed on the target machine
- **Docker Compose** (included with Docker Desktop)
- Internet connection to pull the Docker image

### i. Check if Docker is installed 𐔌՞ ܸ.ˬ.ܸ՞𐦯
```
docker --version 
```
### ii. Install Docker Desktop ⋆˚✿˖°
- Download from [docker.com](https://www.docker.com/products/docker-desktop)
- Run the installer and follow setup instructions
- For Windows: Enable WSL 2 during installation

### iii. Pull the Image ⋆˚꩜｡
On the target machine: 
```
docker pull yourusername/django-app:latest
```
### iv. Create Project Directory ⋆˚࿔
```
mkdir psusphere-docker
cd psusphere-docker
```

### v. Create docker-compose.yml ᝰ.ᐟ
Create a file named docker-compose.yml with this content:
```
services:
  web:
    image: sryea/psusphere:v1.1
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    ports:
      - "8000:8000"
    volumes:
      - django_data:/app
    environment:
      - DEBUG=1
      - USE_SQLITE=true
      - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
      - SITE_ID=2

volumes:
  django_data:
```

### vi. Run the Application ୭ ˚. ᵎᵎ
```
docker compose up -d
```
### vii. Access the Application (˶ˆᗜˆ˵)
Open your browser and go to: http://localhost:8000

The PSUSphere application should be running  ദ്ദി ˉ͈̀꒳ˉ͈́ )✧

---
## ꣑ৎ Authors
<table> 
    <tr> 
        <td align="center"> 
            <img src="https://avatars.githubusercontent.com/Sr-ea" width="100" style="border-radius: 50%; border: 3px solid pink;"> 
            <br> 
            <b>Rhea Lee Salonoy</b> 
            <br> 
            <small>202380016@psu.palawan.edu.ph</small> 
            <br> 
            <a href="https://www.facebook.com/R04.ji">Facebook</a>  ★
            <a href="https://github.com/Sr-ea"> Github</a> 
        </td> 
        <td align="center"> 
            <img src="https://avatars.githubusercontent.com/Nicholohq" width="100" style="border-radius: 50%; border: 3px solid pink;"> 
            <br> 
            <b>Nicholo Luigi Dela Rosa</b> 
            <br> 
            <small>202380063@psu.palawan.edu.ph</small> 
            <br> 
            <a href="https://www.facebook.com/ksnekreik23">Facebook</a> ★
            <a href="https://github.com/Nicholohq">Github</a> 
        </td> 
    </tr> 
</table>