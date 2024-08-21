# Creates a container to update a public IP address
# of an a-record managed by GoDaddy.
# All parameters are passed via env vars
# Env var examples:
#   GODADDY_KEY=<ACCESS KEY HERE>
#   GODADDY_SECRET=<SECRET KEY HERE>
#   GODADDY_DOMAIN_LIST=mydomain.org,myotherdomain.org
#   GODADDY_A_RECORD_LIST=updatertest,updatertest2

FROM python:3

# Setup s6-overlay
ARG S6_OVERLAY_VERSION=3.2.0.0

# RUN apt-get update && apt-get install -y nginx xz-utils
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-noarch.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-noarch.tar.xz
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-x86_64.tar.xz /tmp
RUN tar -C / -Jxpf /tmp/s6-overlay-x86_64.tar.xz

ADD GoDaddyUpdater.py /usr/bin/GoDaddyUpdater.py
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD s6-overlay /etc/s6-overlay

ENTRYPOINT ["/init"]
CMD ["sleep", "infinity"]
