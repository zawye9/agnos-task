# ==========================
# Stage 1 - Builder
# ==========================
FROM python:3.11-slim AS builder

WORKDIR /install

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt

# ==========================
# Stage 2 - Runtime
# ==========================
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy source
COPY . .

ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 3000

# Default command (API)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
