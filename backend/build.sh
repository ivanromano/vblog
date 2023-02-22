#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py flush
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

if [[ $CREATE_SUPERUSER ]];
then
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python manage.py shell
fi
 
python manage.py collectstatic --no-input
python manage.py migrate