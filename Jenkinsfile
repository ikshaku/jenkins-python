pipeline {
    agent any

    stages {
        stage('Welcome') {
            steps {
                echo 'Hello World!'
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'c246691e-23f3-4c7d-814c-d4b103054489', url: 'https://github.com/ikshaku/jenkins-python']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', credentialsId: 'c246691e-23f3-4c7d-814c-d4b103054489', url: 'https://github.com/ikshaku/jenkins-python'
//                 sh '''python3 -m pip install requests
// python3 test.py'''
            }
        }
        stage('Test') {
            steps {
                echo 'Success!'
            }
        }
    }
}
