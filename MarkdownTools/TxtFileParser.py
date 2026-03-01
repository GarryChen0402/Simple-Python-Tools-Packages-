import os

from Header import Header
from BaseLabel import BaseMDLabel

class TextFileParser:
    def __init__(self, splitText:str = '|&&|'):
        self.stringSplitText: str = splitText

    def Parse(self, inputFile:str, outputFile:str):
        if not os.path.exists(inputFile):
            print("Could not fild the input file for parse...")
            return
        if os.path.exists(outputFile):
            print("The output file is already existed...")
            return

        # read the markdown info from inputfile
        infos = []
        with open(inputFile, 'r') as f:
            lines = f.readlines()
            for line in lines:
                infos.append(line.split(self.stringSplitText))
        

        # generate the module infos
        modules: list[BaseMDLabel] = []
        for info in infos:
            if info[0] == 'header':
                modules.append(self._header_generate(info))
            else:
                #TODO: Other label
                pass

        # wirte the markdown text to outputfile 
        with open(outputFile, 'w') as f:
            for module in modules:
                f.write(str(module))
        
    def _header_generate(self, info: list[str]) -> BaseMDLabel:
        text = ''.join(info[2:])
        return Header(text, int(info[1]))
    


