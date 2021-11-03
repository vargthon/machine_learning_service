if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))

import unittest


import subject_test
import domain_test


# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()


suite.addTests(loader.loadTestsFromModule(subject_test))
suite.addTests(loader.loadTestsFromModule(domain_test))


runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)