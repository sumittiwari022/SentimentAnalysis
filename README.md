# Sentiment Analysis Pipeline

## Prerequisites
- AWS CLI configured with credentials
- Docker installed
- Jenkins installed and configured with AWS and Docker plugins
- EKS cluster created (named 'sentiment-eks-cluster')
- ECR repository created

## Steps
1. Replace `<your-ecr-repo>` in Dockerfiles and Kubernetes manifests with your ECR repository URL.
2. Place training data in `/Users/robo/Downloads/jyupiter-nb/Sentiment/` or update paths in `train.py`.
3. Push code to a GitHub repository.
4. Configure Jenkins with the repository URL and trigger the pipeline.
5. Access the UI via the LoadBalancer URL provided by `kubectl get svc sentiment-ui-service`.
