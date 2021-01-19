pipeline {
  agent any

  options {
    timeout(time: 20, unit: 'MINUTES') // set the total execution time of the job
  }
  
  stages {
    stage('checkout') {
      steps {
        git clone 'https://github.com/karnrr/flask-app.git'
        //checkout scm
      }
    }

    stage('Setup') {
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
    
    stage('Linting') {
      steps {
        script {
          sh """
          pylint app/*.py
          """
        }
      }
    }
  }
}
