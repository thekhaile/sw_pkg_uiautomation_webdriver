import pytest
from projectBase import ProjectBase
from southwire_pkg_uiautomation_webdriver.components.authentication import Authentication
from southwire_pkg_uiautomation_webdriver.components.navigation import Navigation
from southwire_pkg_uiautomation_webdriver.components.projectList import ProjectList
from southwire_pkg_uiautomation_webdriver.components.jobList import JobList
from southwire_pkg_uiautomation_webdriver.components.jobSummary.jobSummary import JobSummary

class TestSubmittedJob(ProjectBase):

    def __init__(self, *args, **kwargs):
        super(TestSubmittedJob, self).__init__(*args, **kwargs)
        self.navigation = Navigation(self)
        self.authentication = Authentication(self)
        self.projectList = ProjectList(self)
        self.jobList = JobList(self)
        self.jobSummary = JobSummary(self)

    @pytest.mark.ac
    def testJobSettingsCannotBeEditedAfterRFQSubmission(self):
        # Verify the job settings cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391972
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.tapOverflow()

        try:
            editSettings = self.jobList.getEditSettings().ui_object
        except:
            editSettings = None
        self.assertion.assertNotExists(editSettings, "Job settings button exists")

    @pytest.mark.ac
    def testJobReelsCannotBeEditedAfterRFQSubmission(self):
        # Verify the job reels cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391973
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        try:
            configureJob = self.jobSummary.getConfigureJob().ui_object
        except:
            configureJob = None

        self.assertion.assertNotExists(configureJob, "Configure job button exists")

    @pytest.mark.ac
    def testJobFeederScheduleCannotBeEditedAfterRFQSubmission(self):
        # Verify the job feeder schedule cannot be edited once an RFQ is submitted
        email = 'nick.moore+auto50@mutualmobile.com'
        password = 'newpassword'

        self.caseId = 1391974
        self.navigation.navigateToLoginPage()
        self.authentication.login(email, password)
        self.projectList.selectAProject()
        self.jobList.selectAJob()

        try:
            configureJob = self.jobSummary.getConfigureJob().ui_object
        except:
            configureJob = None

        self.assertion.assertNotExists(configureJob, "Configure job button exists")
