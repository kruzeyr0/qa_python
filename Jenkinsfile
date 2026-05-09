pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'homework_31',
                url: 'https://github.com/kruzeyr0/qa_python.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r lesson_29/requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'set PYTHONPATH=lesson_29 && python -m pytest lesson_29/tests --alluredir=allure-results -v'
            }
        }
    }

    post {
		always {
			allure(
				includeProperties: false,
				results: [[path: 'allure-results']]
			)

			emailext(
				subject: "Jenkins Build: ${currentBuild.currentResult}",
				body: "Build finished with status: ${currentBuild.currentResult}",
				to: "katrich.andrey@ukr.net"
			)
		}
	}
}