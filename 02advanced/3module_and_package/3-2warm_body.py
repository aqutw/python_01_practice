import math

from math import pow, sin, log

import math, logging
math.log(10)
logging.log(10)

from math import log
from logging import log as logger   # logging的log现在变成了logger, alias log module of a package
print log(10)   # 调用的是math的log
logger(10, 'import from logging')   # 调用的是logging的log

import simplejson as json #alias simplejson module of a package
