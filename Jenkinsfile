pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\tanuj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Extract Data') {
            steps {
                bat "${env.PYTHON} -m extract_data.py"
            }
        }
    }

    post {
        success {
            echo "✅ Data extraction completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed during data extraction."
        }
    }
}
