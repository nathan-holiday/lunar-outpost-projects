# Temperature Sensor Data Pipeline with ROS 2

## Project Overview
Built an end-to-end sensor data pipeline using ROS 2 on a Raspberry Pi. A custom ROS 2 Service runs on the Raspberry Pi to provide temperature readings from a DS18B20 sensor. A Service Client on a laptop queries the service every 30 seconds to collect and log temperature data. The collected data is then analyzed and visualized using Python and Jupyter notebooks. Docker was used to run ROS 2 Jazzy in a reproducible development environment on Ubuntu 26.

This project demonstrates practical experience relevant to simulation analysis and test engineer roles, including sensor data handling, ROS 2 communication, data analysis, and reproducible development workflows.

## Motivation
- Gain hands-on experience with ROS 2 publisher/subscriber nodes and architecture
- Analyze real sensor data
- Demonstrate and practice data analysis and visualization
- Use Docker to solve ROS 2 version and environment challenges, learn about containers
- Setup and use Linux OS

## Technical Approach

### Hardware & Setup
- Raspberry Pi with DS18B20 temperature sensor running ROS 2 node as a service for temperature sensor data (OS:Ubuntu 24)
- Ubuntu latop running a client node that queries temperature every 30 seconds
- Docker container used to run ROS 2 Jazzy on laptop (required due to Ubuntu 26 host)

### Software & Tools
- **ROS 2**: Custom publisher and subscriber nodes for sensor data
- **Python + Jupyter**: Data analyssis, processing, visualization
- **Docker**: Reproducible development environment for ROS 2 Jazzy

## Key Results/Skills Demonstrated
- Successfully implemented ROS 2 communication between Raspberry Pi and laptop using custom Service/Client nodes
- Collected and logged time-series temperature data
- Created clear visualizations and analysis using Jupyter notebooks and Python scripts
- Maintained a reproducible environment using Docker

##Skills Demonstrated 
- ROS 2 (services, custom '.srv' and '.msg' files, Python nodes)
- Python data analysis and visualization (matplotlib, pandas, Jupyter)
- Docker for development environments
- Linux proficiency and virtual environment setup/use
- Sensor data handling and time-series analysis

## Repository Structure
- 'notebooks/' - Jupyter notebooks (source '.ipynb' files)
- 'ros2/send_receive/' - Full ROS 2 package with service, scripts
- 'code/' - Additional python scripts
- 'images/'
  - 'physical_setup/' - Photos of the hardware and test setup
  - 'graphs/' - Output graphs and visualizations
- 'docs/' - Exported HTML versions of notebooks
- 'data/' - Data files (e.g. temperature logs)
- 'additional_analysis/' - Additional general data analysis notebooks and telemetry work

## Additional Data Analysis Work
In addition to the main ROS 2 temperature sensor project, I have also worked on general data analysis, including time-series position (XYZ) data visualization using Python and Jupyter notebooks. Examples are available in the 'additional_analysis/' folder.

## Exported Notebook
The full Jupyter notebook analysis is available as an HTML file.
Download it and open it in a web browser to view the rendered notebook with all plots and outputs:

[graph_jupyter_explore.html](docs/graph_jupyter_explore.html)
