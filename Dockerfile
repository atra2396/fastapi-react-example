FROM node:17-alpine as ui-build
WORKDIR /app
COPY ui/package.json ui/package-lock.json ./
RUN npm ci
COPY ui/ .
RUN npm run build

FROM python:3.9-slim-buster as final
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY --from=ui-build /app/ ./ui
CMD uvicorn --host 0.0.0.0 main:app