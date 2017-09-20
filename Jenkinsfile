pipeline{
   agent none
   stages{
        stage('Preparation') { 
            // for display purposes
      // Get some code from a GitHub repository
            agent{
               node {
                 label "linux"
                 customWorkspace '/home/yanbin/workspace/test/jenkinsnode'
                }
            }
            steps{
               git 'https://github.com/AliceCodeZhang/sampleCode.git'
           }
        }
        stage('build') {
           agent any
           steps{
              sh 'pwd'
              echo "abc"
           }
        }
        stage('Test') {
            steps{
             parallel (
                "stream 1" : { 
                     node("linux") { 
                           label "linux" 
                           sh "pwd"
                           sh "sleep 20s" 
                           sh "echo hstream1"
                       } 
                   },
                "stream 2" : { 
                     node("mac") { 
                           label "mac"
                           sh "pwd"
                           sh "sleep 20s" 
                           sh "echo hello2"
                       } 
                   }
             )
            }
        }
   }

}