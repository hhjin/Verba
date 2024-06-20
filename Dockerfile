FROM python:3.11
WORKDIR /Verba
COPY . /Verba
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
&& pip install -e .
EXPOSE 8000
CMD ["verba", "start","--port","8000","--host","0.0.0.0"]
