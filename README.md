# DSC180BProject

This is the Wikipedia project working on its performance on providing COVID-19 pandemic information

### Project Team Members:
- Yiheng Ye, yiy291@ucsd.edu
- Gabrielle Avila, ggavila@ucsd.edu
- Michael Lam, mel157@ucsd.edu

### Requirements:
- python 3.8
- pandas 1.1.0

### Code, Purpose, and Guideline:

- run.py: If target='data': Get top 1000 popular articles relating COVID-19 from Wikipedia. Get the pageview data for them in 2020.
          If target='test': Runs test program about data and getting pageview on the test data.
- elt.py: the library for the data pipeline, see the documentation for detailed functions of every function writtened. Basically
          these functions are used to fulfill the job done in run.py.
- config/data-params.json: it stores the links of the source data as well as the output path for raw data.
- code in src/data: the source code to fulfill the functions about processing data. The current usable files are get_data.py(getting top1000 articles'
  basic information) and get_apipageview.py(getting pageview from given article information csvs)

### Notebooks
The notebook file is primary serving as our original test base for code development. Additionally, it also has a notebook called Project EDA Single Webpage.ipynb which we investigate "COVID-19 pandemic data" page deeply.

## Responsibilities:
- Yiheng Ye set up the structure of the project and the structure of run.py. He also wrote get_data.py and get_apipageview.py and put them into the etl.py
- Gabrielle Avila constructed our report and made deep analysis into the "COVID-19 pandemic data" page.