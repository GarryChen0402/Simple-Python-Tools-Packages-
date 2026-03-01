from TxtFileParser import TextFileParser


if __name__ == '__main__':
    parser = TextFileParser()

    inputFile = './MarkdownTools/ParserTest.txt'
    outputFile = './MarkdownTools/parseResult.md'

    parser.Parse(inputFile, outputFile)