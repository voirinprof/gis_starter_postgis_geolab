FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies for geopandas and psycopg2
RUN apt-get update && apt-get install -y \
  gdal-bin \
  libgdal-dev \
  libpq-dev \
  && rm -rf /var/lib/apt/lists/*

  CMD ["sleep", "infinity"]
