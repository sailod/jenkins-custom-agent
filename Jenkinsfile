pipeline {
  agent {
    kubernetes {
      yamlFile 'KubernetesPod.yaml'
    }
  }
  stages {
    stage('Build') {
      steps {
        container('custom-python') {
          sh 'python /tmp/zip_job.py'
        }
      }
    }
  }
}