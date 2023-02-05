pipeline {
	agent any
	environment {     
    		DOCKERHUB_CREDENTIALS = credentials('dockerhubcred')     
    	}
   	stages {
		stage('Building the model'){
			steps {
				sh 'conda init bash'
        			sh 'conda activate datascience'
				sh 'python model_build.py'
			}
		}
	}
}
