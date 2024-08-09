FROM python:3.11.0

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]