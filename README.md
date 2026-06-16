# Temperature Sensor Data Pipeline with ROS 2

## Project Overview
Built an end-to-end sensor data pipeline using ROS 2. A Raspberry Pi publishes temperature sensor data, which is received and logged by a subscriber on a laptop. The collected data is then analyzed and visualized using Python and Jupyter notebooks. Docker was used to maintain a reproducible ROS 2 Jazzy development environment on Ubuntu 26.

This project demonstrates practical experience relevant to simulation analysis and test engineer roles, including sensor data handling, ROS 2 communication, data analysis, and reproducible development workflows.

## Motivation
- Gain hands-on experience with ROS 2 publisher/subscriber nodes and architecture
- Analyze real sensor data
- Demonstrate and practice data analysis and visualization
- Use Docker to solve ROS 2 version and environment challenges, learn about containers
- Setup and use Linux OS

## Technical Approach

### Hardware & Setup
- Raspberry Pi running ROS 2 node as a publisher for temperature sensor data (OS:Ubuntu 24)
- Ubuntu latop running a subscriber/client that queries temperature every 30 seconds
- Docker container used to run ROS 2 Jazzy on laptop (required due to Ubuntu 26 host)

### Software & Tools
- **ROS 2**: Custom publisher and subscriber nodes for sensor data
- **Python + Jupyter**: Data analyssis, processing, visualization
- **Docker**: Reproducible development environment for ROS 2 Jazzy

## Key Results/Skills Demonstrated
- Successfully implemented ROS 2 communication between Raspberry Pi and laptop using custom nodes
- Collected and logged time-series temperature data
- Created clear visualizations and analysis using Jupyter notebooks and Python scripts
- Maintained a reproducible environment using Docker

##Skills Demonstrated 
- ROS 2 (publisher/subscriber, topics, custom nodes)
- Python data analysis and visualization (matplotlib, pandas, Jupyter)
- Docker for development and environment management
- Linux proficiency and virtual environment setup/use
- Sensor data handling and time-series analysis

## Repository Contents
- 'notebooks/' - Jupyter notebooks for data analysis and graphing
- 'code/' - Python scripts (publisher, subsciber, graphing)
- 'docs/' - Exported HTML verion of the analysis notebook
- 'images/' - Physical setup, plots

## Exported Notebook
View the full Jupyter notebook analysis here:
[graph_jupyter_explore.html](docs/graph_jupyter_explore.html)
