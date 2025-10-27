pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\tanuj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe"
        APP_TOKEN = credentials("APP_TOKEN")   // use Jenkins credentials (string type)
                }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Corrected pip install command
                bat 'pip install -m requirements.txt'
            }
        }

        stage('Extract Data') {
            steps {
                // Set token temporarily and run the script in one command
                bat """
                set TOKEN=${env.APP_TOKEN}
                ${env.PYTHON} extract_data.py
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
