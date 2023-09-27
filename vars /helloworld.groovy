pipeline {
  agent { ${name} }
  stages {
   stage('helloworld') {
     steps {
       echo ("helloworld ${variant}")
      }
    }
  }
}
