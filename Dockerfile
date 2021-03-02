FROM sphinxdoc/sphinx

COPY ./ ./
RUN rm -r docs/build

RUN pip install sphinx_rtd_theme
RUN pip install .

RUN cd docs && make html

FROM nginx:alpine
ADD docs/build/html /usr/share/nginx/html