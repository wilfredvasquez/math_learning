#!/bin/sh

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
celery -A math_learning beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler