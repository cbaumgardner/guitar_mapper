# Scale Chart


www.scale-chart.com

> Caveat: I'm a data engineer and not a front end developer, so lower your expectations.


## Steps to run locally (assuming you have Docker already installed)

1) Clone this repo
2) Build the image by running ``docker build -t scale_chart_image .`` in this directory
3) Start the container by running ``docker run --rm -p 4545:4545 --name scale_chart scale_chart_image``
4) Open a browser and go to http://localhost:4545/
5) To restart the container run docker_restart.py

## Deployment

1) Build image. When building an image for linux from a machine with an Apple chip, run the following:

  ``docker buildx build --platform=linux/amd64 -t scale_chart_linux .``

2) Push to Lightsail.

``aws lightsail push-container-image --region us-east-1 --service-name scale-chart --label scale-chart --image scale_chart_linux:latest``
