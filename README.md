# Azure Cloud Service(DBMS Infrastructure) using Azure Synpase

### Goal
The end product is a cloud based data base management system that was built using Azure Storage, Elastic Compute instance, Synpase Analytics

### Technical Theme 
Multi-Nested JSON Parsing using Spark and running SPARK SQL queries

## Development Environment
*This repo was built using Python 3.10, Azure Workspace, Azure Synapse Analytics*

*Spark Pool Information*
- Name: dbmsspark
- Utilization: 0.00%
- Node size: Medium
- Number of nodes: 3 to 10 nodes
- Apache Spark version: 3.3
- Scala version: 2.12.15
- Python version: 3.10
- Automatic pausing: Enabled (15 min idle)

### Installation instructions

- Request Azure Credentials(200$/student)
- Set up Azure Compute/VM/Machine
- Set up Azure Storage Account
- Create Spark Pool
- Set up Azure Snypase Analytics Platform
- Connect Azure VM, Storage and Analytics through Azure Workspace

### Running the cloud based infrastructure
1. Spin up the Azure Spark pool using "Develop" mode (https://web.azuresynapse.net/) and run the spark cluster using spark pool 
2. Access the Jupyter notebook after the spark pool is up and runnings
3. Create DBMS view and execute queries

### Project structure
```
FitMe/                              # FitMe python module
├── app.py                          # main entrypoint
├── data/
│   ├── [sample datasets from kaggle]
├── analysis/                       # Analysis python module
│   ├── activity_analysis.py        # contains functions for processing activity data
│   ├── calories_analysis.py        # contains functions for processing calories data
│   ├── heartrate_analysis.py       # contains functions for processing heart rate data
│   ├── sleep_analysis.py           # contains functions for processing sleep data
│   ├── steps_analysis.py           # contains functions for processing steps data
```
### Questions

### Data sources

### Contributors
* [Akshit Miglani](https://www.linkedin.com/in/akshitmiglani/): akshit.miglani09@gmail.com | amiglani@uw.edu 
* [Ameya Bhamare](https://www.linkedin.com/in/ameyabhamare/): ameyarb@uw.edu
* [Anish Dixit](https://www.linkedin.com/in/anish-dixit-aaba4616a/): andixit@uw.edu
* Ananya Bajaj
