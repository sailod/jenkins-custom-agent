FROM centos:7

RUN yum update -y
RUN yum install -y python3 zip unzip
ENV VERSION=1.2.0
COPY zip_job.py /tmp
CMD  "cat /etc/os-release && test -f /tmp/zip_job.py"
