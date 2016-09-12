from core.framework import sack
from core.generals import generals

# Module global configs
doAuthor = "Jose Pino, @jofpin"
doVersion = "1.0"
doDate = "30-08-2016"
doDescription   = "Example module"

Framework = sack()

class example(object):
    def __init__(self, optionExample):
        self.optionExample = optionExample

    def demoFunc(self, text):
    	generals.Go(text + ": " + "%s" % (self.optionExample))


def boot(args):
    try:
        optionExample = args[2]
    except IndexError:
        Framework.usageOpt("example <string>")
        return
    run = example(optionExample)
    run.demoFunc("Here comes what you've written")