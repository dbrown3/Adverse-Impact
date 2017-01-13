__author__ = 'dbrown3'

import os
import math
import datetime
import xmltodict

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from docxtpl import DocxTemplate

from AdverseImpactUploader import AdverseImpactUploader

def adverse_impact_export_report(request):
    # Initialize variables
    profiles_list = list()
    company_name = ''
    # Initialize a response object
    response = HttpResponse(content_type='text/docx')
    response['Content-Disposition'] = 'attachment; filename="report.docx"'
    # define the template file directory
    file_dir = os.getcwd() + '/adverseimpact/templates/adverseimpact/Adverse_impact_report_template.docx'
    doc = DocxTemplate(file_dir)

    if 'xml_file' in request.FILES:

        # get uploaded XML file
        xml_file = request.FILES['xml_file']
        file_name = xml_file.name
        adverse_impact_uploader = AdverseImpactUploader()
        # write the file
        with open(adverse_impact_uploader.file_system.location + "/" + file_name, 'wb+') as destination:
            for chunk in xml_file.chunks():
                destination.write(chunk)
        # read the file
        adverse_impact_uploader.read_data_from_file(file_name)
        # parse the file

        xml_data_dict = xmltodict.parse(adverse_impact_uploader.xml_data)
        xml_data_content = xml_data_dict.get('report')
        context = dict()
        if xml_data_content is not None:

            #Title
            context['CompanyName'] = xml_data_content.get('CompanyName')
            #context['DateGenerated'] = current_time.strftime('%B %d, %Y')
            context['toDate'] = request.POST.get('end_date')
            if context['toDate'] == '':
                context['toDate'] = xml_data_content.get('toDate')

            context['fromDate'] = request.POST.get('start_date')
            context['Insert1'] = request.POST.get('profile_name')
            context['DateGenerated'] = xml_data_content.get('DateGenerated')
            #context['fromDate'] = xml_data_content.get('fromDate')
            #context['Insert1'] = xml_data_content.get('Insert1')

            #Data Collection
            context['SampleSize'] = xml_data_content.get('SampleSize')
            context['OnlyIncludeCandidatesWithAllDemographics'] = xml_data_content.get('OnlyIncludeCandidatesWithAllDemographics')
            context['DidNotReportAllDemoPercent'] = xml_data_content.get('DidNotReportAllDemoPercent')
            context['DidNotReportAllDemo'] = xml_data_content.get('DidNotReportAllDemo')

            #Ethnicity Adverse Impact Analysis
            context['RemoveT1Paragraph'] = xml_data_content.get('RemoveT1Paragraph')
            context['Ref29a'] = xml_data_content.get('Ref29a')
            context['EthnicityResponse'] = xml_data_content.get('EthnicityResponse')
            context['hasHispanic'] = xml_data_content.get('hasHispanic')
            context['Ref2'] = xml_data_content.get('Ref2')
            context['Ref3'] = xml_data_content.get('Ref3')
            context['Ref4'] = xml_data_content.get('Ref4')
            context['Ref5'] = xml_data_content.get('Ref5')
            context['RefT1a'] = xml_data_content.get('RefT1a')
            context['hasBlack'] = xml_data_content.get('hasBlack')
            context['Ref6'] = xml_data_content.get('Ref6')
            context['Ref7'] = xml_data_content.get('Ref7')
            context['Ref8'] = xml_data_content.get('Ref8')
            context['Ref9'] = xml_data_content.get('Ref9')
            context['RefT1b'] = xml_data_content.get('RefT1b')
            context['hasPacificIslander'] = xml_data_content.get('hasPacificIslander')
            context['Ref10'] = xml_data_content.get('Ref10')
            context['Ref11'] = xml_data_content.get('Ref11')
            context['Ref12'] = xml_data_content.get('Ref12')
            context['Ref13'] = xml_data_content.get('Ref13')
            context['RefT1c'] = xml_data_content.get('RefT1c')
            context['hasAsian'] = xml_data_content.get('hasAsian')
            context['Ref14'] = xml_data_content.get('Ref14')
            context['Ref15'] = xml_data_content.get('Ref15')
            context['Ref16'] = xml_data_content.get('Ref16')
            context['Ref17'] = xml_data_content.get('Ref17')
            context['RefT1d'] = xml_data_content.get('RefT1d')
            context['hasAmericanIndian'] = xml_data_content.get('hasAmericanIndian')
            context['Ref18'] = xml_data_content.get('Ref18')
            context['Ref19'] = xml_data_content.get('Ref19')
            context['Ref20'] = xml_data_content.get('Ref20')
            context['Ref21'] = xml_data_content.get('Ref21')
            context['RefT1e'] = xml_data_content.get('RefT1e')
            context['hasOther'] = xml_data_content.get('hasOther')
            context['Ref22'] = xml_data_content.get('Ref22')
            context['Ref23'] = xml_data_content.get('Ref23')
            context['Ref24'] = xml_data_content.get('Ref24')
            context['Ref25'] = xml_data_content.get('Ref25')
            context['RefT1f'] = xml_data_content.get('RefT1f')
            context['Ref26'] = xml_data_content.get('Ref26')
            context['Ref27'] = xml_data_content.get('Ref27')
            context['Ref28'] = xml_data_content.get('Ref28')
            context['RefT1Text'] = xml_data_content.get('RefT1Text')
            context['EthnicityNoResponsePercent'] = xml_data_content.get('EthnicityNoResponsePercent')
            context['EthnicityNoResponse'] = xml_data_content.get('EthnicityNoResponse')

            #Gender Adverse Impact Analysis
            context['RemoveT4Paragraph'] = xml_data_content.get('RemoveT4Paragraph')
            context['Ref109t4'] = xml_data_content.get('Ref109t4')
            context['GenderResponse'] = xml_data_content.get('GenderResponse')
            context['Ref70'] = xml_data_content.get('Ref70')
            context['Ref71'] = xml_data_content.get('Ref71')
            context['Ref72'] = xml_data_content.get('Ref72')
            context['Ref73'] = xml_data_content.get('Ref73')
            context['Ref74'] = xml_data_content.get('Ref74')
            context['Ref75'] = xml_data_content.get('Ref75')
            context['Ref76'] = xml_data_content.get('Ref76')
            context['RefT4Text'] = xml_data_content.get('RefT4Text')
            context['GenderNoResponsePercent'] = xml_data_content.get('GenderNoResponsePercent')
            context['GenderNoResponse'] = xml_data_content.get('GenderNoResponse')

            #Age Adverse Impact Analysis
            context['RemoveT7Paragraph'] = xml_data_content.get('RemoveT7Paragraph')
            context['Ref109t7'] = xml_data_content.get('Ref109t7')
            context['AgeResponse'] = xml_data_content.get('AgeResponse')
            context['Ref87'] = xml_data_content.get('Ref87')
            context['Ref88'] = xml_data_content.get('Ref88')
            context['Ref89'] = xml_data_content.get('Ref89')
            context['Ref90'] = xml_data_content.get('Ref90')
            context['Ref91'] = xml_data_content.get('Ref91')
            context['Ref92'] = xml_data_content.get('Ref92')
            context['Ref93'] = xml_data_content.get('Ref93')
            context['RefT7Text'] = xml_data_content.get('RefT7Text')
            context['AgeNoResponsePercent'] = xml_data_content.get('AgeNoResponsePercent')
            context['AgeNoResponse'] = xml_data_content.get('AgeNoResponse')

            #Adverse Impact Analysis Conclusions
            context['Ref107'] = xml_data_content.get('Ref107')


    # Render the document
    doc.render(context)
    doc.save(response)

    return response
