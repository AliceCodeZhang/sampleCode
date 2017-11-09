pipeline {
  agent none
  stages {
    stage('Preparation') {
      parallel {
        stage('Preparation') {
          agent {
            node {
              label 'mac'
            }
            
          }
          steps {
            sh 'echo preparation1'
          }
        }
        stage('Preparation_2') {
          agent any
          steps {
            sh 'echo preparation2'
          }
        }
      }
    }
    stage('build') {
      agent any
      steps {
        sh 'pwd'
        echo 'abc'
      }
    }
    stage('Test') {
      parallel {
        stage('node 1') {
          agent any
          steps {
              sh 'pwd'
              sh 'sleep 20s'
              sh 'echo hstream1'
          }
        }
        stage('node 2') {
          agent {
            label 'mac'
          }
          steps {
              sh 'pwd'
              sh 'sleep 20s'
              sh 'echo hello2'
            
          }
        }
      }
    }
  }
}
