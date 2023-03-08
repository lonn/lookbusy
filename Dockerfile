FROM   python:latest
RUN    curl http://www.devin.com/lookbusy/download/lookbusy-1.4.tar.gz | tar xvz && \
       cd lookbusy-1.4 && ./configure && \
       make && make install && cd .. && rm -rf lookbusy-1.4
RUN    pip install Flask
ADD    server.py server.py
EXPOSE 80
CMD    python -u server.py