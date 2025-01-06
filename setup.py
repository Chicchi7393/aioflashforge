import os
import re
from setuptools import setup, find_packages

packages = find_packages()

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

with open(
    os.path.join(os.path.dirname(__file__), packages[0], "__init__.py"),
    "r",
    encoding="utf-8",
) as f:
    kwargs = {
        var.strip("_"): val
        for var, val in re.findall(
            r'^(__\w+__)\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
        )
    }
    kwargs["author_email"] = kwargs.pop("email", "")

setup(
    name="aioflashforge",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=packages,
    install_requires=["aiohttp", "appdirs", "typing-extensions"],
    python_requires=">=3.7",
    **kwargs
)
