### Deployment
```bash
uv run gunicorn receipt.asgi:application -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
# or
uv run gunicorn receipt.asgi:application -w 4 -k uvicorn.workers.UvicornWorker --bind unix:/run/gunicorn.sock
```
