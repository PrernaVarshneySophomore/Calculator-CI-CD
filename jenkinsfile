
pipeline {
    agent any

    triggers {
        // Check GitHub for changes approximately every 2 minutes.
        pollSCM('H/2 * * * *')
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully.'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    set -eu
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements.txt
                    .venv/bin/python -m py_compile calculator.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    set -eu
                    mkdir -p reports
                    .venv/bin/python -m pytest -v \
                        --junitxml=reports/pytest.xml
                '''
            }

            post {
                always {
                    junit allowEmptyResults: true,
                          testResults: 'reports/pytest.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    set -eu
                    DEPLOY_DIR=/var/lib/jenkins/deployed-calculator

                    mkdir -p "$DEPLOY_DIR"
                    cp calculator.py "$DEPLOY_DIR/calculator.py"
                    cp requirements.txt "$DEPLOY_DIR/requirements.txt"

                    echo "Calculator deployed to $DEPLOY_DIR"
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
