# Introduction 
Add some product introduction

# Getting Started (manual build process)

1. Clone the repo to local machine
```bash
git clone https://github.com/wojiushizzl/yolov8_streamlit.git
# enter your PAT (personal access token) here if git asks for access
```
2. Run docker build
```bash
# sudo is optional
(sudo) docker build -t streamlit .
# use below command to check docker images
(sudo) docker image ls
```
3. Docker run
```bash
# sudo is optional
(sudo) docker run -d -p 80:8501 streamlit -> expose the application on port 80
# use below command to see running containers
(sudo) docker ps
```

4. Access to the application
depend on your host IP, access the application via host_ip:80
