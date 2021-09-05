pipeline {
    agent { dockerfile true }
    stages {
        stage('Build') {
            steps {
                sh 'python /tmp/zip_job.py'
            }
        }
    }
}