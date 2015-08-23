import codecs
import os

class TxtFileHandle:
    def __init__(self):
        self._encoding = "utf8"
        self._encodingList = ["utf8", "utf_8_sig", "cp932", "shift_jis", "ascii", "cp936", "cp1252"]
        self._filePathName = ""

    def ReadTxtFile(self, filePathName):
        """
        A generator which return one decoded line each time.
        """

        fr = codecs.open(filePathName, "rb")

        data = fr.read()
        for EncodingName in self._encodingList:
            try:
                codecs.decode(data, EncodingName)
                break

            except ValueError:
                continue

        self._filePathName = filePathName
        self._encoding = EncodingName

        fr.seek(0, os.SEEK_SET)

        line = True
        while line:
            line = fr.readline()
            line = codecs.decode(line, self._encoding)
            
            # for encoding in self._encodingList:
            #     try:
            #         line = codecs.decode(line, encoding)
            #         break

            #     except ValueError:
            #         continue

            # self._filePathName = filePathName
            # self._encoding = encoding

            yield line

        fr.close()

    def WriteTxtFile(self, data):
        if "" == self._filePathName:
            return False
        
        try:
            data = codecs.encode(data, self._encoding)
            
            f = open(self._filePathName, "wb")
            f.write(data)
            f.close()
            return True

        except:
            return False