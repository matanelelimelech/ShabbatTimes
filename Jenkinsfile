pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('test') {
            steps {
                sh 'pylint itamar.py'
            }
        }stage('build') {
            steps {
                sh 'python itamar.py'
            }
        }
    }
}
