pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sentiment-app'
        DOCKER_HUB_USER = 'sumittiwari022'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sumittiwari022/SentimentAnalysis.git'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python sentiment_model/train_model.py'
            }
        }

        stage('Build Image') {
            steps {
                dir('webapp') {
                    sh 'docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:latest .'
                }
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh 'kubectl apply -f deploy/deployment.yaml'
                sh 'kubectl apply -f deploy/service.yaml'
                sh 'kubectl apply -f deploy/ingress.yaml'
            }
        }
    }
}
