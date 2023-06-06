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
AzureSparkEurovision/               # Project module
├── code/                           # main entrypoint
│   ├── preprocessing/
│       ├── MultiNested_JSON_Processing_AM.ipynb
│   ├── azure/
│       ├── Azure_Synpase_HTML_DBMS514.html
│       ├── Azure_Synpase_PYTHON_DBMS514.py
│       ├── Azure_Synpase_Notebook_DBMS514.ipynb
├── data/
│   ├── [sample datasets from kaggle]
├── presentation                     # Final Submission
├── reports                          # Mid Term Report
```
### Questions
- Which user has posted the most number of tweets
- Which countries has the most tweets being actively posted
- How many tweets are associates with each hashtags
- For each verified user, what is the percentage of different type of tweets to their overall number of tweets
- (path finding) Display the thread (replies) of tweets (the tweet, time, id, in reply to id, user name with their screen name) posted by user with screen_name “blcklcfr” in the order in which they were posted. [HINT: use tweet’s id to discover the thread]
- Are there any three users A, B, C such that: Any of User A’s tweet/s were replied to by B and C and vice versa, and B has replied to any of C’s tweet/s and vice versa. How many such trios exist? Display each trio with names, screen names of users.

### Data sources
[Kaggle-Twitter Eurovision 2018 Final](https://www.kaggle.com/datasets/patrickjoan/twitter-data-from-2018-eurovision-final)

### Contributors
* [Akshit Miglani](https://www.linkedin.com/in/akshitmiglani/): akshit.miglani09@gmail.com | amiglani@uw.edu 
* [Ameya Bhamare](https://www.linkedin.com/in/ameyabhamare/): ameyarb@uw.edu
* [Anish Dixit](https://www.linkedin.com/in/anish-dixit-aaba4616a/): andixit@uw.edu
* Ananya Bajaj
