from setuptools import setup

extras_require = {
    'shellcomplete': ['click_completion'],
    'tensorflow': [
        'tensorflow>=2.7.0',  # c.f. PR #1962
        'tensorflow-probability>=0.11.0',  # c.f. PR #1657
    ],
    'torch': ['torch>=1.10.0'],  # c.f. PR #1657
    'jax': ['jax>=0.2.10', 'jaxlib>=0.1.61,!=0.1.68'],  # c.f. PR #1962, Issue #1501
    'xmlio': ['uproot>=4.1.1'],  # c.f. PR #1567
    'minuit': ['iminuit>=2.7.0'],  # c.f. PR #1895
}
extras_require['backends'] = sorted(
    set(
        extras_require['tensorflow']
        + extras_require['torch']
        + extras_require['jax']
        + extras_require['minuit']
    )
)
extras_require['contrib'] = sorted({'matplotlib', 'requests'})
extras_require['test'] = sorted(
    set(
        extras_require['backends']
        + extras_require['xmlio']
        + extras_require['contrib']
        + extras_require['shellcomplete']
        + [
            'scikit-hep-testdata>=0.4.11',
            'pytest>=6.0',
            'coverage[toml]>=6.0.0',
            'pytest-mock',
            'requests-mock>=1.9.0',
            'pytest-benchmark[histogram]',
            'pytest-console-scripts',
            'pytest-mpl',
            'pydocstyle',
            'papermill~=2.3.4',
            'scrapbook~=0.5.0',
            'jupyter',
            'graphviz',
            'pytest-socket>=0.2.0',  # c.f. PR #1917
        ]
    )
)
extras_require['docs'] = sorted(
    set(
        extras_require['xmlio']
        + extras_require['contrib']
        + [
            'sphinx>=5.1.1',  # c.f. https://github.com/scikit-hep/pyhf/pull/1926
            'sphinxcontrib-bibtex~=2.1',
            'sphinx-click',
            'sphinx_rtd_theme',
            'nbsphinx!=0.8.8',  # c.f. https://github.com/spatialaudio/nbsphinx/issues/620
            'ipywidgets',
            'sphinx-issues',
            'sphinx-copybutton>=0.3.2',
            'sphinx-togglebutton>=0.3.0',
        ]
    )
)
extras_require['develop'] = sorted(
    set(
        extras_require['docs']
        + extras_require['test']
        + [
            'nbdime',
            'tbump>=6.7.0',
            'ipython',
            'pre-commit',
            'nox',
            'check-manifest',
            'codemetapy>=2.3.0',
            'twine',
        ]
    )
)
extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))


setup(
    extras_require=extras_require,
    use_scm_version=lambda: {'local_scheme': lambda version: ''},
)
