FROM python:3.9-slim

# Install required Python packages
RUN pip install Flask matplotlib pandas seaborn

# Copy the entire repository into the container
COPY . /app

# Set the working directory to the new directory
WORKDIR /app

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "plot_runner.py"]