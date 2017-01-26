from executecommand import execute_cmd, form_cmd
from fasTeardown import fasTeardown


class fasShow(fasTeardown):

    def __init__(self, sshclient, log):
        """
        Constructor 
        param sshclient : sshclient obj 
        param log : logger obj
        """
        self.sshclient = sshclient
        self.log = log
        fasTeardown.__init__(self, self.sshclient, self.log)

    def aggr_show(self, **kwargs):
        """
        Lists aggregates.
        """
        args = [
            'checksum',
            'disk',
            'instance',
            'raid-info',
            'storage-type',
            'chksumstyle',
            'diskcount',
            'mirror',
            'disklist',
            'mirror-disklist',
            'node',
            'free-space-realloc',
            'ha-policy',
            'percent-snapshot-space',
            'space-nearly-full-threshold-percent',
            'space-full-threshold-percent',
            'hybrid-enabled',
            'availsize',
            'chksumenabled',
            'chksumstatus',
            'cluster',
            'cluster-id',
            'dr-home-id',
            'dr-home-name',
            'has-mroot',
            'has-partner-mroot',
            'home-id',
            'home-name',
            'hybrid-cache-size-total',
            'hybrid',
            'inconsistent',
            'is-home',
            'maxraidsize',
            'cache-raid-group-size',
            'owner-id',
            'owner-name',
            'percent-used',
            'plexes',
            'raidgroups',
            'raidstatus',
            'raidtype',
            'resyncsnaptime',
            'root',
            'sis-metadata-space-used',
            'size',
            'state']
        cmd = "aggr show -field aggregate,size,availsize,node "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def lun_show(self, fields="size", **kwargs):
        """
        Lists all the luns.
        """
        args = [
            'instance',
            'fields',
            'vserver',
            'path',
            'volume',
            'qtree',
            'lun',
            'size',
            'ostype',
            'space-reserve',
            'serial',
            'serial-hex',
            'comment',
            'space-reserve-honored',
            'space-allocation',
            'state',
            'uuid',
            'mapped',
            'block-size',
            'device-legacy-id',
            'device-binary-id',
            'device-text-id',
            'read-only',
            'restore-inaccessible',
            'size-used',
            'max-resize-size',
            'creation-timestamp',
            'class',
            'node',
            'qos-policy-group',
            'caching-policy',
            'is-clone',
            'is-clone-autodelete-enabled',
            'inconsistent-import']
        if fields is not None:
            kwargs['fields'] = fields
        cmd = "lun show "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def job_show(self, **kwargs):
        args = [
            'inprogress',
            'instance',
            'jobstate',
            'sched',
            'times',
            'type',
            'fields',
            'id',
            'vserver',
            'name',
            'description',
            'priority',
            'node',
            'affinity',
            'schedule',
            'queuetime',
            'starttime',
            'endtime',
            'dropdeadtime',
            'restarted',
            'state',
            'code',
            'completion',
            'jobtype',
            'category',
            'progress',
            'username',
            'restart-is-delayed-by-module']
        cmd = "job show "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)

    def volume_show(self, **kwargs):
        """
        lists the volumes
        """
        args = ['fields', 'vserver', 'volume', 'type']
        cmd = "volume show "
        cmd_new = form_cmd(args, kwargs, cmd)
        return execute_cmd(self.sshclient, cmd_new, self.log)
