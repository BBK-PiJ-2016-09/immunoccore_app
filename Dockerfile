FROM python:3.7

COPY ./immunocore /immunocore
RUN cd /immunocore && \
    python setup.py install && \
    chmod 755 /docker-entrypoint.sh

ENTRYPOINT ["/immunocore/docker-entrypoint.sh"]
