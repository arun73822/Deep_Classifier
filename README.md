# Deep Clasifier project
  # this is my first cnn project

# Iam creating the .gitignore and license file after pull the changes to vs code iam getting error that is 
# "fatal: unable to access 'https://github.com/arun73822/Deep_Classifier.git/': Could not resolve host:   github.com." 
# to resolve this problem goto to repository click on settings and select the option is 
#      Always suggest updating pull request branches 
# after that pull the changes from vscode it works fine.

# workflow
1.Update config.yaml
2.Update secrets.yaml [Optional]
3.Update params.yaml
4.Update the entity
5.Update the configuration manager in src config.
6.Update the components
7.Update the pipeline
8.Test run pipeline stage
9.run tox for testing your package
10.Update the dvc.yaml
11.run "dvc repro" for running all the stages in pipeline


![img]( https://github.com/arun73822/Deep_Classifier/blob/master/Data%20Ingestion%402x%20(1).png )



# to run dvc.yaml
dvc init
dvc repro 
dvc dag

# environment
rm -rf ./env/  --> forcefully remove the environment
rm ~/.condaarc --> Any unwanted font display in the terminal
conda config --set env_promt "({name})"