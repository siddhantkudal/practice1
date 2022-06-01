pipeline {

agent any

stages {

stage('Build') {

steps {

bat 'javac HelloWorld.java'
  bat 'java -version'

}

}

stage('Run') {

steps {

bat 'java HelloWorld'
}
}
}
}
