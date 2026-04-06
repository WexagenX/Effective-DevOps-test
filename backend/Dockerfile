FROM python:3.12-slim

# Install Curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app

COPY app.py .

USER appuser

EXPOSE 8080

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 CMD curl -f http://localhost:8080/ || exit 1

CMD ["python", "app.py"]


