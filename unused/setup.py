from setuptools import setup

setup(
    name='code_exec',
    version='0.1',
    description='Code execution XBlock',
    packages=['code_exec'],
    install_requires=['XBlock', 'xblock-utils'],
    entry_points={
        'xblock.v1': [
            'code_exec = code_exec:CodeExecXBlock',
        ]
    }
)