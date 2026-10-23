pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/NiranjanYadav-NY/html-form-jenkins.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test_form.py'
            }
        }
    }

    post {
        success {
            echo 'HTML form tests passed!'
        }
        failure {
            echo 'HTML form tests failed!'
        }
    }
}
