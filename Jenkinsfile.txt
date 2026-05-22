pipeline {

    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t salesdashboard:%BUILD_NUMBER% .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 8501:8501 --name dashboard-%BUILD_NUMBER% salesdashboard:%BUILD_NUMBER%'
            }
        }
    }
}