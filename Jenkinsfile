pipeline {
    agent any
    parameters {
    	string(name: 'ITU_DATE', defaultValue: '2023-01-01')
    }
    stages {
        stage('Initialize') {
            steps {
		    dir('project') {
			    checkout scm
		    }
            }
        }
	stage('Python Enviroment'){
		steps {
			sh '''
			cd project
			python3 -m venv venv
    			chmod +x venv/bin/activate
			'''
		}
	}
	stage('Install Reqirements'){
		steps {
			sh '''
    			cd project
			. venv/bin/activate
			pip install -r reqirements.txt
			'''
		}
	}
	stage('Run script'){
		steps {
			sh '''
    			cd project
       			. venv/bin/activate
        		python3 py_itu_change.py ${params.ITU_DATE}
			'''
		}
	}
    }
}
