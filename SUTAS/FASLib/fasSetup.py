from FASLib.executecommand import execute_cmd, form_cmd
from robot.libraries.BuiltIn import BuiltIn


class fasSetup:

	def __init__(self, sshclient, log):
		"""
		Constructor 
		param sshclient : sshclient obj 
		param log : logger obj
		"""
		self.sshclient = sshclient
		self.log = log

	def raise_Exception(self, msg):
		"""
		Raise Exception msg
		param msg: Error msg to be displayed
		"""
		#self.log.info(msg)
		raise Exception(msg)

	def lun_create(self, **kwargs):
		"""
		Create LUN.
		Required arguments are vserver, volume, lun, size,ostype and aggregate.
		vserver: SVM name
		volume: Volume name
		lun: lun name
		size: size of the lun to be created
		aggregate: name of the aggregate
		"""
		args = [
			'vserver',
			'path',
			'volume',
			'qtree',
			'lun',
			'size',
			'file-path',
			'ostype',
			'space-reserve',
			'comment',
			'space-allocation',
			'class',
			'qos-policy-group',
			'caching-policy']
		cmd = "lun create "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def volume_create(self, **kwargs):
		"""
		Create Volume.
		Required arguments are vserver, volume, size and aggregate.
		vserver: SVM name
		volume: Volume name
		size: size of the volume to be created
		aggregate: aggregate name
		"""
		args = [
			'vserver',
			'volume',
			'aggregate',
			'aggr-list',
			'aggr-list-multiplier',
			'size',
			'state',
			'policy',
			'user',
			'group',
			'security-style',
			'unix-permissions',
			'junction-path',
			'comment',
			'max-autosize',
			'min-autosize',
			'autosize-grow-threshold-percent',
			'autosize-shrink-threshold-percent',
			'autosize-mode',
			'space-slo',
			'space-guarantee',
			'type',
			'percent-snapshot-space',
			'snapshot-policy',
			'language',
			'foreground',
			'nvfail',
			'enable-snapdiff',
			'qos-policy-group',
			'caching-policy',
			'vserver-dr-protection',
			'encrypt']
		cmd = "volume create "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def lun_map(self, **kwargs):
		"""
		Map lun to specified igroup.
		Required arguments are vserver, path and igroup.
		vserver:    SVM name
		path:       lun path
		igroup:     name of the igroup to be mapped
		"""
		args = ['vserver', 'path', 'igroup']
		cmd = "lun map "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def lun_resize(self, **kwargs):
		"""
		resize lun.
		Required arguments are vserver, path and size.
		vserver:    SVM name
		path:       lun path
		size:       total lun size
		"""
		args = ['vserver', 'path', 'size']
		cmd = "lun resize "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def lun_modify(self, **kwargs):
		"""
		Modify lun properties.
		Required arguments are vserver and path.
		vserver: SVM name
		path: lun path
		you can modify following attributes
		['space-reserve', 'space-allocation', 'caching-policy', 'state', 'qos-policy-group']
		space-reserve: enabled/disabled
		space-allocation: enabled/disabled
		caching-policy: all/all_read/default/random_read etc.
		state: online/offline
		"""
		args = [
			'vserver',
			'path',
			'space-reserve',
			'space-allocation',
			'caching-policy',
			'state',
			'qos-policy-group']
		cmd = "lun modify "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def vserver_create(self, **kwargs):
		"""
		vserver: SVM name to be created
		rootvolume: volume name to be created on SVM
		aggregate: Aggregate name
		rootvolume-security-style:mixed or ntfs or unix
		"""
		args = [
			'vserver',
			'subtype',
			'rootvolume',
			'aggregate',
			'rootvolume-security-style',
			'language',
			'snapshot-policy',
			'comment',
			'quota-policy',
			'is-repository',
			'caching-policy',
			'ipspace',
			'foreground']
		cmd = "vserver create "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def aggregate_create(self, **kwargs):
		"""
		aggregate: Aggregate Name
		diskcount: No of Disks
		"""
		args = [
			'aggregate',
			'chksumstyle',
			'diskcount',
			'diskrpm',
			'disksize',
			'disktype',
			'diskclass',
			'mirror',
			'pool',
			'disklist',
			'mirror-disklist',
			'ignore-pool-checks',
			'allow-mixed-rpm',
			'allow-same-carrier',
			'node',
			'maxraidsize',
			'raidtype',
			'simulate',
			'encrypt',
			'snaplock-type']
		cmd = "aggr create "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)

	def network_interface_create(self, **kwargs):
		"""
		vserver:        Vserver Name
		lif:            Logical Interface Name
		role:           Role
		data-protocol:  Data Protocol
		home-node:      Home Node
		home-port:      Home Port
		address:        Network Address
		netmask:        Netmask
		"""
		args = [
			'vserver',
			'lif',
			'role',
			'data-protocol',
			'home-node',
			'home-port',
			'address',
			'netmask',
			'netmask-length',
			'auto',
			'subnet-name',
			'status-admin',
			'failover-policy',
			'firewall-policy',
			'auto-revert',
			'dns-zone',
			'listen-for-dns-query',
			'failover-group',
			'comment',
			'force-subnet-association',
			'is-dns-update-enabled']
		cmd = "network interface create "
		cmd_new = form_cmd(args, kwargs, cmd)
		return execute_cmd(self.sshclient, cmd_new, self.log)
