from setuptools import setup

description = "Simplified tool for re-ranking images using CLIP given a text"

setup(
    name="clip_rerank",
    version="0.1.0",
    author="Mehdi Cherti",
    description=description,
    license="MIT",
    url="https://github.com/mehdidc/clip_rerank",
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['clip_rerank'],
    include_package_data=True,
    install_requires=['clize'],
)

