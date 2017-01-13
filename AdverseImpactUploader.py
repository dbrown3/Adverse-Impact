__author__ = 'mdema'

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os


class AdverseImpactUploader():

    def __init__(self):

        # The column headers from the input data (or file)
        self.xml_data = None

        #file system for storing files
        if not os.path.isdir(settings.MEDIA_ROOT + "adverseimpact/"):
            os.mkdir(settings.MEDIA_ROOT + "adverseimpact/")

        self.file_system = FileSystemStorage(location=settings.MEDIA_ROOT + "adverseimpact/")

    def read_data_from_file(self, filename):
        try:
            file_path = self.file_system.path(filename)
        except NotImplementedError:
            raise Exception('File not found for reading')

        self.xml_data = open(file_path, 'r').read()
