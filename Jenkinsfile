pipeline {
	agent any
	environment {     
    		DOCKERHUB_CREDENTIALS = credentials('dockerhubcred')     
    	}
   	stages {
		stage('Building the model'){
			steps {
				sh '''
				#!/usr/bin/env bash
				source ~/opt/anaconda3/etc/profile.d/conda.sh
				conda activate datascience
				python model_build.py ~/fashion-mnist-train-1.csv
				'''
			}
		}
	}
}
