# Python nginx openshift + jenkins

oc new-project dev   --display-name="Dev"
oc new-project stage --display-name="Stage"

oc policy add-role-to-user edit system:serviceaccount:cicd:jenkins -n dev
oc policy add-role-to-user edit system:serviceaccount:cicd:jenkins -n stage
oc policy add-role-to-user edit system:serviceaccount:cicd:default -n dev
oc policy add-role-to-user edit system:serviceaccount:cicd:default -n stage

## 1 Open Jenkins
jenkins-cicd.apps.openshift.btech.io

## 2 Manage > Configure System
## 3 Kubernetes Pod Template > Add Pod Template

Name: python
Labels: python

// click on add container
Name: jnlp
Docker Image: idealo/jenkins-slave-python-centos7:latest
Always pull image: True
Working directory: /tmp
Command to Run: 
Arguments to pass to the command: ${computer.jnlpmac} ${computer.name}
Allocate pseudo-TTY: False
Service Account: Jenkins

## 4 Apply & Save

## 5 Create buildconfig
export KUBECONFIG=/root/openshift-config/auth/kubeconfig
oc project cicd 
oc create -f https://raw.githubusercontent.com/zufardhiyaulhaq/openshift-python-nginx-pipeline/master/openshift/pipelines/jenkins-pipeline.yaml 

## 6 Run Buildconfig
oc start-build python-nginx-pipeline

## 7 View Pipeline in jenkins
jenkins-cicd.apps.openshift.btech.io
