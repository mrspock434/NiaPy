# encoding=utf8
# pylint: disable=mixed-indentation, multiple-statements
from unittest import skip

from NiaPy.tests.test_algorithm import AlgorithmTestCase, MyBenchmark
from NiaPy.algorithms.other import TabuSearch

class TSTestCase(AlgorithmTestCase):
	@skip('Not implemented jet')
	def test_custom_works_fine(self):
		ts_custom = TabuSearch(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, benchmark=MyBenchmark(), seed=self.seed)
		ts_customc = TabuSearch(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, benchmark=MyBenchmark(), seed=self.seed)
		AlgorithmTestCase.algorithm_run_test(self, ts_custom, ts_customc)

	@skip('Not implemented jet')
	def test_griewank_works_fine(self):
		ts_griewank = TabuSearch(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, benchmark='griewank', seed=self.seed)
		ts_griewankc = TabuSearch(NP=10, D=self.D, nFES=self.nFES, nGEN=self.nGEN, benchmark='griewank', seed=self.seed)
		AlgorithmTestCase.algorithm_run_test(self, ts_griewank, ts_griewankc)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
