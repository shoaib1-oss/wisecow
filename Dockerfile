# Use Ubuntu 22.04 as base
FROM ubuntu:22.04

# Set noninteractive frontend and add /usr/games to PATH
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/games:${PATH}"

# Install required packages
RUN apt-get update && apt-get install -y \
    bash \
    cowsay \
    fortune-mod \
    netcat-openbsd \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /home/ubuntu/wisecow

# Copy the application script
COPY wisecow.sh .

# Make script executable
RUN chmod +x wisecow.sh

# Expose the application port
EXPOSE 4499

# Run the application
ENTRYPOINT ["./wisecow.sh"]
