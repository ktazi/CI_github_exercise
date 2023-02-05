pipeline {
	agent any
	environment {     
    		DOCKERHUB_CREDENTIALS = credentials('dockerhubcred')     
    	}
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
	}
}
