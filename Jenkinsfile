pipeline {
  agent any

  options {
    timeout(time: 20, unit: 'MINUTES') // set the total execution time of the job
  }
  
  stages {
    stage('checkout') {
      steps {
        //git clone 'https://github.com/karnrr/flask-app.git'
        checkout([$class: 'GitSCM',
          branches: [[name: '*/master']],
          extensions: scm.extensions,
          userRemoteConfigs:[[
            url: 'https://github.com/karnrr/flask-app.git'
          ]]
        ])
      }
    }

    stage('Setup') {
      steps {
        // script {
        //   sh """
        //   pip install -r requirements.txt
        //   """
        // }

        withPythonEnv('/usr/local/bin/python3.6') {
          sh 'pip install -r requirements.txt'
        }
      }
    }
    
    stage('Linting') {
      steps {
        // script {
        //   sh """
        //   pylint app/*.py
        //   """
        // }

        //  sh 'python3 -m pylint -f text * | cat > report.txt '
        withPythonEnv('/usr/local/bin/python3.6') {
          sh 'python3 -m pylint * > report.txt || exit 0'
        }
      }
    }

    stage('Cythonize') {
      steps {
        withPythonEnv('/usr/local/bin/python3.6') {
          sh 'pip install cython'
        }

        withPythonEnv('/usr/local/bin/python3.6') {
          sh 'python cython_setup.py build_ext'
        }
      }   
    }
  }
}
