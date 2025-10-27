pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\tanuj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
        PIP = "C:\\Users\\tanuj\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe"
        APP_TOKEN = credentials('APP_TOKEN')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PIP%" install -r requirements.txt'
            }
        }

        stage('Extract Data') {
            steps {
                bat """
                set TOKEN=${env.APP_TOKEN}
                "${env.PYTHON}" extract_data.py
                """
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check console output for details."
        }
    }
}
