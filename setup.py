from setuptools import setup, find_packages
setup(
    name = "mqtt_turtle",
    version = "0.1",
    packages = find_packages(),
    scripts = ['mqtt_turtle_receiver', 'mqtt_turtle_sender'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['pyev>=0.9.0', 'paho-mqtt>=1.1'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'mqtt_turtle': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "xc",
    author_email = "raidercodebear@gmail.com",
    description = "This is a mqtt benchmark tool",
    license = "GNU General Public License v3 (GPLv3)",
    keywords = "mqtt benchmark",
    url = "",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)