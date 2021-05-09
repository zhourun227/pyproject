import json
import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processors.script import ExecuteScript


class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        data=json.loads(text)
        # newObj=['age'].fillna(data['age'].mean(), inplace=True)
        #outputStream.write(bytearray(json.dumps(data).encode('utf-8')))
        outputStream.write(bytearray(json.dumps(data,sort_keys=True,indent=3,separators=(',',':'),skipkeys=True)))


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, ExecuteScript.REL_SUCCESS)
else:
    pass