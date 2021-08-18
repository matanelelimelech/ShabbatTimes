pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh 'pylint itamar.py'
            }
        }
        stage('build') {
            steps {
                sh 'python itamar.py'
            }
        }
    }
}
