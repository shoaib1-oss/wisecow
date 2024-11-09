# Use a lightweight base image
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay netcat && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy the wisecow.sh script into the container
COPY wisecow.sh .

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the application's port
EXPOSE 4499

# Start the application
CMD ["./wisecow.sh"]
