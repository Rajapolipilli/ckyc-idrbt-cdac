from django.conf import settings
from .models import Policy,PolicyField
from xml.etree import ElementTree, cElementTree
from xml.dom import minidom
from xml.dom.minidom import parseString
from xml.etree.ElementTree import XML, fromstring, tostring

import xml.etree.ElementTree as ET

s_root=settings.SERVICE_NAME

def getXML(val):
	pol=Policy.objects.get(pk=val)
	# print(pol)
	print(pol.policyfield_set.all())

	root = ElementTree.Element(str(s_root))
	child0 = ElementTree.SubElement(root, str(pol))

	for pf in pol.policyfield_set.all():
		# print(pf._meta.get_fields())
		f=[f.name for f in pf._meta.get_fields()]
		#print(f)

		child1 = ElementTree.SubElement(child0, 'Field')

		child1_1 = ElementTree.SubElement(child1, str(f[2]))
		child1_1.text = str(pf.name)

		child1_1 = ElementTree.SubElement(child1, str(f[3]))
		child1_1.text = str(pf.meta)

		if pf.datatype !='None':
			if pf.datatype == 'select' and pf.pattern== 'genderSelect':

				child1_1 = ElementTree.SubElement(child1, 'select')
				child_p = ElementTree.SubElement(child1_1, 'option')
				child_p.text = 'Male'
				child_p = ElementTree.SubElement(child1_1, 'option')
				child_p.text = 'Female'
				child_p = ElementTree.SubElement(child1_1, 'option')
				child_p.text = 'Other'
			else:
				child1_1 = ElementTree.SubElement(child1, str(f[4]))
				child1_1.text = str(pf.datatype)

		if pf.pattern != 'None':
			if pf.pattern == 'dob_constraint':
				child1_1 = ElementTree.SubElement(child1, str(f[5]))
				child_p = ElementTree.SubElement(child1_1, 'min')
				child_p.text = str(1902)
				child_p = ElementTree.SubElement(child1_1, 'max')
				child_p.text = str(2002)
			elif pf.pattern == 'genderSelect':
				pass
			else:	
				child1_1 = ElementTree.SubElement(child1, str(f[5]))
				child1_1.text = str(pf.pattern)	

		child1_1 = ElementTree.SubElement(child1, str(f[7]))
		child1_1.text = str(pf.message)

		
		# child1_1.text = str(pf.proof_doc)
		if pf.proof:
			res = pf.proof.strip('][').split(',')
			print(res,res[0],'\n\n')
			child1_1 = ElementTree.SubElement(child1, str(f[6]))
			for j in res:
				child_p = ElementTree.SubElement(child1_1, 'attachments')
				child_p.text = str(j)

		xm=ElementTree.tostring(root).decode()
		xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
		# with open("New_Database.xml", "w") as f:
		#     f.write(xmlstr)		
		f = open("media/"+str(pol)+".xml", "w")
		f.write(xmlstr)
		f.close()
	return s_root


