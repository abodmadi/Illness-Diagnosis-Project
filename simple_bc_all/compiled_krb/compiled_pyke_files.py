# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'dquestion.kqb'):
           [1672504914.245, 'dquestion.qbc'],
         ('', '', 'dfact.kfb'):
           [1672501875.462, 'dfact.fbc'],
         ('', '', 'drules.krb'):
           [1672504914.336, 'drules_bc.py'],
        },
        compiler_version)

