#!/bin/bash

uv run gunicorn -w 4 -b 0.0.0.0:8081 app:app
