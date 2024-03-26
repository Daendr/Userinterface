pipeline {
    parameters {
        choice(name: 'REPOSITORY', choices: ['https://github.com/Daendr/Userinterface.git'], description: 'Выберите репозиторий для сборки')
        booleanParam(name: 'VERBOSE', defaultValue: false, description: 'Enable verbose mode')
    }
    agent any

    triggers {
        cron('H 8 * * *') // Запланированная сборка каждый день в 8 часов
        pollSCM('H/5 * * * *') // Проверять изменения каждые 5 минут
    }

    environment {
        // Устанавливаем кодировку для вывода Python в UTF-8
        PYTHONIOENCODING = 'UTF-8'
        // Добавляем путь к Python в переменную PATH
        PATH = "C:\\Users\\AU\\AppData\\Local\\Programs\\Python\\Python39\\:$PATH"
    }

    options {
        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '5'))
    }

    stages {
        stage('Set UTF-8 Encoding') {
            steps {
                script {
                    // Устанавливаем кодировку консоли на UTF-8
                    bat 'chcp 65001'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Установка зависимостей из файла requirements.txt
                    bat 'chcp 65001 && C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install -r requirements.txt'
                }
            }
        }
        stage('Clean and Create Workspace Folder') {
            steps {
                script {
                    // Удаление папки Log, если она существует
                    bat 'rmdir /S /Q "%WORKSPACE%\\Log" || exit 0'
                    // Удаление старой директории PytestArtifacts перед каждым запуском
                    bat 'rmdir /S /Q "%WORKSPACE%\\PytestArtifacts" || exit 0'
                    // Создание папки в Jenkins workspace
                    bat 'mkdir "%WORKSPACE%\\PytestArtifacts"'
                }
            }
        }
        stage('Run Tests') {
        when {
            expression { params.VERBOSE }
        }
        steps {
            // Запуск тестов в режиме verbose
            bat 'chcp 65001 && C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest --verbose tests'
        }
        }

        stage('Run Tests Quietly') {
            when {
                expression { !params.VERBOSE }
            }
            steps {
                // Запуск тестов в тихом режиме
                bat 'chcp 65001 && C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest --quiet tests'
            }
        }
        stage('Run HTML Report') {
            steps {
                script {
                    // Установка плагина pytest-html
                    bat 'chcp 65001 && C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install pytest-html'
                    // Запуск тестов с генерацией HTML-отчета
                    bat 'chcp 65001 && C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pytest --html=%WORKSPACE%\\PytestArtifacts\\report.html'
                }
            }
        }
        stage('Publish and Copy HTML Report') {
            steps {
                script {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'PytestArtifacts',
                        reportFiles: 'report.html',
                        reportName: 'HTML Report'
                    ])
                }
            }
        }
    }
    post {
    always {
        echo 'Этот шаг выполняется всегда'
    }
    success {
        echo 'Этот шаг выполняется после успешной сборки'
    }
    unstable {
        echo 'Этот шаг выполняется после нестабильной сборки'
    }
    failure {
        echo 'Этот шаг выполняется после неудачной сборки'
    }
    cleanup {
        echo 'Этот шаг выполняется для очистки после завершения сборки'
    }
    }
}