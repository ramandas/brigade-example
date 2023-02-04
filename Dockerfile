FROM python:3.8.12-alpine3.15

RUN mkdir -p /sample
WORKDIR /sample

#RUN pip install flask
COPY ./webApplication1 /sample/
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python","app.py"]