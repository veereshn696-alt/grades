pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                   if (isUnix()) {
                        sh 'docker build -t studentgrade:latest .'
                   } else {
                        bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t studentgrade:latest .'
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
                        bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run --rm studentgrade:latest pytest'
                    }
                }
            }
        }
    }
}
