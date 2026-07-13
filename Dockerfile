# Step 1: Base image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy source code
COPY . .

# Step 5: Expose port
EXPOSE 8000

# Step 6: Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
