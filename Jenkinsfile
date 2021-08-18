pipeline {
    agent { docker { image 'matanelelimelech/jenkinsdocker' } }

    stages {
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
        
        stage('build') {
            steps {
                sh 'python itamar.py'
            }
        }
    }
}
