import pathlib

import pandas as pd
import xml.etree.ElementTree as ET
import os

dir_path = "C:/Users/chant/OneDrive/FFHS/2022 - 2023/9 Semester/IR/Semesterarbeit/NCT0001xxxx"

cols = ["clinical_study",
        "required_header",
        "download_date",
        "link_text",
        "url",
        "id_info",
        "org_study_id",
        "nct_id",
        "brief_title",
        "official_title",
        "sponsors",
        "lead_sponsor",
        "agency",
        "agency_class",
        "source",
        "oversight_info",
        "is_fda_regulated_drug",
        "is_fda_regulated_device",
        "brief_summary",
        "textblock",
        "overall_status",
        "start_date",
        "completion_date",
        "primary_completion_date",
        "phase",
        "study_type",
        "has_expanded_access",
        "study_design_info",
        "allocation",
        "intervention_model",
        "primary_purpose",
        "masking",
        "primary_outcome",
        "measure",
        "time_frame",
        "description",
        "number_of_arms",
        "enrollment",
        "condition",
        "arm_group",
        "arm_group_label",
        "arm_group_type",
        "intervention",
        "intervention_type",
        "intervention_name",
        "description",
        "arm_group_label",
        "eligibility",
        "criteria",
        "textblock ",
        "gender",
        "minimum_age",
        "maximum_age",
        ]
# folder path
count = 0
# Iterate directory
dir = "C:/Users/chant/IdeaProjects/medical_studies/xml_files"

for i in os.listdir(dir_path):
        to_xml = []
        tags = []
        xml_files = dir_path+"/{}".format(i)
        print(xml_files)
        parse = ET.parse(xml_files)
        rootElement = parse.getroot()
        tag =  rootElement.tag

        for col in cols:

                for n in parse.iter(col):
                        to_xml.append("<field name='{}'>{}</field>".format(n.tag,n.text))
                        tags.append(n.tag)
        to_xml.insert( 0,"<add><doc>")
        to_xml.append("</doc></add>")

        with open(dir+'/new_{}'.format(i), 'w') as xml:
                for j in to_xml:
                        xml.write("%s" % j)
        print('Done')





