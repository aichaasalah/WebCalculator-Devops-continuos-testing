pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    // Build Docker image and run tests inside the container
                    sh 'docker build -t calculator-app .'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to registry
                    sh 'docker tag calculator-app your-repo/calculator-app:latest'
                    sh 'docker push your-repo/calculator-app:latest'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! All tests passed!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs for errors.'
        }
    }
}
