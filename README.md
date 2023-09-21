# Provides docker alpine images by framework.

#### Content
- nginx
- python
- Binary
- Golang

#### Support Architecture
- x86_64
- aarch64 / arm64v8

#### Docker image test
- Check Operation
    ```bash
    docker run -d <docker image>
    docker exec -it <docker container image> /bin/sh
    netstat -lntp # check port running 
    curl -o - -I http://localhost:80 # API testing
    ```

####  To display file headers of a elf file.
- command
    ```bash
    readelf -h elf_file
    ```

#### install docker package
- amazon linux 2023 and amazon linux 2
    ```bash
    yum install -y docker       #dnf install -y docker
    systemctl restart docker
    usermod -aG docker ec2-user
    chmod 666 /var/run/docker.sock
    ```

- ubuntu 22.04
    ```bash
    snap install docker
    snap restart docker
    ```

#### Alpine Linux
- gcompat
    ```
    apk add gcompat
    ```
- curl
    ```
    apk --no-cache add curl
    ```