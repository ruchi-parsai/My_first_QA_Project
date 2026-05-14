pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t playwright-framework .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run -v %cd%/allure-results:/app/allure-results playwright-framework'
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}