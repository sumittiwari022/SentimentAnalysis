pipeline {
    agent any
    environment {
        AWS_REGION = 'us-west-2'
        ECR_REGISTRY = '<your-ecr-repo>'
        EKS_CLUSTER = 'sentiment-eks-cluster'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/sentiment-analysis-pipeline.git'
            }
        }
        stage('Train Model') {
            steps {
                dir('model') {
                    sh 'docker build -t sentiment-model .'
                    sh 'docker run -v $(pwd):/model sentiment-model'
                }
            }
        }
        stage('Build API') {
            steps {
                dir('api') {
                    sh 'docker build -t ${ECR_REGISTRY}/sentiment-api:latest .'
                    sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
                    sh 'docker push ${ECR_REGISTRY}/sentiment-api:latest'
                }
            }
        }
        stage('Build UI') {
            steps {
                dir('ui') {
                    sh 'docker build -t ${ECR_REGISTRY}/sentiment-ui:latest .'
                    sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
                    sh 'docker push ${ECR_REGISTRY}/sentiment-ui:latest'
                }
            }
        }
        stage('Deploy to EKS') {
            steps {
                dir('kubernetes') {
                    sh 'aws eks update-kubeconfig --region ${AWS_REGION} --name ${EKS_CLUSTER}'
                    sh 'kubectl apply -f api-deployment.yaml'
                    sh 'kubectl apply -f api-service.yaml'
                    sh 'kubectl apply -f ui-deployment.yaml'
                    sh 'kubectl apply -f ui-service.yaml'
                    sh 'kubectl apply -f ingress.yaml'
                }
            }
        }
    }
}