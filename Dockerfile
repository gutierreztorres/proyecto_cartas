# Use Python slim image
FROM python:3.13-slim-bullseye

# Install system dependencies and ensure all packages are up-to-date
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create directory for temporary files
RUN mkdir -p /dev/shm

# Create non-root user
RUN useradd -m -r appuser && \
    mkdir /django_app && \
    mkdir -p /django_app/staticfiles && \
    chown -R appuser:appuser /django_app

# Set working directory
WORKDIR /django_app

# Set environment variables for Python and Django optimization
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/django_app
ENV DJANGO_SETTINGS_MODULE=configuracion.settings

# Install Python dependencies
COPY requirements.txt /django_app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy specific application files and folders
COPY --chown=appuser:appuser manage.py /django_app/

COPY --chown=appuser:appuser cartas/ /django_app/cartas/
COPY --chown=appuser:appuser respuesta/ /django_app/respuesta/
COPY --chown=appuser:appuser configuracion/ /django_app/configuracion/

COPY --chown=appuser:appuser db.sqlite3 /django_app/db.sqlite3


# Create staticfiles directory (will be populated during collectstatic)
RUN mkdir -p /django_app/staticfiles

RUN mkdir -p /django_app/static

# Switch to non-root user
USER appuser
 
# Expose the application port
EXPOSE 8000 
 
# Start the application using Gunicorn with adjusted timeouts and worker configuration
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--workers=2", "--threads=2", "--worker-class=sync", "--timeout=120", "--max-requests=1000", "--max-requests-jitter=50", "--worker-tmp-dir=/dev/shm", "config.wsgi:application"]
