# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Install necessary packages and set noninteractive frontend
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y apt-utils fortune-mod cowsay netcat-openbsd && \
    apt-get clean

# Copy application script into the container
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh

# Expose port
EXPOSE 4499

# Run the application
CMD ["/app/wisecow.sh"]

