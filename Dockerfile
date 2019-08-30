#Download base image ubuntu 16.04
FROM ubuntu:bionic
 
# Update Software repository
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get update
RUN apt-get -y install git-core    
RUN apt-get install -y wget ca-certificates
# RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
# RUN  sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib
RUN git clone https://github.com/Shritesh99/Kleos2k18-server
RUN apt-get install -y python3-pip
RUN cd Kleos2k18-server
RUN pip3 install -r requirements.txt
RUN su - postgress 
RUN createuser admin 
RUN createdb kleos --owner admin
RUN psql -c "ALTER USER admin WITH PASSWORD '123'"
RUN exit
RUN python3 manage.py migrate
# Configure Services and Port
# COPY start.sh /start.sh
CMD ["python3 manage.py runserver"]
 
# EXPOSE 80 443