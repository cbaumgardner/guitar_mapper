import os

os.system("docker stop scale_chart")
os.system("docker image rm scale_chart")
os.system("docker build -t scale_chart .")
os.system("docker run --rm -p 4545:4545 --name scale_chart scale_chart")