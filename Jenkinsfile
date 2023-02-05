pipeline {
	agent any
   	stages {
		stage('Creating staging branch') {
			steps {
                		sh 'git checkout dev'
                		sh 'git pull origin dev'
                		echo 'Creating a staging branch'
                		sh  'if [[ $(git branch -l | grep staging) != "" ]];then git branch -d staging; fi'
               			sh 'git branch staging'
            
            		}
		}
		stage('Building the last version of the model'){
			steps {
				sh '''
				#!/usr/bin/env bash
				source ~/opt/anaconda3/etc/profile.d/conda.sh
				conda activate datascience
				python model_build.py ~/fashion-mnist-train-1.csv
				'''
			}
		}
		stage('Building the app on docker'){
			steps {
				
				sh 'docker build -t flask-app-python .'
			}
		}
		stage('Testing the app and model'){
			steps {
				sh 'python3 -m flask run --host=0.0.0.0 &'
				sh 'python3 test.py'
				sh 'pkill python run app.py'
			}
		}
		stage('Deploying and merging staging branch'){
			steps {
				sh 'docker run -p 5000:5000 flask-app-python &'
				echo 'Merging to the git master'
				sh 'git checkout master'
				sh 'git pull'
				sh 'git merge staging -m "incorporating build"'
				echo 'Deleting the staging branch'
				sh 'git branch -d staging'
			}
		}
	}
}
