pipeline {
    agent any
    parameters {
	    string defaultValue: '2023-01-01', name: 'ITU_DATE', trim: true
    }
    stages {
	stage('Python Enviroment'){
		steps {
			sh """
			python3 -m venv venv
    			chmod +x venv/bin/activate
			"""
		}
	}
	stage('Install Reqirements'){
		steps {
			sh """
			. venv/bin/activate
			pip install -r reqirements.txt
			"""
		}
	}
	stage('Run script'){
		steps {
			sh """
   			echo "filter since ${params.ITU_DATE}"
       			. venv/bin/activate
        		python3 py_itu_change.py ${params.ITU_DATE}
			"""
		}
	}
    }
}
