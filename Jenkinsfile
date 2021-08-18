pipeline {
    agent any
    stages {
        stage('test') {
            steps {
                sh '/usr/bin/pylint itamar.py'
            }
        }
        stage('build') {
            steps {
                sh 'python itamar.py'
            }
        }
    }
}
