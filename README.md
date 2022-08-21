# Build and deploy

```bashrc
docker build --platform=linux/amd64 -t django_api .
docker tag django_api:latest public.ecr.aws/t1r6r0z7/django_api:latest
docker push public.ecr.aws/t1r6r0z7/django_api:latest
aws ecs update-service --cluster app --service django-api --force-new-deployment
```
# django
