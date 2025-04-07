pipeline {
    agent any
    environment {
        AWS_REGION = 'ap-south-1'
        ECR_REGISTRY = '865698115856.dkr.ecr.ap-south-1.amazonaws.com'
        EKS_CLUSTER = 'sentiment-eks-cluster'
    }
    stages {
        stage("Cleanfirst") {
             steps {
                 cleanWs()
             }
         }
        stage("Initialization") {
    steps {
        // use name of the patchset as the build name
        // buildName "${BUILD_NUMBER}-${App_Name}-${GIT_BRANCH}"
        wrap([$class: 'BuildUser']) {
            script {
                def changeLogSets = currentBuild.changeSets
                currentBuild.displayName = "#${currentBuild.number}-#${params.GIT_BRANCH}--Build By: #${BUILD_USER}"
                currentBuild.description = "Build By: ${BUILD_USER}"
                }
            
            }
        }
    }
        stage('Checkout') {
    steps {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/full-sentiment']],
                  userRemoteConfigs: [[url: 'https://github.com/sumittiwari022/SentimentAnalysis.git']]])
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
        stage('Prepare API') {
            steps {
                sh 'mkdir -p api/model'
                sh 'cp model/sentiment_model.pkl api/model/'
                sh 'cp model/vectorizer.pkl api/model/'
            }
        }
        stage('Build API') {
            steps {
                dir('api') {
                    sh 'docker build -t ${ECR_REGISTRY}/custom-images:sentiment-api .'
                    sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
                    sh 'docker push ${ECR_REGISTRY}/custom-images:sentiment-api'
                }
            }
        }
        stage('Build UI') {
            steps {
                dir('ui') {
                    sh 'docker build -t ${ECR_REGISTRY}/custom-images:sentiment-ui .'
                    sh 'aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}'
                    sh 'docker push ${ECR_REGISTRY}/custom-images:sentiment-ui'
                }
            }
        }
        // stage('Deploy to EKS') {
        //     steps {
        //         dir('kubernetes') {
        //             sh 'aws eks update-kubeconfig --region ${AWS_REGION} --name ${EKS_CLUSTER}'
        //             sh 'kubectl apply -f api-deployment.yaml'
        //             sh 'kubectl apply -f api-service.yaml'
        //             sh 'kubectl apply -f ui-deployment.yaml'
        //             sh 'kubectl apply -f ui-service.yaml'
        //             sh 'kubectl apply -f ingress.yaml'
        //         }
        //     }
        // }
        stage("Cleanlast") {
             steps {
                 cleanWs()
             }
         }
    }
}