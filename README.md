# Group Project - Monitor a Web App and Detect Attacks

Final project for CS 457/557 exploring how to attack and defend a small web application environment.

## BBS
The basic buletin board app is implemented. Build with `docker compose build` and 
run with `docker compose up`

### Database Schema
Store posts in db as
id (pk), uid (fk -> users.id), content

Store users in db as
id (pk), username, password

### Vulnerabilities
The username and password are stored in a plaintext cookie, which makes MitM attacks
easy. 

The post creation process is subject to SQL injection.