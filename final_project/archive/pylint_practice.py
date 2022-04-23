import pylint.lint
pylint_opts = ['--disable=line-too-long', 'translator.py']
pylint.lint.Run(pylint_opts)