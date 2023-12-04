pipeline {
    agent any
    stages {
        stage('Fortify Remote Arguements') {
          tools {
            jdk 'JDK11'
          }
            steps {
                fortifyRemoteArguements transOptions: '-Xmx4G',
                scanOptions: '"-analyzers" "dataflow"'
            }
        }
        stage('Fortify Remote Analysis') {
            steps {
                withEnv(['PATH+FORTIFY=/var/Fortify_SCA_and_Apps_22.1.1/bin']) {
                    sh 'printenv'
                    fortifyRemoteAnalysis remoteAnalysisProjectType: fortifyPython(skipBuild: 'true'),
                    remoteOptionalConfig: [notifyEmail: 'aphelele.kubeka@mtn.com'],
                    uploadSSC: [appname: 'weather-app', appVersion: 'v1.0']
                }
            }
        }
    }
}
