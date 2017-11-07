pipeline {
  agent none
  stages {
    stage('Preparation') {
      parallel {
        stage('Preparation') {
          agent any
          steps {
            git 'https://github.com/AliceCodeZhang/sampleCode.git'
          }
        }
        stage('second') {
          agent any
          steps {
            sh 'sh "echo preparation2"'
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
        stage('stream 1') {
          steps {
            node(label: 'linux') {
              label 'linux'
              sh 'pwd'
              sh 'sleep 20s'
              sh 'echo hstream1'
            }
            
          }
        }
        stage('stream 2') {
          steps {
            node(label: 'mac') {
              label 'mac'
              sh 'pwd'
              sh 'sleep 20s'
              sh 'echo hello2'
            }
            
          }
        }
      }
    }
  }
}