
import xml.etree.ElementTree as ET
from collections import Counter

def parse_xpdl(xpdl_file):
    tree = ET.parse(xpdl_file)
    root = tree.getroot()

    elements_counter = Counter() #class object of collections

    # namespace
    ns = {'xpdl': 'http://www.wfmc.org/2009/XPDL2.2'}

    # checking for swimlanes
    elements_counter['Pools'] = len(root.findall('.//xpdl:Pool', ns))
    elements_counter['Lanes'] = len(root.findall('.//xpdl:Lanes', ns))

    # checking for events
    elements_counter['Total_Events'] = len(root.findall('.//xpdl:Event', ns))
    elements_counter['Start_Events'] = len(root.findall('.//xpdl:StartEvent', ns))
    elements_counter['Intermediate_Events'] = len(root.findall('.//xpdl:IntermediateEvent', ns))
    elements_counter['End_Events'] = len(root.findall('.//xpdl:EndEvent', ns))

    # checking Activites & Tasks
    elements_counter['Tasks'] = len(root.findall('.//xpdl:Activity', ns))
    elements_counter['User_Tasks'] = len(root.findall('.//xpdl:TaskUser', ns))
    elements_counter['Service_Tasks'] = len(root.findall('.//xpdl:TaskService', ns))
    elements_counter['Script_Tasks'] = len(root.findall('.//xpdl:TaskScript', ns))
    elements_counter['Manual_Tasks'] = len(root.findall('.//xpdl:TaskManual', ns))
    elements_counter['Sub_Processes'] = len(root.findall('.//xpdl:SubProcess', ns))


    # checkign for gateways
    gateways = root.findall('.//xpdl:Route', ns)
    elements_counter['Total_Gateways'] = len(gateways)
    elements_counter['Exclusive_Gateways_XOR'] = len([gw for gw in gateways if gw.get('GatewayType') == 'Exclusive'])
    elements_counter['Parallel_Gateways_AND'] = len([gw for gw in gateways if gw.get('GatewayType') == 'Parallel'])
    elements_counter['Inclusive_Gateways_OR'] = len([gw for gw in gateways if gw.get('GatewayType') == 'Inclusive'])

    # checking for artifacts
    artifacts = root.findall('.//xpdl:Artifact', ns)
    elements_counter['Total_Artifacts'] = len(artifacts)
    elements_counter['Data_Objects'] = len([art for art in artifacts if art.get('ArtifactType') == 'DataObject'])
    elements_counter['Groups'] = len([art for art in artifacts if art.get('ArtifactType') == 'Group'])
    elements_counter['Annotations'] = len([art for art in artifacts if art.get('ArtifactType') == 'Annotation'])

    
    #checking for connectors
    sequence_flows = root.findall('.//xpdl:Transition', ns)
    message_flows = root.findall('.//xpdl:MessageFlow', ns)
    associations = root.findall('.//xpdl:Association', ns)
    elements_counter['Sequence_Flows'] = len(sequence_flows)
    elements_counter['Message_Flows'] = len(message_flows)
    elements_counter['Associations'] = len(associations)
    elements_counter['Total_Connecting_Objects'] = len(sequence_flows) + len(message_flows) + len(associations)

    return elements_counter

def generate_report(counter):
    report = "BPMN_Model_Elements:\n"
    for key, value in counter.items():
        report += f"{key.replace('_', ' ')}: {value}\n" #replace underscore with space
    return report

def main():
    xpdl_file = "demo.xpdl"  
    counter = parse_xpdl(xpdl_file)
    report = generate_report(counter)
    print(report)

if __name__ == "__main__":
    main()
