import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json_env",
    version="1.0.9",
    author="Asashishi_Nyan!",
    author_email="1072903224@qq.com",
    description="This is a simple environment variable solution for .json file, which is based on 'os' and 'json' lib\n. Use this lib and you don't need to worry about type issues with 'os.environ' it's all handled by this package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asashishi/json_env",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.7",
)
