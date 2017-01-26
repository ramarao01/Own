from jira.client import JIRA

class Jiralib():
    
    def __init__(self, server, username, pwd):

        self.conn = self.connect_jira(server, username, pwd)
        #self.project_id = project_id
        
    def find_project_by_name(self, project_name):
        project = None
        for i in self.conn.projects():
            if i.name == project_name:       
                project = i
        if project:
            return project.id
        else:
            print "no project with name %s" %project_name
 
    def connect_jira(self, server, username, pwd):
        """
        Will write once i get time
        """  
        options = {'server': server}
        try:      
            jira = JIRA(options, basic_auth=(username, pwd))
        except Exception as  e:        
            print e.msg
        return jira
    
    def raise_issue(self, project_name, summary, description, comment = None, watcher = None, issuetype={'name': 'Bug'}, attachments = None):
        """
        TODO
        """

        new_issue = self.conn.create_issue(project= self.find_project_by_name(project_name), summary=summary,
                                      description=description, issuetype=issuetype)
        if attachments:
            self.conn.add_attachment(new_issue, attachments)
        if comment:
            self.conn.add_camment(new_issue, comment)
            
        #As of now no users available to add as a watcher
        #if watcher:
            #self.conn.add_watcher(new_issue, watcher)
        #else:
            #self.conn.add_watcher(new_issue, 'admin')
            
            
            
        print 'New issue %s created successfully.' %new_issue
    
    
    

