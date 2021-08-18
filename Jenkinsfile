pipeline {
    agent { docker { image 'matanelelimelech/jenkinsdocker' } }

    stages {
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
        
        stage('deploy') {
            steps {
                sh 'python deploy.py'
            }
        }
    }
}
