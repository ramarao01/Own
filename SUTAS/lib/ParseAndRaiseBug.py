try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from Jiralib import Jiralib
import os

class ParseAndRaiseBug:
    def parse(self):
        server = 'http://10.130.205.11:8080'
        username = 'admin'
        pwd = 'admin'
        project_name = 'Storage Services'
        file= os.getcwd() + '\output.xml'
        tree = ET.ElementTree(file = file)

        root = tree.getroot()

        def chk_stats():
            """
            TBW
            """
            stats = root.find('statistics')
            
            if stats:
                #import pdb;pdb.set_trace()
                
                childs = stats.find('suite').getchildren()
                for child in  childs:
                    if child.tag == 'stat':
                        items = child.items()
                        for item in items:
                            if item[0] == 'fail' and  item[1] != '0':
                                return True
            return False
                            
        if chk_stats():
            
            suit = root.find('suite')
            suit_name = suit.attrib['name']
            childs = suit.findall('test')
            obj = Jiralib(server, username, pwd)

            for child in childs:
                st = child.find('status')
                if st.get('status') == 'FAIL':
                    tc_name = child.attrib['name']
                    kws = child.findall('kw')           
                    for kw in kws:
                        if kw.find('status').attrib['status'] == 'FAIL':
                            if not kw.find('kw'):
                                kw_name = kw.attrib['name']
                                for i in kw.getchildren():
                                    if i.tag == 'msg' and i.attrib['level'] == 'FAIL':
                                        msg = i.text
                                msg = msg.replace('\n', '')
                                summ =  tc_name + " failed with error " + msg
                                desc = suit_name + "->" + tc_name + "->" + kw_name + "->" + msg +  " Please check the attached log for more information"

                            else:
                                kw = kw.find('kw')
                                for i in kw.getchildren():
                                    if i.tag == 'msg' and i.attrib['level'] == 'FAIL':
                                        msg = i.text
                                msg = msg.replace('\n', '')
                                kw_name = kw.attrib['name']
                                summ =  tc_name + " failed with error " + msg
                                desc = suit_name +  "->" +  tc_name + "->" + kw_name + "->" + msg +  " Please check the attached log for more information"
                            
                            att = os.getcwd() + "\%s.log" %tc_name
                            obj.raise_issue(project_name, summ, desc, attachments=att)                    

