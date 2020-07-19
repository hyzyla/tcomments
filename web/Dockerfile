FROM node:10.16.0

WORKDIR usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json

RUN npm install

COPY . /usr/src/app/.

RUN npm run build
