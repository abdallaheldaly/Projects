# Power_Bi_Diploma
<div>
    <h3>A grant provided by Creativa Innovation Hubs, which is affiliated with ITIDA</h3>
    <h3>This is the code for my lectures, and you can find the recording of the lectures on the <a href="https://t.me/+KaHzQw7wwDs5MWY0">Telegram</a> group</h3>
    <h5>the solution method on my ways</h5>
</div>

How to Run The app with Docker

First, you will download <a href="https://docs.docker.com/engine/install/">Docker</a></h3> from the official website appropriate for your operating system

Build the docker image

 ## $ docker build .
 Now that your docker image is created you can see them with,

 ## $ docker images
 IMAGE ID like what "9d58fedf0d56"
 You can start the Jupyter server with,

 ## $ docker run -p 8888:8888 "Put you IMAGE ID"

Your notebooks are now acessible on http://127.0.0.1:8888 or http://127.0.0.1:8888/lab as usual

For your information, docker is not in the course outline
