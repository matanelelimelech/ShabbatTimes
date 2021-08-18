pipeline {
    agent { docker { image 'python:3.5.1' } }

    stages {
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
        stage('install requirements') {
            steps{
               sh 'sudo pip install -r requirements.txt'
            }
        }
     
        stage('build') {
            steps {
                sh 'python itamar.py'
            }
        }
    }
}
