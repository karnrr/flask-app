pipeline{
  options {
    timeout(time: 20, unit: 'MINUTES') // set the total execution time of the job
  }
  
  stages{
    stage('Setup'){
      steps{
        script{
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
    
    stage('Linting'){
      steps{
        script{
          sh """
          pylint app/*.py
          """
        }
      }
    }
  }
}
