pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                   if (isUnix()) {
                        sh 'docker build -t studentgrade:latest .'
                   } else {
                        bat 'docker build -t studentgrade:latest .'
                   }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm studentgrade:latest pytest'
                    } else {
                        bat 'docker run --rm studentgrade:latest pytest'
                    }
                }
            }
        }
    }
}
