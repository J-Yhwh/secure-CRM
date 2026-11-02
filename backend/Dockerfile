

# ---------- build stage ----------
FROM python:3.11-slim AS build

WORKDIR /app

# install system deps needed for some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- runtime stage ----------
FROM python:3.11-slim

WORKDIR /app

# copy installed packages from build stage
COPY --from=build /root/.local /root/.local

# copy application code
COPY . .

# make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
