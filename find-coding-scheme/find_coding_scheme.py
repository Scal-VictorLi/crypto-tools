import sys
import re

# first argument: unknown coding text
if len(sys.argv) != 2: sys.exit(2)
estr=sys.argv[1]

binrex = re.compile('^[01]+$', re.MULTILINE)
if(binrex.match(estr)): print 'binary'

octrex = re.compile('^[0-7]+$', re.MULTILINE)
if(octrex.match(estr)): print 'octal'

decrex = re.compile('^[0-9]+$', re.MULTILINE)
if(decrex.match(estr)): print 'decimal'

hexrex = re.compile('^[A-Fa-f0-9]+$', re.MULTILINE)
if(hexrex.match(estr)): print 'hexadecimal'

b64rex = re.compile('^[A-Za-z0-9+/]+[=]{0,2}$', re.MULTILINE)
if(b64rex.match(estr)): print 'base64'

uurex = re.compile('^(begin.*\n)?[\x20-\x60\n]+(end[\n]?)?$', re.MULTILINE)
if(uurex.match(estr)): print 'uuencode'

ascii85rex = re.compile('^[A-Za-z0-9!#$%&()*+\-;<=>?@^_`{|}~]+$', re.MULTILINE)
if(ascii85rex.match(estr)): print 'ascii85'

binhexrex = re.compile(r'^[A-NP-VX-Z0-9a-fh-mp-r\!\"\#\$\%\&\'\(\)\*\+\,\-\@\`\[\:]+$', re.MULTILINE)
if(binhexrex.match(estr)): print 'binhexrex'

xxrex = re.compile('^[A-Za-z0-9+\-]+$')
if estr.startswith('begin'):
	tstr = estr.split('\n')
	tstr = ''.join(tstr[1:len(tstr)-1])
	if(xxrex.match(tstr)): print 'xxencode'
if(xxrex.match(estr)): print 'xxencode'
