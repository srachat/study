#!/bin/sh

sleep 10

celery -A src.worker worker -l INFO -E