from test.helper import use_example


class part_1:
  @use_example(1)
  def test_example_1(self, problem):
    assert problem.solve_1() == 2

  def test_solution(self, problem):
    assert problem.solve_1() == 528


class part_2:
  @use_example(1)
  def test_example_1(self, problem):
    assert problem.solve_2() == 1

  def test_solution(self, problem):
    assert problem.solve_2() == 497
