FROM fedora:40

# Install GUI-related system packages
RUN dnf install -y \
    python3 \
    python3-tkinter \
    python3-pip \
    tk \
    xorg-x11-server-common \
    xorg-x11-xdm \
    xorg-x11-util-macros \
    xorg-x11-xauth \
    xorg-x11-fonts-Type1 \
    xorg-x11-fonts-misc \
    && dnf clean all

# Set display variable for X11
ENV DISPLAY=:0

# Set working directory to inside actual_project
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual project into the container
COPY actual_project/ ./  

# Set the working directory to inside the copied app
WORKDIR /app

# Run the app (RUNME.py is now directly under /app)
CMD ["python3", "RUNME.py"]
