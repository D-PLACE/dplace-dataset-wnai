from setuptools import setup


setup(
    name='cldfbench_wnai',
    py_modules=['cldfbench_wnai'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-wnai=cldfbench_wnai:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
