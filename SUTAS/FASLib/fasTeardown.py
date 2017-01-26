from executecommand import execute_cmd, form_cmd
import time

class fasTeardown:

    def __init__(self, sshclient, log):
        """
        Constructor 
        param sshclient : sshclient obj 
        param log : logger obj
        """
        self.sshclient = sshclient
        self.log = log

    def volume_offline(self, **kwargs):
        """
        Make volume offline.
        Mandatory field vserver,volume
        vserver :   SVM Name
        volume  :   volume named to be offlined 
        """
        args = [
            'vserver',
            'volume',
            'force',
            'foreground',
            'disable-luns-check']
        cmd = "volume offline "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def lun_delete(self, **kwargs):
        """
        delete lun.
        Mandatory field vserver,path
        vserver : SVM Name
        path    : Lun path 
        """
        args = [
            'vserver',
            'path',
            'volume',
            'qtree',
            'lun',
            'force',
            'force-fenced']
        cmd = "lun delete "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def volume_delete(self, **kwargs):
        """
        delete volume
        Mandatory fields vserver,volume
        vserver :   SVM Name
        volume  :   Volume Name to be deleted
        """
        args = ['vserver', 'volume', 'foreground']
        cmd = "volume delete "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def vserver_delete(self, **kwargs):
        """
        vserver delete
        Mandatory fields vserver
        vserver : SVM Name
        """
        args = ['vserver', 'foreground']
        cmd = "vserver delete "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def aggr_delete(self, **kwargs):
        """
        Mandatory fields
        aggregate:      Aggregate Name
        """
        time.sleep(45)
        args = ['aggregate']
        cmd = "aggr delete "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def network_interface_delete(self, **kwargs):
        """
        Mandatory fields are vserver,Lif
        vserver :   Vserver Name
        Lif     :   Logical Interface Name
        """
        args = ['vserver', 'lif']
        cmd = "network interface delete "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)
