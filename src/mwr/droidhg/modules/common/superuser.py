import os

class SuperUser(object):
    """
    Mercury Client Library: provides utility methods for aiding with superuser
    binary installation on the Agent.
    """

    def __agentPathSu(self):
        """
        Get the path to which su is uploaded on the Agent.
        """

        return "/data/data/com.mwr.droidhg.agent/su"

    def _localPathSu(self):
        """
        Get the path to the su binary on the local system.
        """

        return os.path.join(os.path.dirname(__file__) , "..", "tools", "setup", "minimal-su", "libs", "armeabi", "su")

    def __agentPathScript(self):
        """
        Get the path to which the install script is uploaded on the Agent.
        """

        return "/data/data/com.mwr.droidhg.agent/install-su.sh"

    def _localPathScript(self):
        """
        Get the path to the install script on the local system.
        """

        return os.path.join(os.path.dirname(__file__) , "..", "tools", "setup", "minimal-su", "install-su.sh")

    def isSuInstalled(self):
        """
        Test whether su is installed on the Agent.
        """

        return self.exists("/system/bin/su")

    def uploadSu(self):
        """
        Upload su to the Agent.
        """

        # Remove existing uploads of su
        self.shellExec("rm /data/data/com.mwr.droidhg.agent/su")

        bytes_copied = self.uploadFile(self._localPathSu(), self.__agentPathSu())

        if bytes_copied == os.path.getsize(self._localPathSu()):
            return True
        else:
            return False

    def uploadSuInstallScript(self):
        """
        Upload su install script to the Agent.
        """

        # Remove existing uploads of su install script
        self.shellExec("rm /data/data/com.mwr.droidhg.agent/install-su.sh")

        bytes_copied = self.uploadFile(self._localPathScript(), self.__agentPathScript())

        if bytes_copied == os.path.getsize(self._localPathScript()):
            self.shellExec("chmod 770 " + self.__agentPathScript())
            return True
        else:
            return False

