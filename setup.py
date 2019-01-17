from setuptools import setup, find_packages

setup(
    name='taskwarrior_jrnl_hook',
    version='0.1.1',
    url='https://github.com/Hatoris/taskwarrior_jrnl_hook',
    description=(
        'A hook to add started task in taskwarrior to jrnl'
    ),
    author='Florian Bernard',
    author_email='florianxbernard@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "taskw",
        "babel"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'taskwarrior_jrnl_hook= taskwarrior_jrnl_hook:cmdline'
        ],
    },
)