FROM python:3.12-slim
WORKDIR /app
COPY app/ ./app/
RUN python -m compileall -q app && useradd --uid 10001 --create-home student
USER student
EXPOSE 8000
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
HEALTHCHECK --interval=5s --timeout=3s --start-period=5s --retries=5 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"
CMD ["python", "app/main.py"]
