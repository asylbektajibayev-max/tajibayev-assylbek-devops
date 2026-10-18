pipeline {
    agent any
    options { timestamps(); disableConcurrentBuilds(); skipDefaultCheckout(true) }
    environment {
        STUDENT_NAME = 'Assylbek'
        STUDENT_SURNAME = 'Tajibayev'
        STUDENT_GROUP = 'IT2-2310'
        STUDENT_ID = '38288'
        IMAGE = 'tajibayev-assylbek-devops'
        CONTAINER = 'tajibayev-assylbek-jenkins-container'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse HEAD'
                echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
                echo "Group: ${env.STUDENT_GROUP}; Student ID: ${env.STUDENT_ID}"
            }
        }
        stage('Build') {
            steps { sh 'python3 -m compileall -q app tests' }
        }
        stage('Test') {
            steps { sh 'python3 -m unittest discover -s tests -v' }
        }
        stage('Docker Build') {
            steps { sh 'docker build -t "$IMAGE:$BUILD_NUMBER" -t "$IMAGE:latest" .' }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    set -eu
                    docker rm -f "$CONTAINER" 2>/dev/null || true
                    docker run -d --name "$CONTAINER" \
                      -p 127.0.0.1:8087:8000 \
                      -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID \
                      "$IMAGE:$BUILD_NUMBER"
                    for attempt in $(seq 1 30); do
                      if docker exec "$CONTAINER" python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"; then break; fi
                      sleep 1
                    done
                    docker exec "$CONTAINER" python -c "import json,os,urllib.request; actual=json.load(urllib.request.urlopen('http://127.0.0.1:8000/api/student')); expected={k:os.environ['STUDENT_'+k.upper()] for k in ('name','surname','group','id')}; assert actual==expected, (actual,expected); print(actual)"
                    docker logs "$CONTAINER"
                    docker inspect --format='Image={{.Image}} Status={{.State.Status}}' "$CONTAINER"
                '''
            }
        }
    }
    post {
        failure { sh 'docker logs "$CONTAINER" 2>/dev/null || true' }
    }
}
