# Receipt Processor

A webservice written with FastAPI to process a receipt and determine a point value for that receipt. The receipt is entered into in-app memory with a POST method, and points for a specific receipt in memory are calculated after making a GET request for that receipt (by ID).

A Dockerfile is included in this project. You must have Docker installed to run a Docker container of this app. To build the image, run `docker build -t myimage .`. To run a container from that image (in the example, the name is `myimage`), run `docker run -d --name mycontainer -p 8000:8000 myimage`.
