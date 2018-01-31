#DIST:
from setuptools  import setup
import json

settings = json.loads(open("config.json").read())


package_name = str(settings["package"])
setup(
name=package_name,
version="0.0.2.2",
author="thinkersilver",
author_email="myonlineprofile2012@gmail.com",
packages=[package_name],
scripts=['bin/%s' % package_name],
description="Publish articles",
include_package_data=True,
package_data={
package_name: ["site/*.*"],
'':['config.json']}

,exclude_package_data={
package_name: ["site/node_modules/*"] }

)