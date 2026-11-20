# Group Project - Monitor a Web App and Detect Attacks

Final project for CS 457/557 exploring how to attack and defend a small web application environment.

## BBS
The basic buletin board app is implemented. For now just run it with `python -m bbs`.
I will implement docker soon.

### Database Schema
Store posts in db as
id (pk), user (fk -> users.user), date, content

Store users in db as
user (pk), password