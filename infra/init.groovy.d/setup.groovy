import jenkins.model.Jenkins
import hudson.security.HudsonPrivateSecurityRealm
import hudson.security.FullControlOnceLoggedInAuthorizationStrategy
import org.jenkinsci.plugins.workflow.job.WorkflowJob
import org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition
import hudson.plugins.git.GitSCM
import hudson.plugins.git.BranchSpec

def instance = Jenkins.get()
def realm = new HudsonPrivateSecurityRealm(false)
realm.createAccount('assylbek', System.getenv('JENKINS_ADMIN_PASSWORD'))
instance.setSecurityRealm(realm)
def authorization = new FullControlOnceLoggedInAuthorizationStrategy()
authorization.setAllowAnonymousRead(false)
instance.setAuthorizationStrategy(authorization)
instance.setNumExecutors(1)
instance.setSystemMessage('DevOps laboratory - Assylbek Tajibayev - IT2-2310 - 38288')
def job = instance.getItem('Tajibayev_Assylbek_DevOps')
if (job == null) job = instance.createProject(WorkflowJob, 'Tajibayev_Assylbek_DevOps')
def scm = new GitSCM('https://github.com/asylbektajibayev-max/tajibayev-assylbek-devops.git')
scm.getBranches().clear()
scm.getBranches().add(new BranchSpec('*/main'))
def definition = new CpsScmFlowDefinition(scm, 'Jenkinsfile')
definition.setLightweight(true)
job.setDefinition(definition)
job.save()
instance.save()
