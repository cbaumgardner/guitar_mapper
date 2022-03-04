# Scale Chart

I got tired of googling guitar scales so I made this to create them for me. It's still a work in progress, plenty of enhancements to come.

Steps to run (assuming you have Docker already installed)

1) Clone this repo
2) Build the image by running ``docker build -t scale_chart .`` in this directory
3) Start the container by running ``docker run --rm -p 4545:4545 scale_chart --name scale_chart``
4) Open a browser and go to http://localhost:4545/


If you want to quickly test changes
1) In Pycharm run the following in the Terminal ``export FLASK_APP=scale_chart``
2) Then run ``flask run`` 
3) The output will give a link where you can view the webpage. It is not localhost!
