#/bin/sh
PROJECT_ID='mystical-accord-420'
docker build -t predict-service .
docker tag predict-service gcr.io/$PROJECT_ID/predict-service
gcloud docker -- push gcr.io/$PROJECT_ID/predict-service

