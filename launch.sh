#!/bin/bash

uv run gunicorn -w 4 -b 127.0.0.1:8081 app:app
