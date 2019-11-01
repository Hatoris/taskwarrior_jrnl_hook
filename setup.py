from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='taskwarrior_jrnl_hook',
    version='0.1.5',
    url='https://github.com/Hatoris/taskwarrior_jrnl_hook',
    description=(
        'A hook to add started task in taskwarrior to jrnl'
    ),
    author='Florian Bernard',
    author_email='florianxbernard@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "taskw",
        "babel",
        "pyyaml"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_jrnl_hook= taskwarrior_jrnl_hook:cmdline'
        ],
    },
)