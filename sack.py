#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
########
# Sack #
########
#
# Identify connection of sessions for social engineering attacks
#
# @version     1.0
# @link        https://github.com/jofpin/sack
# @author      Jose Pino (Fraph), @jofpin | jofpin@gmail.com
# @copyright   2016 Sack / Framework social engineering attacks
#
# This file is the boot in Sack.
# For full copyright information this visit: https://github.com/jofpin/sack
#
# Copyright 2016 by Jose Pino <jofpin@gmail.com>
#**

from core.framework import sack
from core.generals import generals

# We generalize the main class of <sack>
app = sack()

# Request root home to run <sack> with all permissions
app.rootConnection()

if __name__ == "__main__":
    # General expression this is expressed after the root
    app.main()