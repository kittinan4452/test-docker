FROM python:3.13
WORKDIR /kittinan/app
COPY requirements.txt .
RUN pip indtsll --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python" , 'app.py' ]
