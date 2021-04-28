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
      parallel {
        stage('node 1') {
          agent 'master'
          steps {
              sh 'pwd'
              sh 'sleep 20s'
              sh 'python ./test/test.py'
          }
        }
        stage('node 2') {
          agent {
            label 'slave1'
          }
          steps {
              sh 'pwd'
              sh 'sleep 20s'
              sh 'echo slave1'
              sh 'python ./test/test.py'
            
          }
        }
      }
    }
  }
}
