# Use a slim version of Python
FROM python:3.11-slim

# Create a non-root user
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Change ownership to the non-root user
RUN chown -R appuser:appgroup /app

# Use the non-root user
USER appuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
