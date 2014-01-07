#!/usr/bin/env python
import os
import re

REGEX = re.compile(r'(\d{1,4}-\d{1,2}-\d{1,2}_[0]+)(\d+).(\w{1,4})',
				   re.I|re.U)
files = os.listdir(os.getcwdu())

for file_name in files:
	group = re.findall(REGEX, file_name)
	if not group:
		print("skipping: %s" % file_name)
		continue
	group = group[0]
	new_file_name = '%(iter)02d.%(ext)s' % {
		'iter': int(group[1]),
		'ext': group[2]
	}
	print("renaming '%(old)s' to '%(new)s'" % {
			'old': file_name,
			'new': new_file_name,
		}
	)
	os.rename(file_name, new_file_name)
	