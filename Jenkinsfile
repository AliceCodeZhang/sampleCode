void setBuildStatus(String jsUrl, String message, String state) {
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [$class: "ManuallyEnteredRepositorySource", url: jsUrl],
        contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/sampleCode"],
        errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
        statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
    ]);
}


pipeline {
  agent none
  options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr:'20'))
        timeout(time: 30, unit: 'MINUTES')
  }
  stages {
    stage('build') {
      agent any
      steps {
        sh 'pwd'
        echo 'build'
      }
    }
    stage('Test') {
          agent {
            label 'slave1'
          }
          steps {
              sh 'pwd'
              sh 'echo run test at slave1'
              sh 'python ./src/test2.py'
            
          }
        }
  }
}
